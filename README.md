** LeBonCoin Filter/Alert Bot **


- Find posts related to sales (ventes/offres) on leboncoin.fr and relay them to email address(es)
- Email and target URL configuration is done in ```config.py```, search parameters are passed as command line arguments (python lbc.py --help)
- Only tested on real estate sales (ventes immobilieres) but it should be easily extendable to other section from the config file
    - Feel free to test and confirm
- Any contribution is welcome
- Google "cronjob" if interested in running the script on a specific schedule (e.g every day, at the 30th min of each hour)
- ~ alpha (docstrings are still missing, but I'll probably get around to it)


- Install/Run on Mac/Linux:

```git clone <this project dir>```
```pip install -r requirements.txt --user```
```python lbc.py --help```

