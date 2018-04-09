import sys, os, re
import urllib
import requests
import sqlite3
from datetime import datetime
from bs4 import BeautifulSoup as bs
from pdb import set_trace as b
from pprint import pprint

import parsecmd
import logger
import mapping
import mailing
import config


class LBCParser():
    """
    """
    
    def __init__(self):
        """
        """
        #self.args = parse_args()
        self.destinations = cfg['destinations']
        self.section = cfg['section']
        self.baseUrl = os.path.join(cfg['lbcbase'], self.section)
        
        # create actual url based on args
        self.url = self.get_url_from_args(self.baseUrl, args)
        

    def get_db(self):
        """
        """
        self.db = sqlite3.connect('{}/db'.format(cfg['lbc_dir']))
        self.db.execute("""
        CREATE TABLE IF NOT EXISTS links (
          url TEXT UNIQUE,
          date DATETIME,
          seen BOOL DEFAULT 0,
          nb_views INTEGER,
          emailed BOOL DEFAULT 0
        );""")

    
    def get_url_from_args(self, baseUrl, args):
        """
        """
        url = baseUrl
        if args.region:
            url += "{}/".format(args.region)
        if args.location:
            locstr = '%20'
            if len(args.location) > 3:
                logger.warning('LBC only allows up to 3 different locations (last one(s) will be ignored)')
            for loc in args.location:
                locstr += '{}%2C%20'.format(loc)
            locstr = re.sub('%2C%20$', '', locstr)
            url +=  "?th=1&location={}".format(locstr)
        if args.searches:
            cat_searches = "q="
            for srch in args.searches:
                cat_searches += "{}%20".format(srch)
            url+='&'+cat_searches
        if args.minprice or args.maxprice:
            ps, pe = (args.minprice, args.maxprice)
            ps_idx, pe_idx = (u'', u'')
            if ps:
                # get closest mapped index for corresponding value
                ps_idx = sorted([(i, abs(int(x.replace('+',''))-int(ps)))\
                    for x,i in mapping.price_map.items()], key=lambda x: x[1])[0][0]
            if pe:
                pe_idx = sorted([(i, abs(int(x.replace('+',''))-int(pe)))\
                    for x,i in mapping.price_map.items()], key=lambda x: x[1])[0][0]
            url += "&ps={}&pe={}".format(ps_idx, pe_idx)
        if args.minarea or args.maxarea:
            sqs, sqe = (args.minarea, args.maxarea)
            sqs_idx, sqe_idx = (u'', u'')
            if sqs:
                sqs_idx = sorted([(i, abs(int(x.replace('+',''))-int(sqs)))\
                    for x,i in mapping.surface_map.items()], key=lambda x: x[1])[0][0]
            if sqe:
                sqe_idx = sorted([(i, abs(int(x.replace('+',''))-int(sqe)))\
                    for x,i in mapping.surface_map.items()], key=lambda x: x[1])[0][0]
            url += "&sqs={}&sqe={}".format(sqs_idx, sqe_idx)
        if args.minroom or args.maxroom:
            ros, roe = (args.minroom, args.maxroom)
            ros_idx, roe_idx = (u'', u'')
            if ros:
                ros_idx = sorted([(i, abs(int(x.replace('+',''))-int(ros)))\
                    for x,i in mapping.piece_map.items()], key=lambda x: x[1])[0][0]
            if pe:
                roe_idx = sorted([(i, abs(int(x.replace('+',''))-int(roe)))\
                    for x,i in mapping.piece_map.items()], key=lambda x: x[1])[0][0]
            url += "&ros={}&roe={}".format(ros_idx, roe_idx)
        return url

    

    def get_links(self):
        """
        """
        log.info("Searching for {}".format(args.searches))
        self.links = []
        #url = baseUrl + urllib.urlencode({"q": search})
        pageSoup = bs(requests.get(self.url).text, "html.parser")
        # We search all the link
        for i, aTag in enumerate(pageSoup.findAll('a')):
            href = aTag.get('href')
            if href:
                # target matches via regex
                match = re.search(r"\d{8,12}", href)
                if match and self.section.replace('offres/','') in href:
                    self.links.append(href)
        # only keep N links (see maxmail argument)
        if args.maxmail:
            self.links = self.links[:int(args.maxmail)]



    def get_mail_body(self):
        """
        """
        self.num_mail = 0
        self.text = '<ul>\n'
        db_query = "select rowid, url from links where emailed=0;"
        for rowid, url in self.db.execute(db_query):
            log.info("New link found: {}.".format(url))
            self.text += '<li><a href="{url}">{url} (#{id})</a></li>\n'.format(id=rowid, url=url)
            self.db.execute("update links set emailed=1 where rowid=?", (rowid,))
            self.num_mail += 1
        self.text += '</ul>\n'
        self.text = ("{} article(s) found:<br />".format(self.num_mail)) + '\n' + self.text
        

    def send_mail(self):
        """
        """
        if self.num_mail > 0:
            log.info("Sending to the following address(es):\n {}".format(self.destinations))
            mailing.send_message(self.text, self.destinations)
            self.db.commit()
        else:
            log.info("Nothing new to send :(")


def main():
    """
    """
    # instanciate LPCparser
    parser = LBCParser()

    # init db
    parser.get_db()

    # get all links according to request
    parser.get_links()

    # update db
    for link in parser.links:
        parser.db.execute("insert or ignore into links ('url','date') values (?,?);", (link, datetime.now()))
    parser.db.commit()
    
    # get mail body by querying db for new links that yet weren't sent
    parser.get_mail_body()

    # send mail(s)
    parser.send_mail()
    
    # close db
    parser.db.close()


def check_config_is_default(cfg, log):
    """
    """
    try:
        assert (not 'usr' in cfg['destinations'] and not 'usr' in cfg['source_usr'])
    except AssertionError:
        err = "Edit config.py with 'source' and 'destinations' info before running the program.\n"
        log.exception(err); print err
        sys.exit()
 


if __name__ == "__main__":
    
    # init - parse args, get config, get logger 
    args    = parsecmd.parse_args(print_args=False)
    cfg     = config.get_config()
    log  = logger.get_logger()
    
    # check config file is still default
    check_config_is_default(cfg, log)

    # run
    log.info('Start')
    main()
    log.info('End')


