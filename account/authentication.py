#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/10 20:06
# @Author  : maojx
# @Site    : 
# @File    : authentication.py
# @Software: PyCharm
from django.contrib.auth.models import User


class EmailAuthBackend(object):
    def authenticate(self, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
