import os

from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

SENDER_EMAIL = os.environ.get("SENDER_EMAIL")
SENDER_PASSWORD = os.environ.get("SENDER_PASSWORD")
RECEIVER_EMAIL = os.environ.get("RECEIVER_EMAIL")
SMTP_SERVER = "smtp.gmail.com"  # Fixed server string
SMTP_PORT = 587

@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/send-email", methods=["POST"])
def send_email():
    form_data = request.form.to_dict()
    print(form_data)
    name = form_data.get("name", "").strip()
    email = form_data.get("email", "").strip()
    phone = form_data.get("phone", "").strip()
    subject = form_data.get("subject", "").strip()
    message = form_data.get("message", "").strip()

    msg = MIMEMultipart("alternative")

    # Your authenticated email
    msg["From"] = SENDER_EMAIL

    # Your email
    msg["To"] = RECEIVER_EMAIL

    # VERY IMPORTANT:
    # Replies will go directly to the person who submitted the form
    msg["Reply-To"] = email

    msg["Subject"] = f"New Portfolio Contact: {subject}"

    body = f"""
You received a new message from your portfolio website.

Name: {name}
Email: {email}
Phone: {phone}
Subject: {subject}

Message:
{message}

--------------------------------
This message was sent from your portfolio contact form.
"""

    msg.attach(MIMEText(body, "plain", "utf-8"))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(
                SENDER_EMAIL,
                RECEIVER_EMAIL,
                msg.as_string()
            )

        return redirect(url_for("hello", success=1, _anchor="contact"))

    except Exception as e:
        print(f"Email error: {e}")
        return "Failed to send email", 500
    
    


if __name__ == "__main__":
    app.run()