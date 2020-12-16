import os 
import datetime
import reports
import emails
import datetime

today = datetime.datetime.now().strftime("%B %d, %Y")

user = os.path.expanduser("~")
directory = os.path.join(user, "supplier-data", "descriptions")
files = os.listdir(directory)

def process_txt_files(files):
    paragraph = ""
    for file in files:
        with open(directory + "/" + file) as f:
            lines = f.readlines()
            name = lines[0].strip()
            weight = lines[1].strip()
            paragraph += "name: " + name + "<br/>" + "weight: " + weight + "<br/><br/>"

    return paragraph

if __name__ == "__main__":
    paragraph = process_txt_files(files)
    title = "Processed Update on " + today
    reports.generate_report("/tmp/processed.pdf", title, paragraph)

    sender = "automation@example.com"
    recipient = "student-04-4397b9b45ea1@example.com"
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attachment = "/tmp/processed.pdf"

    message = emails.generate_email(sender, recipient, subject, body, attachment)
    emails.send_email(message)