# -*- coding:utf-8 -*-

'''
DNSPodSDK
=========
DNSPod API SDK library, written in Python.

Example:
    >>> import AliyunSDK
    >>> rds = AliyunSDK.RDS(access_id, access_secret)
    >>> ret = rds.show_instance_info(db_instance_id)
    >>> print ret
'''

from public import Public
from account import Account

__title__ = 'DNSPodSDK'
__author__ = 'Nanu'
