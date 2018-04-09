import argparse
from pprint import pprint

def parse_args(print_args=False):
    """
    """
    parser = argparse.ArgumentParser(description="LeBonCoin.fr Filter/Alert Bot")
    
    parser.add_argument("-r", "--region", metavar="region", dest="region",
                        help="Region", default="")
    parser.add_argument("-l", "--location", metavar="location", dest="location", nargs="+",
                        help="Location (zip code)", default=[])
    parser.add_argument("-s", "--search", metavar="search", dest="searches", nargs="+",
                        help="Searches to perform", default=["Appartement"])
    parser.add_argument("-minp", "--minprice", metavar="minprice", dest="minprice",
                        help="minimum price value", default="")
    parser.add_argument("-maxp", "--maxprice", metavar="maxprice", dest="maxprice",
                        help="maximum price value", default="")
    parser.add_argument("-minr", "--minroom", metavar="minroom", dest="minroom",
                        help="minimum num of rooms", default="")
    parser.add_argument("-maxr", "--maxroom", metavar="maxroom", dest="maxroom",
                        help="maximum num of rooms", default="")
    parser.add_argument("-mina", "--minarea", metavar="minarea", dest="minarea",
                        help="minimum area in m2", default="")
    parser.add_argument("-maxa", "--maxarea", metavar="maxarea", dest="maxarea",
                        help="maximum area in m2", default="")
    parser.add_argument("-m", "--maxmail", metavar="maxmail", dest="maxmail",
                        help="Max # of emails sent", default="10")
    parser.add_argument("-u", "--email_subject", metavar="email-subject", dest="email_subject",
                        help="Email's subject", default="Item(s) matched your search")
    # TODO move below to config
    #parser.add_argument("-e", metavar="email-to", dest="email_to",
    #                    help="Email to send it to", default="")
    #parser.add_argument("-f", metavar="email-from", dest="email_from",
    #                    help="Email to send it from", default="")
    #parser.add_argument("--smtp-server", metavar="smtp-server", dest="server",
    #                    help="SMTP server to use", default="localhost")
    
    if print_args:
        print '\n'
        for k,v in sorted(vars(parser.parse_args()).items()):
            print "{}: {}".format(k, v)
        print '\n'
    return parser.parse_args()

