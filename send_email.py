import smtplib, ssl

def sendEmail(message):
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "geethaprabuo812@gmail.com"
    password = "1234"
    reciever_email = "geethaprabuo812@gmail.com"

    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context = context)
        server.login(sender_email, password)
        server.sendmail(sender_email, reciever_email, message)
    except Exception as e:
        print(e)
        server.quit()