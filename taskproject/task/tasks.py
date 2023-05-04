from django.core.mail import send_mail
from .models import Task
from celery import shared_task


from celery import shared_task
from .report import generate_task_report

@shared_task
def generate_task_report_task():
    report_filename = generate_task_report()
    print(f'Отчет сгенерирован: {report_filename}')