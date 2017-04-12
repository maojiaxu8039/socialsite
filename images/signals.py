#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/12 21:41
# @Author  : maojx
# @Site    : 
# @File    : signals.py
# @Software: PyCharm
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Image


@receiver(m2m_changed, sender=Image.users_like.through)
def users_like_changed(sender, instance, **kwargs):
    instance.total_likes = instance.users_like.count()
    instance.save()
