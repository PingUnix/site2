from django.db import models
from design import *

# Create your models here.


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(
        'design.Person',
        through='Membership',       ## 自定义中间表
        through_fields=('group', 'person'),
    )

    def __str__(self):
        return self.name


class Membership(models.Model):  # 这就是具体的中间表模型
    group = models.ForeignKey('Group', on_delete=models.CASCADE)
    person = models.ForeignKey('design.Person', on_delete=models.CASCADE)
    inviter = models.ForeignKey(
        'design.Person',
        on_delete=models.CASCADE,
        related_name="membership_invites",
    )
    invite_reason = models.CharField(max_length=64)

    def __str__(self):
        return self.group.name


