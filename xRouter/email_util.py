#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/23 下午10:58
# @Author  : zhuhao
# @Project : helloPython
# @File    : email_util.py
# @Contact : hyzhuhao891407@163.com 
# @Software : PyCharm
# @Desc: email帮助类

import os
import smtplib
from email.mime.multipart import MIMEMultipart, MIMEBase
from email.mime.text import MIMEText
from email.header import Header
from email import encoders


class EmailUtil:

    def __init__(self, subject=None, dispatcher=None, tos=None, ccs=None, contents=None, attachments=None,
                 email_host=None, username=None, password=None):
        """
        构造函数
        :param subject: 邮件主题
        :param dispatcher: 发送者
        :param tos: 接收者
        :param ccs: 抄送者
        :param contents: 邮件正文内容
        :param attachments: 附件
        :param email_host: 发送邮件服务器
        :param username: 用户名
        :param password: 密码
        """
        self._subject = subject
        self._contents = contents
        self._dispatcher = dispatcher
        self._tos = tos if tos is not None else []
        self._ccs = ccs if ccs is not None else []
        self._attachments = attachments if attachments is not None else []
        self._email_host = email_host
        self._user = username
        self._password = password

    def send_email(self):
        """
        发送邮件
        :return: 发送成功返回True，失败返回False
        """
        if self._dispatcher is None:
            print('the email sender is None,cancel sending.')
            return
        if self._email_host is None:
            print('the email host is None,cancel sending.')
            return
        if self._user is None or self._password is None:
            print('the mail user name or password is None,cancel sending.')
            return
        # 构造邮件
        msg = MIMEMultipart()
        msg['From'] = self._dispatcher
        msg['To'] = ','.join(self._tos)  # 超送
        if len(self._ccs) > 0:
            msg['cc'] = ','.join(self._ccs)
        msg['Subject'] = Header(self._subject, 'utf-8').encode()
        # plain 代表纯文本，邮件内容
        msg.attach(MIMEText(self._contents, 'plain', 'utf-8'))
        # 构造附件
        if len(self._attachments) > 0:
            # print('加载附件')
            for attach_file in self._attachments:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(open(attach_file, 'rb').read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', 'attachment;filename="%s"' % os.path.basename(attach_file))
                msg.attach(part)
        try:
            smtp = smtplib.SMTP()
            smtp.connect(self._email_host)
            smtp.login(self._user, self._password)
            smtp.sendmail(self._dispatcher, self._tos, msg.as_string())
            smtp.quit()
            return True
        except smtplib.SMTPException as e:
            print(e)
            return False
