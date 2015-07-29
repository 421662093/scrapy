# coding:utf-8
import json
import time
import random


def stamp2time(stamp, _type='%Y-%m-%d %H:%M:%S'):  # 将时间戳转化为时间
        # time.gmtime(_time)
    return time.strftime(_type, time.localtime(stamp+28800))


def time2stamp(_time, _type='%Y-%m-%d %H:%M:%S'):  # 将时间转化为时间戳

    return time.mktime(time.strptime(_time, _type))


def getstamp():  # 获取当前时间戳
    return time.time()


def getrandom(start=1000,end=1000000):
    #生成随机数
    return random.randint(start, end) 

def delrepeat(templist):
    #移除list重复
    new_ids = []
    for item in templist:
        if item not in new_ids and len(item)>0:
            new_ids.append(item)
    return new_ids