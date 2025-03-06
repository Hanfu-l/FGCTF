from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.
#题目模型
class Topic(models.Model):
    #题目名称
    name = models.CharField(max_length=30,unique=True)
    #题目分数
    score=models.IntegerField(default=0)
    #镜像名称
    DockerName=models.CharField(max_length=255)
    #转发到容器的端口
    DockerPort=models.CharField(max_length=255)
    #描述
    Description=models.CharField(max_length=255)
    #是否显示
    Visable=models.BooleanField(default=False)
    #flag填入
    Keyvalue=models.CharField(max_length=255,default="123")



#拓展用户字段分数
class Score(models.Model):
    #确保用户与Score模型唯一
    Score_by = models.OneToOneField(User, related_name='UserScore',on_delete=models.CASCADE)
    score=models.IntegerField(default=0)
    SubmitTopics=models.ManyToManyField(Topic, related_name='UserSubmitTopic')

    # 更新 Score 的总分
    def update_score(self):
        # 获取所有绑定的 SubmitTopics 中的 score 字段并计算总和
        total_score = self.SubmitTopics.aggregate(total_score=models.Sum('score'))['total_score'] or 0
        self.score = total_score
        self.save()

    # 获取当前 Score 对应的所有 Topic 的总分
    def get_total_score(self):
        return self.SubmitTopics.aggregate(total_score=models.Sum('score'))['total_score'] or 0

    # 检查是否已经绑定相同的 Topic
    def is_topic_already_bound(self, topic):
        return self.SubmitTopics.filter(id=topic.id).exists()

    # 添加一个新的 Topic 并更新 Score 分数
    def add_topic(self, topic):
        if not self.is_topic_already_bound(topic):
            self.SubmitTopics.add(topic)
            self.update_score()  # 更新总分





#用户关于docker的信息
class UserDockerData(models.Model):
    #指向User
    DockerUser = models.ForeignKey(User, related_name='docker_data', on_delete=models.CASCADE)
    #最大启动镜像数量，默认为1
    MaxDockerNumber=models.IntegerField(default=1)
    #当前启动镜像数量
    RunDockerNumber=models.IntegerField(default=0)
    #当前启动的镜像名称
    RunDockerId=models.CharField(max_length=255)
    #当前启动镜像的题目ID
    RunDockerTopicId=models.IntegerField(default=-1)
    