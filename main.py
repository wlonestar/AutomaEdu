import argparse
import logging
import codecs
import glob
import os.path
from jinja2 import Environment, FileSystemLoader

import timeofday
from request import Request

current_directory = os.path.dirname(os.path.abspath(__file__))
env = Environment(loader=FileSystemLoader(current_directory))
template = glob.glob('template/mail.j2')[0]
file = 'template/result.html'


# write string to html using template
# params: map
# template_file: jinja2 template
# filename: html file
def write2html(params, template_file, filename):
    res = env.get_template(template_file).render(params)
    test = codecs.open(filename, 'w', 'utf-8')
    test.write(res)
    test.close()
    print('success, result in template/result.html')


# read parameters from arguments
# -u or --username: username
# -p or --password: password
def config():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", dest="username")
    parser.add_argument("-p", "--password", dest="password")
    args = parser.parse_args()
    return args.__getattribute__('username'), args.__getattribute__('password')


# run in command line
# python main.py -u <username> -p <password>
if __name__ == "__main__":
    USERNAME, PASSWORD = config()
    logging.debug(USERNAME, PASSWORD)
    request = Request(USERNAME, PASSWORD)
    request.login()
    ret = request.search_today()
    param = {
        'results': ret,
        'daytime': timeofday.get_format_date()
    }
    write2html(param, template, file)
