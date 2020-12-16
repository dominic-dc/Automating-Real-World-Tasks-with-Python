import psutil
import shutil
import socket
import emails

def check_disk_usage():
    du = shutil.disk_usage("/")
    free = du.free / du.total * 100
    return free > 20

def check_cpu_usage():
    usage = psutil.cpu_percent(60)
    return usage < 80

def check_free_memory():
    available = psutil.virtual_memory().available
    available_mb = available / 1024 ** 2
    return available_mb > 500

def check_hostname():
    ip_add = socket.gethostbyname('localhost')
    return ip_add == "127.0.0.1"

def report_issue(issue):
    sender = "automation@example.com"
    recipient = "student-04-4397b9b45ea1@example.com"
    subject = issue
    body = "Please check your system and resolve the issue as soon as possible."
    message = emails.generate_email(sender, recipient, subject, body)
    emails.send_email(message)

if not check_cpu_usage():
    subject = "Error - CPU usage is over 80%"
    report_issue(subject)

if not check_disk_usage():
    subject = "Error - Available disk space is less than 20%"
    report_issue(subject)

if not check_free_memory():
    subject = "Error - Available memory is less than 500MB"
    report_issue(subject)

if not check_hostname():
    subject = "Error - localhost cannot be resolved to 127.0.0.1"