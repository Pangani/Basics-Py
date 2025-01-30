import smtplib

server = smtplib.SMTP('smtp.gmail.com', 25)
server.ehlo()

with open('password.txt', 'r') as f:
    password = f.read().strip()

server.login('roypangani@gmail.com', password)
