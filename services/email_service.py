import os
import csv
import smtplib
import tempfile

from email import encoders
from email.mime.base import MIMEBase
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

        msg = MIMEMultipart()

        msg["From"] = sender
        msg["To"] = receiver
        msg["Subject"] = f"🛡 Cyber Security Jobs ({len(jobs)})"
        msg["Date"] = formatdate(localtime=True)

        html = f"""
<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

<style>

body {{
    margin:0;
    padding:30px;
    background:#f2f4f8;
    font-family:Arial, Helvetica, sans-serif;
}}

.container {{
    max-width:900px;
    margin:auto;
}}

.header {{
    background:#0d6efd;
    color:white;
    text-align:center;
    padding:25px;
    border-radius:12px;
}}

.summary {{
    background:white;
    margin-top:20px;
    padding:18px;
    border-radius:10px;
    font-size:18px;
    box-shadow:0 2px 8px rgba(0,0,0,.08);
}}

.job {{
    background:white;
    margin-top:20px;
    padding:20px;
    border-radius:10px;
    border-left:6px solid #0d6efd;
    box-shadow:0 2px 8px rgba(0,0,0,.08);
}}

.job h2 {{
    margin-top:0;
    color:#0d6efd;
}}

.apply-btn {{
    display:inline-block;
    margin-top:15px;
    background:#198754;
    color:white !important;
    padding:10px 18px;
    text-decoration:none;
    border-radius:6px;
    font-weight:bold;
}}

.footer {{
    text-align:center;
    color:#666;
    margin-top:35px;
    font-size:14px;
}}

</style>

</head>

<body>

<div class="container">

<div class="header">

<h1>🛡 Cyber Security Job Agent</h1>

<p>Daily Cyber Security Job Report</p>

</div>

<div class="summary">

<b>Total New Jobs :</b> {len(jobs)}

</div>
"""

        for job in jobs:

            html += f"""
<div class="job">

<h2>{job.title}</h2>

<p><b>🏢 Company :</b> {job.company}</p>

<p><b>📍 Location :</b> {job.location}</p>

<p><b>💼 Experience :</b> {job.experience}</p>

<p><b>💰 Salary :</b> {job.salary}</p>

<p><b>🌐 Source :</b> {job.source}</p>

<a class="apply-btn" href="{job.apply_link}">
🚀 Apply Now
</a>

</div>
"""

        html += """
<div class="footer">

<hr>

<p><b>Cyber Security Job Agent</b></p>

<p>Generated Automatically using GitHub Actions</p>

</div>

</div>

</body>

</html>
"""

        msg.attach(MIMEText(html, "html"))

        # ==================================================
        # Create CSV Attachment
        # ==================================================

        csv_file = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".csv",
            mode="w",
            newline="",
            encoding="utf-8"
        )

        writer = csv.writer(csv_file)

        writer.writerow([
            "Company",
            "Job Title",
            "Location",
            "Experience",
            "Salary",
            "Source",
            "Apply Link"
        ])

        for job in jobs:

            writer.writerow([
                job.company,
                job.title,
                job.location,
                job.experience,
                job.salary,
                job.source,
                job.apply_link
            ])

        csv_file.close()

        attachment = MIMEBase(
            "application",
            "octet-stream"
        )

        with open(csv_file.name, "rb") as f:
            attachment.set_payload(f.read())

        encoders.encode_base64(attachment)

        attachment.add_header(
            "Content-Disposition",
            'attachment; filename="CyberSecurityJobs.csv"'
        )

        msg.attach(attachment)

        # ==================================================
        # Send Email
        # ==================================================

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