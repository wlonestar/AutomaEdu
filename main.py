import util
import config
import request


# run in command line
# python main.py -u <username> -p <password>
if __name__ == '__main__':
    username, password = config.parse_params()
    print('parse params: username: {}, password: {}'.format(username, password))
    day = config.get_config()
    print('get search day: {}'.format(day))
    request = request.Request(username, password)
    request.login()
    print('start searching {} \'s free classrooms...'.format(day))
    if day == 'today':
        ret = request.search_today()
    elif day == 'tomorrow':
        ret = request.search_tomorrow()
    print('search done')
    param = {
        'results': ret,
        'daytime': util.get_format_date()
    }
    print('start writing into file...')
    config.write2html(param)

