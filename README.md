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

执行命令

```shell
python main.py -u <username> -p <password>
```

## 部署

Fork 本项目，启用 GitHub Actions，添加下列仓库密钥：

- `HHU_USERNAME`: URP 教务系统用户名
- `HHU_PASSWORD`: URP 教务系统密码
- `MAIL_USERNAME`: 邮箱服务发件邮箱
- `MAIL_PASSWORD`: 邮箱服务发件邮箱授权密码
- `EMAIL`: 收件邮箱

## 用到的 Python 库

- [requests](https://pypi.org/project/requests/)
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)
- [ddddocr](https://github.com/sml2h3/ddddocr)
- [Pillow](https://pillow.readthedocs.io/en/stable/)
- [lxml](https://pypi.org/project/lxml/)
- [pytz](https://pypi.org/project/pytz/)
- [jinja2](https://pypi.org/project/Jinja2/)

## 注意事项

1. 本仓库代码仅供学习参考，严禁对学校教务系统进行网络攻击等行为

2. 由于不确定学校是否会对教务登录接口进行更改，所以该仓库具有时效性

3. 爬虫小白作品，欢迎批评指正

## 赞助我

如果您觉得这个项目还不错的话，可以请作者喝杯咖啡 🤩

![](https://mypic-1305118058.cos.ap-hongkong.myqcloud.com/img/money.jpg)