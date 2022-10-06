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
    if day == 'today':
        daytime = util.get_utc8_today_format()
    elif day == 'tomorrow':
        daytime = util.get_utc8_tomorrow_format()
    param = {
        'results': ret,
        'daytime': daytime,
    }
    print('start writing into file...')
    config.write2html(param)

