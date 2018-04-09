import os

config = {

    # LBC specific url info
    'section':      'ventes_immobilieres/offres/',
    'lbcbase':      'https://www.leboncoin.fr/', 
    
    # (source) email address from which mails are sent
    'source_usr':   "usr@gmail.com", 
    'source_pwd':   "pwd",

    # smtmp auth (change as nedded)
    'smtp_addr':    'smtp.gmail.com',
    'smtp_port':    587,
    
    # (destination) email addresses where mails are sent to
    'destinations': ["usr@gmail.com", "usr2@yahoo.com"],
    
    # local db/log directory
    'lbc_dir':      '.lbc',
}
    
    
def get_config():
    return config


