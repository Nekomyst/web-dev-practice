import pyrebase
from getpass import getpass

firebaseConfig = {
	# firebase-credentials.json
}

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()
 
 
email = input("Please Enter Your Email Address : \n")
password = getpass("Please Enter Your Password : \n")
 
#create users
#user = auth.create_user_with_email_and_password(email, password)
#print("Success .... ")
 
 
login = auth.sign_in_with_email_and_password(email, password)
 
#send email verification
auth.send_email_verification(login['idToken'])
 
 
#reset the password
auth.send_password_reset_email(email)
 
print("Success ... ")
