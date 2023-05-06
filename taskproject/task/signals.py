from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Task, Subscription
from .tasks import send_notifications


@receiver(post_save, sender=Subscription)
def subscription_created(sender, instance, created, **kwargs):
    if created:
        task = instance.task

        subscribers = Subscription.objects.filter(task=task).select_related('user')
        print(f"Subscribers for task {task}: {subscribers}")

        task_dict = {
            'id': task.id,
            'title': task.title,
        }
        subscribers_list = [
            {
                'id': subscriber.id,
                'user': {
                    'id': subscriber.user.id,
                    'username': subscriber.user.username,
                },
                'task': task_dict,
            }
            for subscriber in subscribers
        ]
        send_notifications.delay(subscribers_list, task_dict)