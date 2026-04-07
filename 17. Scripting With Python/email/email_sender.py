import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


html = Template(Path("index.html").read_text())


email = EmailMessage()
email['from'] = "from_mail@gmail.com"
email['to'] = "to_mail@gmail.com"
email['subject'] = "<E-mail-subject>..."

# email.set_content(html.substitute(name="YaseenAmin"))

email.set_content(html.substitute({"name": "YaseenAmin"}), "html")

try:
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login("from_mail@gmail.com", "gooale-app-password")
        smtp.send_message(email)
        print("✅ Email sent successfully!")

except Exception as e:
    print(f"❌ Error: {e}")
