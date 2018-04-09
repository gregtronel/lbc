import argparse
from pprint import pprint

def parse_args(print_args=False):
    """
    """
    parser = argparse.ArgumentParser(description="LeBonCoin.fr Filter/Alert Bot")
    
    parser.add_argument("-r", metavar="region", dest="region",
                        help="Region", default="ile_de_france")
    parser.add_argument("-l", metavar="location", dest="location", nargs="+",
                        help="Location (zip code)", default=["Paris"])
    parser.add_argument("-s", metavar="search", dest="searches", nargs="+",
                        help="Searches to perform", default=["Appartement"])
    parser.add_argument("-minp", metavar="minprice", dest="minprice",
                        help="minimum price value", default="")
    parser.add_argument("-maxp", metavar="maxprice", dest="maxprice",
                        help="maximum price value", default="")
    parser.add_argument("-minr", metavar="minroom", dest="minroom",
                        help="minimum num of rooms", default="")
    parser.add_argument("-maxr", metavar="maxroom", dest="maxroom",
                        help="maximum num of rooms", default="")
    parser.add_argument("-mina", metavar="minarea", dest="minarea",
                        help="minimum area in m2", default="")
    parser.add_argument("-maxa", metavar="maxarea", dest="maxarea",
                        help="maximum area in m2", default="")
    #parser.add_argument("-e", metavar="email-to", dest="email_to",
    #                    help="Email to send it to", default="")
    #parser.add_argument("-f", metavar="email-from", dest="email_from",
    #                    help="Email to send it from", default="")
    parser.add_argument("-m", metavar="maxmail", dest="maxmail",
                        help="Max # of emails sent", default="10")
    parser.add_argument("-u", metavar="email-subject", dest="email_subject",
                        help="Email's subject", default="Item(s) matched your search")
    parser.add_argument("--smtp-server", metavar="smtp-server", dest="server",
                        help="SMTP server to use", default="localhost")
    
    if print_args:
        print '\n'
        for k,v in sorted(vars(parser.parse_args()).items()):
            print "{}: {}".format(k, v)
        print '\n'
    return parser.parse_args()

