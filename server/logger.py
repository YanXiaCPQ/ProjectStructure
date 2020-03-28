#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

# 建立记录器,可以建立多个，其他文件需要哪个就导入哪个. 看logger.ini
worklog = logging.getLogger('get_worklog')
translog = logging.getLogger('get_translog')
sqllog = logging.getLogger('get_sqllog')
