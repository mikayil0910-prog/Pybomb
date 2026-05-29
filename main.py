from email.mime.text import MIMEText
import smtplib
import password

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login('pybombpython@gmail.com', password.PASSWORD)

    email_to = input("Where to send?: ")
    number = int(input("How many mails?: "))
    message = input("Your message: ")
    subject = input("Your subject: ")

    for i in range(number):
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = 'pybombpython@gmail.com'
        msg['To'] = email_to

        server.sendmail("pybombpython@gmail.com", email_to, msg.as_string())

        print(f"Sent email number {i+1}")

    server.quit()
    print("Done!")

except Exception as e:
    print(f"Error: {e}")