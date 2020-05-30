# Python program for sending email
# Import the smtplib module
# The smtplib module defines an SMTP client session object
# that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon.
import smtplib
import urllib.request as urllib
# Senders email
sender_email = "link2pm333@gmail.com"
# Receivers email
rec_email = "priyansh.m333@gmail.com"

message = "Hie thier, Your Model has been Trained with accuracy more than 90%...Thank You"
# Initialize the server variable
server = smtplib.SMTP('smtp.gmail.com', 587)
# Start the server connection
server.starttls()
# Login
server.login("sender mail", "sender pass")
print("Login Success!")
# Send Email
server.sendmail("reciever name", "sneder name", message)
print(f"Email has been sent successfully to {rec_email}")
