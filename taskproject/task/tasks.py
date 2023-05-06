from django.core.mail import send_mail
from .models import Task
from celery import shared_task

@shared_task
def generate_task_report_task():
    from .report import generate_task_report
    report_filename = generate_task_report()
    print(f'Отчет сгенерирован: {report_filename}')


@shared_task
def send_notifications(subscribers, task):
    print(f"Subscribers: {subscribers}")
    for subscriber in subscribers:
        user = subscriber['user']
        notification = f"Уведомление для {subscriber['user']['username']}: Задача '{task['title']}' была обновлена. Проверьте!"
        print(notification)