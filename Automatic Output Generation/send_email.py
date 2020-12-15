from email.message import EmailMessage
from os import path
import mimetypes
import smtplib
import getpass

message = EmailMessage()

sender = "me@example.com"
recipient = "you@example.com"
message["From"] = sender
message["To"] = recipient
message["Subject"] = 'Greetings from {} to {}!'.format(sender, recipient)

body = """Hey there!
...
... I'm learning to send emails using Python!"""
print(message)

attachment_path = "Automatic Output Generation\ppl.jpg"
attachment_filename = path.basename(attachment_path)

mime_type, _ = mimetypes.guess_type(attachment_path)
mime_type, mime_subtype = mime_type.split('/', 1)
print(mime_type, mime_subtype)

with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(), maintype=mime_type, subtype=mime_subtype, filename=path.basename(attachment_path))

# print(message)

mail_server = smtplib.SMTP_SSL('smtp.example.com')
mail_pass = getpass.getpass("Enter password: ")


mail_server.login(sender, mail_pass)
print("Authentication failed! Please try again!")

mail_server.send_message(message)
mail_server.quit()


