import os, sys
from pdb import set_trace as b
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
 
import config
cfg = config.get_config()


def send_message(msg, dests, args, subject="Sent from local"):

    content= """\
    {}
    """.format(msg)

    try:	
	server = smtplib.SMTP(cfg['smtp_addr'], cfg['smtp_port'])
	server.starttls()
	server.login(cfg['source_usr'], cfg['source_pwd'])
        
        msg = MIMEMultipart()
        if args.email_subject:
            msg['Subject'] = args.email_subject
        else:
            msg['Subject'] = subject
        msg['From'] = cfg['source_usr']
	msg.attach(MIMEText(content, 'html'))
        for dest in dests:
            msg['To'] = dest
	    server.sendmail(cfg['source_usr'], dest, msg.as_string())
	
        server.quit()

    except Exception, exc:
	sys.exit( "mail failed; %s" % str(exc) ) # give a error message

