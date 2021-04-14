import smtplib

to = input('Please enter the email of the recipient: ')             # Create variables for the destination address and the Body of text for the email
body = input('Please type the body of the email:\n ')

def sendMail(to,  body):
    server = smtplib.SMTP('smtp.gmail.com', 587)                    # Set the SMTP details for the server
    server.ehlo()                                                   # Open the proceeding s for the sending of email    
    server.starttls()                                               # Start TLS encryption for sending the password not in clear text
    server.login('', '')       # Log into the SMTP server with a valid account
    server.sendmail('', to,body)          # Set the send from address and then input the variables for the destination and text body
    server.close()                                                  # Close the session

sendMail(to,body)                                                   # Call the function to start the process
