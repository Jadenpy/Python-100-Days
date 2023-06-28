# -*- coding: utf-8 -*-
# @Author: Jaden Hu
# @Date:   2023-06-28 13:32:40
# @Last Modified by:   Jaden Hu
# @Last Modified time: 2023-06-28 13:57:59


#python3
#接口类型：互亿无线触发短信接口，支持发送验证码短信、订单通知短信等。
#账户注册：请通过该地址开通账户https://user.ihuyi.com/new/register.html
#注意事项：
#（1）调试期间，请用默认的模板进行测试，默认模板详见接口文档；
#（2）请使用 用户名 及 APIkey来调用接口，APIkey在会员中心可以获取；
#（3）该代码仅供接入互亿无线短信接口参考使用，客户可根据实际需要自行编写；

import urllib.parse
import urllib.request

#接口地址
url = 'http://106.ihuyi.com/webservice/sms.php?method=Submit'

#定义请求的数据
values = {
    'account':'C24964889',                              #账户密码并不等同网站的账户密码
    'password':'739066a43d70ce4e172a3105b88fcd09',
    'mobile':'15950817790',
    'content':'line1 welder 维修呼叫',
    'format':'json',
}

#将数据进行编码
data = urllib.parse.urlencode(values).encode(encoding='UTF8')

#发起请求
req = urllib.request.Request(url, data)
response = urllib.request.urlopen(req)
res = response.read()

#打印结果
print(res.decode("utf8"))
