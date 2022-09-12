# 河海大学教务系统自动登录脚本

## 关于这个项目

学校教务系统的登录有效期很短，一天之内想多次访问教务必须每次输验证码，很麻烦。

加之线下上课，没课的时候想查询空闲教室需要登录教务查询，比较繁琐。

通过一天半左右的时间慢慢摸索，本人终于能自动登录教务并爬取空闲教室相关信息了。

## 使用

克隆这个项目

```
git clone https://github.com/wlonestar/HHU_URP_auto_login.git
```

修改 `main.py` 中的用户名和密码字段

![](https://mypic-1305118058.cos.ap-hongkong.myqcloud.com/img/Snipaste_2022-09-12_14-54-49.png)

将上面两行改成自己的学号和密码即可

然后直接运行 `main.py` 即可

## 用到的 Python 库

- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)

- [ddddocr](https://github.com/sml2h3/ddddocr)

- [Js2Py](https://pypi.org/project/Js2Py/)

## 注意事项

1. 本仓库代码仅供学习参考，严禁对学校教务系统进行网络攻击等行为

2. 由于不确定学校是否会对教务登录接口进行更改，所以该仓库具有时效性

3. 爬虫小白作品，欢迎批评指正
