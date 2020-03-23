#!/usr/bin/env python
# coding=utf-8

import sys
import json
from urllib import parse

from requests import Session

session = Session()

def get_lesson_urls(lesson_key):
    lesson_info_url = "https://www.eeo.cn/saasajax/webcast.ajax.php?action=getLessonLiveInfo"
    headers = { 'User-Agent':'MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'}
    data = {
        'lessonKey': lesson_key
    }
    try:
        resp = session.post(url=lesson_info_url, headers=headers, data=data)
        lesson_urls = resp.json()['data']['lessonData']['vodList']
        return lesson_urls
    except:
        print('Error')


def get_urls(url):
    lessonKey = parse.parse_qs(parse.urlparse(url).query).get('lessonKey', [])[0]
    lesson_info_url = "https://www.eeo.cn/saasajax/webcast.ajax.php?action=getLessonLiveInfo"
    headers = { 'User-Agent':'MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'}
    if len(lessonKey) == 0:
        return "Get key Error!"
    else:
        data = {
        'lessonKey': lessonKey
        }
    try:
        resp = session.post(url=lesson_info_url, headers=headers, data=data)
        lesson_urls = resp.json()['data']['lessonData']['vodList']
        return lesson_urls
    except:
        return {'info': 'Try again later!'}





if __name__ == '__main__':
    lesson_key = sys.argv[1]
    urls = get_lesson_urls(lesson_key)
    for url in urls.values():
        print(url)
