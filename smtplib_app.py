# import smtplib
# from email.mime.text import MIMEText
# from dotenv import load_dotenv
# import os

# load_dotenv()
# gmail_address = os.getenv("GMAIL_ADDRESS")
# gmail_app_password = os.getenv("GMAIL_APP_PASSWORD")

# msg = MIMEText("Hello from Python!")
# msg["Subject"] = "Remindar"
# msg["From"] = "emanshatnawi185@gmail.com"
# msg["To"] = "friend@gmail.com"

# try:
#     with smtplib.SMTP("smtp.gmail.com", 587) as server:
#         server.starttls()
#         server.login(gmail_address, gmail_app_password)
#         server.send_message(msg)
#     print("Email sent successfully!")
# except smtplib.SMTPAuthenticationError as e:
#     print(f"Authentication failed. Check your email address and app password. Error: {e}")
# except Exception as e:
#     print(f"An error occurred: {e}")