import csv
from django.utils import timezone
from .models import Task

def generate_task_report():
    report_filename = f'task_report_{timezone.now().strftime("%Y%m%d_%H%M%S")}.csv'
    with open(report_filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['id', 'title', 'description', 'status', 'priority', 'created_at', 'due_date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for task in Task.objects.all():
            writer.writerow({
                'id': task.id,
                'title': task.title,
                'description': task.description,
                'status': task.status,
                'priority': task.priority,
                'created_at': task.created_at,
                'due_date': task.due_date,
            })

    return report_filename