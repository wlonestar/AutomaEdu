import hashlib
import logging

import requests
from bs4 import BeautifulSoup

from captcha import captcha_code
from timeofday import *

Host = 'jwxs.hhu.edu.cn'
prefix = 'http://jwxs.hhu.edu.cn/'
UserAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 ' \
            'Safari/537.36 '

login_url = prefix + 'login'
captcha_url = prefix + 'img/captcha.jpg'
post_url = prefix + 'j_spring_security_check'
index_url = prefix + 'index.jsp'
query_url = prefix + 'student/teachingResources/freeClassroomQuery/search'
query_refer_url = prefix + 'student/teachingResources/freeClassroomQuery/custom'


campus_code = {
    '全部': 0,
    '校本部': 1,
    '江宁校区': 2,
    '常州校区': 3,
}

teaching_num = {
    61: '为学楼',
    62: '厚德楼',
}

classtime = {
    1: '第1节 08:00-08:45',
    2: '第2节 08:50-09:35',
    3: '第3节 09:50-10:35',
    4: '第4节 10:40-11:25',
    5: '第5节 11:30-12:15',
    6: '第6节 14:00-14:45',
    7: '第7节 14:50-15:35',
    8: '第8节 15:50-16:35',
    9: '第9节 16:40-17:25',
    10: '第10节 18:30-19:15',
    11: '第11节 19:20-20:05',
    12: '第12节 20:10-20:55',
}


class Request(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.session = requests.Session()
        self.headers = {
            'Host': Host,
            'User-Agent': UserAgent,
            'Referer': login_url,
        }
        self.cookies = self.session.cookies
        self.times = 5

    def captcha(self):
        while True:
            src = 'captcha.jpg'
            dst = 'captcha_p.png'
            response = self.session.get(captcha_url)
            file = open(src, 'wb')
            file.write(response.content)
            file.close()
            res = captcha_code(src, dst)
            if res is not None:
                return res

    def login(self):
        if self.times > 0:
            print('username:', self.username)
            print('password(encoded):', hashlib.md5(bytes(self.password,encoding = 'utf-8')).hexdigest())
            post_data = {
                'j_username': self.username,
                'j_password': hashlib.md5(bytes(self.password,encoding = 'utf-8')).hexdigest(),
                'j_captcha': self.captcha(),
            }

            self.session.post(post_url, post_data, headers=self.headers)
            response = self.session.get(index_url, headers=self.headers, cookies=self.session.cookies)
            soup = BeautifulSoup(response.text, 'lxml')
            name = soup.find('title').string
            if name == 'URP综合教务系统首页':
                print('login success')
                print('JSESSIONID:', self.session.cookies.get('JSESSIONID'))
            else:
                print('login failed, retry')
                self.times -= 1
                self.login()
        else:
            print('login failed, please retry later')

    def search_free_classroom(self, query_param):
        headers = {
            'Host': Host,
            'User-Agent': UserAgent,
            'Referer': query_refer_url,
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        }
        response = self.session.post(query_url, data=query_param, headers=headers, cookies=self.session.cookies)
        data = response.json()[0]['records']
        logging.debug('free classrooms:', '(week', query_param['weeks'], ')', '(section', query_param['wSection'], ')')
        sets = []
        for i in range(len(data)):
            val = data[i]['classroomName']
            sets.append(val)
        logging.debug(sets)
        return sets

    def search_today(self):
        code = 3
        tea_codes = [61, 62]
        week_num = get_weekday()
        results = []
        for tea_code in tea_codes:
            classrooms = []
            for i in range(1, 13):
                section = str(week_num) + '/' + str(i)
                param = {
                    'weeks': get_week_num(),
                    'jslxdm': '',
                    'codeCampusListNumber': code,
                    'teaNum': tea_code,
                    'wSection': section,
                    'pageNum': 1,
                    'pageSize': 100,
                }
                ret = self.search_free_classroom(param)
                classroom = {
                    'time': classtime.get(i),
                    'rooms': ", ".join(ret),
                }
                classrooms.append(classroom)
            results.append({
                'tea': teaching_num.get(tea_code),
                'classrooms': classrooms,
            })
        return results

    def search_aweek(self, week):
        code = campus_code.get('常州校区')
        tea_code = teaching_num.get(61)
        sections = [
            ['1/1', '2/1', '3/1', '4/1', '5/1', '6/1', '7/1'],
            ['1/2', '2/2', '3/2', '4/2', '5/2', '6/2', '7/2'],
            ['1/3', '2/3', '3/3', '4/3', '5/3', '6/3', '7/3'],
            ['1/4', '2/4', '3/4', '4/4', '5/4', '6/4', '7/4'],
            ['1/5', '2/5', '3/5', '4/5', '5/5', '6/5', '7/5'],
            ['1/6', '2/6', '3/6', '4/6', '5/6', '6/6', '7/6'],
            ['1/7', '2/7', '3/7', '4/7', '5/7', '6/7', '7/7'],
            ['1/8', '2/8', '3/8', '4/8', '5/8', '6/8', '7/8'],
            ['1/9', '2/9', '3/9', '4/9', '5/9', '6/9', '7/9'],
            ['1/10', '2/10', '3/10', '4/10', '5/10', '6/10', '7/10'],
            ['1/11', '2/11', '3/11', '4/11', '5/11', '6/11', '7/11'],
            ['1/12', '2/12', '3/12', '4/12', '5/12', '6/12', '7/12'],
        ]
        result_set = []
        for i in range(0, len(sections)):
            new = []
            for j in range(0, len(sections[i]) + 1):
                new.append('')
            result_set.append(new)

        for row in range(0, len(sections)):
            result_set[row][0] = row + 1
            for col in range(0, len(sections[row])):
                param = {
                    'weeks': week,
                    'jslxdm': '',
                    'codeCampusListNumber': code,
                    'teaNum': tea_code,
                    'wSection': sections[row][col],
                    'pageNum': 1,
                    'pageSize': 50,
                }
                ret = self.search_free_classroom(param)
                result_set[row][col + 1] = ','.join(ret)
        return result_set
