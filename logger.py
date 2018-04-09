import os
import logging
import logging.handlers

import config
cfg = config.get_config()

def get_logger():
    """
    """
    log = logging.getLogger("default")
    log.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s | %(levelname)8s | %(message)s")
    sh = logging.StreamHandler()
    sh.setFormatter(formatter)
    log.addHandler(sh)
    
    if not os.path.isdir(cfg['lbc_dir']):
        os.mkdir(cfg['lbc_dir'])
    
    rh = logging.handlers.RotatingFileHandler(
        '{}/log'.format(cfg['lbc_dir']), 
        maxBytes=256*1024, backupCount=10)
    rh.setFormatter(formatter)
    log.addHandler(rh)
    
    return log


