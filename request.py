import hashlib
import requests
import util

from bs4 import BeautifulSoup

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

teaching_num = {
    61: '为学楼',
    62: '厚德楼',
}

class_time = {
    1: '第1节 08:00 08:45',
    2: '第2节 08:50 09:35',
    3: '第3节 09:50 10:35',
    4: '第4节 10:40 11:25',
    5: '第5节 11:30 12:15',
    6: '第6节 14:00 14:45',
    7: '第7节 14:50 15:35',
    8: '第8节 15:50 16:35',
    9: '第9节 16:40 17:25',
    10: '第10节 18:30 19:15',
    11: '第11节 19:20 20:05',
    12: '第12节 20:10 20:55',
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
            src, dst = 'captcha.jpg', 'captcha_p.png'
            response = self.session.get(captcha_url)
            file = open(src, 'wb')
            file.write(response.content)
            file.close()
            res = util.captcha_code(src, dst)
            print('captcha:', res)
            if res is not None:
                return res

    def login(self):
        if self.times > 0:
            post_data = {
                'j_username': self.username,
                'j_password': hashlib.md5(bytes(self.password, encoding='utf-8')).hexdigest(),
                'j_captcha': self.captcha(),
            }
            self.session.post(post_url, post_data, headers=self.headers)
            response = self.session.get(index_url, headers=self.headers, cookies=self.session.cookies)
            soup = BeautifulSoup(response.text, 'lxml')
            name = soup.find('title').string
            if name == 'URP综合教务系统首页':
                print('login success.')
            else:
                print('\033[93m' + 'login failed, retrying.' + '\033[0m')
                self.times -= 1
                self.login()
        else:
            print('login failed, please retry later.')

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
        sets = []
        for i in range(len(data)):
            val = data[i]['classroomName']
            sets.append(val)
        return sets

    def search_today(self):
        campus_code = 3             # 校区代码
        tea_codes = [61, 62]        # 教学楼代码列表
        week_num = util.get_weekday()    # 周数
        results = []                # 结果集
        for tea_code in tea_codes:
            classrooms = []
            for i in range(1, 13):
                section = str(week_num) + '/' + str(i)  # 节数
                param = {
                    'weeks': util.get_week_num(),
                    'jslxdm': '',
                    'codeCampusListNumber': campus_code,
                    'teaNum': tea_code,
                    'wSection': section,
                    'pageNum': 1,
                    'pageSize': 100,
                }
                ret = self.search_free_classroom(param)
                classroom = {
                    'time': class_time.get(i),
                    'rooms': ", ".join(ret),
                }
                classrooms.append(classroom)
            results.append({
                'tea': teaching_num.get(tea_code),
                'classrooms': classrooms,
            })
        return results
