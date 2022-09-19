import argparse
import logging

from request import Request


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
    request.search_aweek(4)
