import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = "yaseen"
email['to'] = "test@gmail.com"
email['subject'] = "You won 1,000,000 dollars..."

email.set_content("I am a Python Master 🔥")

try:
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login("test@gmail.com", "123456789")
        smtp.send_message(email)
        print("✅ Email sent successfully!")

except Exception as e:
    print(f"❌ Error: {e}")
