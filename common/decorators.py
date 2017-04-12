#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/11 20:16
# @Author  : maojx
# @Site    : 
# @File    : decorators.py
# @Software: PyCharm
from django.http import HttpResponseBadRequest


def ajax_required(f):
    def wrap(request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest()
        return f(request, *args, **kwargs)

    wrap.__doc__ = f.__doc__
    wrap.__name__ = f.__name__
    return wrap
