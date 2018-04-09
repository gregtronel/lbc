## LeBonCoin Filter/Alert Bot
----

### Some notes
- Find posts related to sales (ventes/offres) on [leboncoin.fr](https://www.leboncoin.fr) and relay them to email address(es)
- Email and target URL configuration is done in ```config.py```
- Search parameters are passed as command line arguments (python lbc.py --help)
- Only tested on real estate sales (ventes immobilieres) but it should be easily extendable to other sections of the site directly from the config file
    - Feel free to test and confirm to above, thought I'll probably get to it eventually.
- Google how to setup a "cronjob" if interested in running the script on a specific schedule (e.g every day, at the 30th min of each hour)
- ~ alpha (docstrings are still missing, but I'll probably get around to it)
- Any contribution is welcome

## Install/Run on Mac/Linux:
1. ```$ git clone <this project dir>```
2. ```$ pip install -r requirements.txt --user```
3. Edit ```config.py``` with email information
4. ```$ python lbc.py --help``` for help about search parameters

### Example Usage:
To send a mail containing the 10 latest posts about appartments or houses sales in Lyon (districts/arrondissements 1, 2 or 3) between prices 300k and 500k.
```python lbc.py --region rhone_alpes --location 69001 69002 69003 --minprice 300000 --maxprice 500000 --maxmail 10 --search appartement maison```

