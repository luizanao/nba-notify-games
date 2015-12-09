import os
from datetime import datetime

diretorio = "/home/luizfelipe/Desktop/nba/"

def parse_games():

	for entry in os.listdir(diretorio):
	    if (entry.endswith(".txt")):
	        f = open(diretorio + entry, 'r')
	        games = f.read().split("\n")
	        
	        for game in games:
		        splited_sting = game.split(',')
		        time, teams = splited_sting[1].split('-')
		        time = time[:-1]+":00"
		        date = datetime.strptime(splited_sting[0]+ ' ' + time.replace('h',':') , '%d/%m/%Y %H:%M:%S')
		        
		        print date, teams

	send_email()

def send_email():
    import smtplib

    gmail_user = ""
    gmail_pwd = ""
    FROM = ""
    TO = ['']#recipient if type(recipient) is list else [recipient]
    SUBJECT = 'test'
    TEXT = "test email"

    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print 'successfully sent the mail'
    except:
        print "failed to send mail"


if __name__ == "__main__":
	parse_games()