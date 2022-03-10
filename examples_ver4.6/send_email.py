import smtplib

def send_email(body):    

    gmail_user = 'alert.exceed.limits@gmail.com'
    gmail_password = 'Hello@9801'

    sent_from = gmail_user
    to = ['aattia@admix.com', 'jmccalmont@admix.com']
    subject = 'Alert_Exceeding_Limits_Fast_Feed is in DANGER!'
    #body = ''

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(sent_from, to, email_text)
        smtp_server.close()
        print ("Email sent successfully!")
    except Exception as ex:
        print ("Something went wrong….",ex)