#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 ubuntu <ubuntu@txOS>
#
# Distributed under terms of the MIT license.

"""

"""
import pymysql


class DbOperate(object):
    def __init__(self):
        db = pymysql.connect(host='mysql', 
                port=3306,
                user='root',
                password='123456',
                db='webapp',
                charset='utf8')
