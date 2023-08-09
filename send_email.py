import smtplib, ssl
host = "smtp.gmail.com"
port = 465
username = "jhonatanjk125@gmail.com"
password = "cajzcoqzmnpqrker"
context = ssl.create_default_context()
receiver = "jhonatanjk125@gmail.com"
message = """\
Subject: Hi!
How are you?"""
with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username,password)
    server.sendmail(username, receiver, message)