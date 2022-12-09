from email.message import EmailMessage
import ssl
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()


emailSender   = os.getenv('GOOGLE_EMAIL')
emailPassword = os.getenv('GOOGLE_PASSWORD')

# Generate an email in https://temp-mail.org/es/
emailReceiver = os.getenv('EMAIL_RECIPIENT')

subject = "Don't forget to subscribe"

body = """

When you watch a video, please hit subscribe

"""

em = EmailMessage()
em['From'] = emailSender
em['To'] = emailReceiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(emailSender, emailPassword)
    smtp.sendmail(emailSender, emailReceiver, em.as_string())

