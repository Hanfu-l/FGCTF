# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from topic.models import Score  # 导入你的模型

@receiver(post_save, sender=User)
def create_user_score(sender, instance, created, **kwargs):
    if created:
        # 检查用户是否已经有 Score 实例
        if not hasattr(instance, 'UserScore'):
            Score.objects.create(Score_by=instance)