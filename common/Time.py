#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime


class Time(object):
    def __init__(self, startRunningTime):
        self.startRunningTime = startRunningTime

    def get_current_time(self):
        return datetime.datetime.now()

    def get_current_bar_time(self):
        # TODO：to implement the accurate get_current_bar_time function
        return self.get_current_time()

    def get_start_time(self):
        # TODO：to implement the accurate get_start_time function
        return self.startRunningTime

    def get_start_bar_time(self):
        # TODO：to implement the accurate get_start_bar_time function
        return self.get_start_time()
© 2018 GitHub, Inc.