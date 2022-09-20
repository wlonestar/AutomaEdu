import argparse
import codecs
import glob
import os
import util

from jinja2 import Environment, FileSystemLoader
from request import Request

TEMPLATE_FILE = glob.glob('template/mail.j2')[0]
HTML_FILE = 'template/result.html'


# write string to html using template
# params: map
# template_file: jinja2 template
# filename: html file
def write2html(params, template_file=TEMPLATE_FILE, html_file=HTML_FILE):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    env = Environment(loader=FileSystemLoader(current_directory))
    res = env.get_template(template_file).render(params)
    test = codecs.open(html_file, 'w', 'utf-8')
    test.write(res)
    test.close()


# read parameters from arguments
# -u or --username: username
# -p or --password: password
def parse_params():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", dest="username")
    parser.add_argument("-p", "--password", dest="password")
    args = parser.parse_args()
    return args.__getattribute__('username'), args.__getattribute__('password')


# run in command line
# python main.py -u <username> -p <password>
if __name__ == '__main__':
    USERNAME, PASSWORD = parse_params()
    request = Request(USERNAME, PASSWORD)
    print('username:', USERNAME, '\npassword:', PASSWORD)
    request.login()
    print('start searching today\'s free classrooms...')
    ret = request.search_today()
    print('search done')
    param = {
        'results': ret,
        'daytime': util.get_format_date()
    }
    print('start writing template file...')
    write2html(param)
    print('success. result in', HTML_FILE)
