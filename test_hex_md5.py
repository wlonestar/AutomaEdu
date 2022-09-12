import js2py
from md5 import *

if __name__ == "__main__":
    js2py.translate_file('md5.js', 'md5.py')
    data = md5.hex_md5('12ibnsdkq1ed')
    print(data)
