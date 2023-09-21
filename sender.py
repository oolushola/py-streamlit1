import smtplib
import ssl


def sendEmail(message, receiver):
    host = "smpt.gmail.com"
    port = 465

    username = "odejobiolushola@gmail.com"
    password = "uvjm dpig yymz zvef"

    my_context = ssl.create_default_context()

    try:
        with smtplib.SMTP(host, port, timeout=30) as server:
            server.login(username, password)
            server.sendmail(username, receiver, message)
    except Exception as e:
        print(e)
