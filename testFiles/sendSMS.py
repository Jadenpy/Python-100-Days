# -*- coding: utf-8 -*-
# @Author: Jaden Hu
# @Date:   2023-06-28 13:20:20
# @Last Modified by:   Jaden Hu
# @Last Modified time: 2023-06-28 13:28:50


import urllib.parse
import http.client
import json


def main():
    host  = "106.ihuyi.com"
    sms_send_uri = "/webservice/sms.php?method=Submit"
    # 下面的参数需要填入自己注册的账号和对应的密码
    params = urllib.parse.urlencode({'account': '20213287', 'password' : '15950817790i', 'content': '您的验证码是：147258。请不要把验证码泄露给其他人。', 'mobile': '15950817790', 'format':'json' })
    print(params)
    headers = {'Content-type': 'application/x-www-form-urlencoded', 'Accept': 'text/plain'}
    conn = http.client.HTTPConnection(host, port=80, timeout=30)
    conn.request('POST', sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    jsonstr = response_str.decode('utf-8')
    print(json.loads(jsonstr))
    conn.close()


if __name__ == '__main__':
    main()

