import pytz
import ddddocr

from PIL import Image
from datetime import datetime, timedelta


def get_utc8_today():
    return datetime.now(pytz.timezone('Asia/Shanghai'))


def get_utc8_tomorrow():
    return datetime.now(pytz.timezone('Asia/Shanghai')) + timedelta(days=1)


# only for 2022-2023 1
def get_week_num(d=datetime.now(pytz.timezone('Asia/Shanghai'))):
    return d.isocalendar().week - 34


# mon -> 1, ect..
def get_weekday(d=datetime.now(pytz.timezone('Asia/Shanghai'))):
    return datetime.weekday(d) + 1


def get_format_date(d=datetime.now(pytz.timezone('Asia/Shanghai'))):
    return d.strftime('%Y年%m月%d日')


def process_data(src, dst):
    img = Image.open(src)
    w, h = img.size
    for x in range(w):
        for y in range(h):
            r, g, b = img.getpixel((x, y))
            low, up = 50, 256
            if r == 0 and g == 0 and b == 0:
                img.putpixel((x, y), (255, 255, 255))
            if r in range(low) and g in range(low) and b in range(low):
                img.putpixel((x, y), (255, 255, 255))
            if r in range(low, up) and g in range(low, up) and b in range(low, up):
                img.putpixel((x, y), (255, 255, 255))
    img.save(dst)


def captcha_code(src, dst):
    print('start image processing...')
    process_data(src, dst)
    print('image processing is complete.')
    ocr = ddddocr.DdddOcr(show_ad=False)
    with open(dst, 'rb') as f:
        img_bytes = f.read()
    res = ocr.classification(img_bytes)
    if len(res) == 4:
        return res
