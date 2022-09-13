import logging
import os.path
import random
from time import sleep

import ddddocr
import requests
from PIL import Image

url = 'http://jwxs.hhu.edu.cn/img/captcha.jpg'
total = 10

origin_prefix = './__captcha/'
processed_prefix = './__captcha_processed/'


def captcha_data(pic_id):
    res = requests.get(url)
    file = open(origin_prefix + 'captcha_' + str(pic_id) + '.jpg', 'wb')
    file.write(res.content)
    file.close()
    logging.debug('download picture', pic_id)


def process_data(pic_id, src, dst):
    img = Image.open(src)
    w, h = img.size
    for x in range(w):
        for y in range(h):
            r, g, b = img.getpixel((x, y))
            low = 50
            up = 256
            if r == 0 and g == 0 and b == 0:
                img.putpixel((x, y), (255, 255, 255))
            if r in range(low) and g in range(low) and b in range(low):
                img.putpixel((x, y), (255, 255, 255))
            if r in range(low, up) and g in range(low, up) and b in range(low, up):
                img.putpixel((x, y), (255, 255, 255))
    img.save(dst)
    logging.debug('picture ', pic_id, 'finished')


def captcha_code(src, dst):
    process_data(0, src, dst)
    ocr = ddddocr.DdddOcr(show_ad=False)
    with open(dst, 'rb') as f:
        img_bytes = f.read()
    res = ocr.classification(img_bytes)
    if len(res) == 4:
        print('captcha:', res)
        return res


def captcha_dataset():
    for i in range(total):
        captcha_data(i)
        rand = random.uniform(1.0, 1.5)
        sleep(rand)
    print('all ', total, ' downloaded')


def process_dataset():
    for i in range(total):
        src = origin_prefix + 'captcha_' + str(i) + '.jpg'
        dst = processed_prefix + 'captcha_p_' + str(i) + '.png'
        process_data(i, src, dst)
    print("all pictures process finished!")


def recognize_compare():
    ocr = ddddocr.DdddOcr(show_ad=False)
    origin_count = 0
    for i in range(total):
        path = origin_prefix + 'captcha_' + str(i) + '.jpg'
        with open(path, 'rb') as f:
            img_bytes = f.read()
        res = ocr.classification(img_bytes)
        if len(res) != 4:
            origin_count += 1
    print('origin error: ', origin_count, ' ', origin_count / total, '%')
    process_count = 0
    for i in range(total):
        path = processed_prefix + 'captcha_p_' + str(i) + '.png'
        with open(path, 'rb') as f:
            img_bytes = f.read()
        res = ocr.classification(img_bytes)
        if len(res) != 4:
            print('id: ', i, ' result: ', res)
            process_count += 1
    print('processed error: ', process_count, ' ', process_count / total, '%')


if __name__ == "__main__":
    if not os.path.exists(origin_prefix):
        os.makedirs(origin_prefix)
        print(origin_prefix, 'created')
    else:
        print(origin_prefix, 'existed')
    if not os.path.exists(processed_prefix):
        os.makedirs(processed_prefix)
        print(processed_prefix, 'created')
    else:
        print(processed_prefix, 'existed')
    captcha_dataset()
    process_dataset()
    recognize_compare()
