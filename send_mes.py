import smtplib
from email.message import EmailMessage
from celery import Celery

app = Celery('celery_app', broker='amqp://guest:guest@localhost//',
             backend="db+sqlite://result.sqlite3")
@app.task
def send_email(to_email, subject, body):
    my_email = "milasuhobrus@yandex.ru"
    my_password = "dzzjkddthkmostyt"

    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = my_email
    msg["To"] = to_email

    try:
        print("Отправка")
        with smtplib.SMTP("smtp.yandex.ru", 587) as server:
            server.starttls()
            server.login(my_email, my_password)
            server.send_message(msg)
    except Exception as e:
        print(f"Не получилось {e}")
send_email(
    to_email="gagileveu@mail.ru",
    subject="Сухобрус М",
    body="67"
)