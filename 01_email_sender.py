from email.message import EmailMessage
import ssl
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()


def prepareData():

    emailSender   = os.getenv('GOOGLE_EMAIL')
    emailPassword = os.getenv('GOOGLE_PASSWORD')
    emailReceiver = os.getenv('EMAIL_RECIPIENT')

    emailSubject = "Don't forget to subscribe"

    emailBody = """

    When you watch a video, please hit subscribe

    """

    return {
        'from'    : emailSender,
        'password': emailPassword,
        'to'      : emailReceiver,
        'subject' : emailSubject,
        'message' : emailBody
    }


def sendEmail():

    config        = prepareData()

    em            = EmailMessage()
    em['From']    = config['from']
    em['To']      = config['to']
    em['subject'] = config['subject']
    em.set_content(config['message'])

    context       = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(config['from'], config['password'])
        smtp.sendmail(config['from'], config['to'], em.as_string())

    print('=' * 10, ' ' * 5, 'Email enviado exitosamente', ' ' * 5, '=' * 10)

def main():
    sendEmail()


if __name__ == "__main__":
    main()