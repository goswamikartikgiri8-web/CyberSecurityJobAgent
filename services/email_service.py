import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
from dotenv import load_dotenv

load_dotenv()


class EmailService:

    def send(self, jobs):

        sender = os.getenv("EMAIL_USER")
        password = os.getenv("EMAIL_PASS")
        receiver = os.getenv("EMAIL_TO")

        msg = MIMEMultipart("alternative")

        msg["From"] = sender
        msg["To"] = receiver
        msg["Subject"] = f"Cyber Security Jobs ({len(jobs)})"
        msg["Date"] = formatdate(localtime=True)

        html = f"""
        <html>
        <body style="font-family:Arial">

        <h2>🚀 Cyber Security Daily Report</h2>

        <p>Total New Jobs : <b>{len(jobs)}</b></p>

        <hr>
        """

        for job in jobs:

            html += f"""
            <div style="border:1px solid #ddd;
                        border-radius:10px;
                        padding:15px;
                        margin-bottom:20px;">

                <h3>{job.title}</h3>

                <p><b>Company :</b> {job.company}</p>
                <p><b>Location :</b> {job.location}</p>
                <p><b>Experience :</b> {job.experience}</p>
                <p><b>Salary :</b> {job.salary}</p>
                <p><b>Source :</b> {job.source}</p>

                <a href="{job.apply_link}">
                    Apply Here
                </a>

            </div>
            """

        html += """
        </body>
        </html>
        """

        msg.attach(MIMEText(html, "html"))

        print(f"Sender    : {sender}")
        print(f"Receiver  : {receiver}")

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        server.login(sender, password)

        response = server.sendmail(
            sender,
            [receiver],
            msg.as_string()
        )

        print("SMTP Response :", response)

        server.quit()

        print("✅ Email Sent Successfully")