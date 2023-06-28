# -*- coding: utf-8 -*-
# @Author: Jaden Hu
# @Date:   2023-06-28 12:42:57
# @Last Modified by:   Jaden Hu
# @Last Modified time: 2023-06-28 13:07:24
# -*- coding: utf-8 -*-
# @Author: Jaden Hu
# @Date:   2023-06-28 12:42:57
# @Last Modified by:   Jaden Hu
# @Last Modified time: 2023-06-28 12:43:00


from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText


def main():
    # 请自行修改下面的邮件发送者和接收者
    sender = 'huxinsheng2008@163.com'
    receivers = ['62620612@qq.com', 'jaden.hu@kautex.com']
    message = MIMEText('用Python发送邮件的示例代码,来自jaden.', 'plain', 'utf-8')
    message['From'] = Header('张三', 'utf-8')
    message['To'] = Header('胡新生', 'utf-8')
    message['Subject'] = Header('示例代码实验邮件', 'utf-8')
   # smtper = SMTP('smtp.126.com')
    smtper = SMTP('smtp.163.com')     #smtp.163.com
    # 请自行修改下面的登录口令
    smtper.login(sender, 'TZBLAHFKHXYUUGBS')
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成!')


if __name__ == '__main__':
    main()