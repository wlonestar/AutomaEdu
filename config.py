import os
import glob
import yaml
import codecs
import argparse

from jinja2 import Environment, FileSystemLoader

config_file = 'config.yaml'
template_file = glob.glob('template/template.j2')[0]
html_file = 'template/result.html'


# read parameters from arguments
# -u or --username: username
# -p or --password: password
def parse_params():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", dest="username")
    parser.add_argument("-p", "--password", dest="password")
    args = parser.parse_args()
    return args.__getattribute__('username'), args.__getattribute__('password')


# read config from yaml file
# day: today or tomorrow
def get_config():
    with open(config_file, 'r') as f:
        _day = yaml.safe_load(f)
    return _day.get('day')


# write string to html using template
# params: map
# template_file: jinja2 template
# filename: html file
def write2html(_params, _template_file=template_file, _html_file=html_file):
    print('write contents into file: {}, using template file: {}'.format(_html_file, _template_file))
    current_directory = os.path.dirname(os.path.abspath(__file__))
    env = Environment(loader=FileSystemLoader(current_directory))
    res = env.get_template(_template_file).render(_params)
    fd = codecs.open(_html_file, 'w', 'utf-8')
    fd.write(res)
    fd.close()
    print('success. result in {}'.format(_html_file))
