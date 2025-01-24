# encoding: utf-8

import datetime
from email import encoders
from email.mime.base import MIMEBase
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from main import merge_html_reports

PROJECT = 'ZEUSSDK_AUTOUI_TEST_REPORT'

MAIL_SERVER = 'smtpdm.aliyun.com'
MAIL_PORT = '80'
MAIL_USER = 'jenkins@mailsender.topjoy.com'
MAIL_PASS = 'V946EypyqAGcLaQH'

MAIL_CC_LIST = ['jiaheqi@topjoy.com', 'yangguang@topjoy.com', 'zhengwei@topjoy.com', 'chenzhongyou@topjoy.com',
                'wangyue@topjoy.com']
MAIL_RECEIVER_LIST = ['jiaheqi@topjoy.com']
MAIL_SENDER = 'jenkins@mailsender.topjoy.com'


def send_mail():
    subject = "ZEUSSDK_AUTOUI_TEST_REPORT"
    report_file = './report/uiauto_report_android.html'
    with open(report_file, 'rb') as f:
        mail_body = f.read()
    # 定义邮件内容
    msg = MIMEMultipart()
    body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    msg['Subject'] = subject
    msg['from'] = MAIL_SENDER
    msg['to'] = ','.join(MAIL_RECEIVER_LIST)
    msg['Cc'] = ','.join(MAIL_CC_LIST)
    msg.attach(body)
    # 添加附件
    att = MIMEText(open(report_file, 'rb').read(), 'base64', 'utf-8')
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename= "ZeusSDKUIAuto_report.html"'
    msg.attach(att)

    mail = Mail(MAIL_SERVER, MAIL_PORT, MAIL_USER, MAIL_PASS)
    mail.send(MAIL_RECEIVER_LIST, MAIL_CC_LIST, subject, msg.as_string())


def send_mail_multi():
    # 要合并的两个报告文件
    files = ['./report/uiauto_report_android.html', './report/uiauto_report_ios.html']
    # 合并后的输出文件
    report_file = './report/uiauto_report_merged.html'
    # 合并报告
    merge_html_reports(files, report_file)
    subject = "ZEUSSDK_AUTOUI_TEST_REPORT"
    with open(report_file, 'rb') as f:
        mail_body = f.read()
    # 定义邮件内容
    msg = MIMEMultipart()
    body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    msg['Subject'] = subject
    msg['from'] = MAIL_SENDER
    msg['to'] = ','.join(MAIL_RECEIVER_LIST)
    msg['Cc'] = ','.join(MAIL_CC_LIST)
    msg.attach(body)
    for file in files:
        with open(file, 'rb') as f:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(f.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename="{file}"')
            msg.attach(part)
    mail = Mail(MAIL_SERVER, MAIL_PORT, MAIL_USER, MAIL_PASS)
    mail.send(MAIL_RECEIVER_LIST, MAIL_CC_LIST, subject, msg.as_string())


class Mail(object):
    def __init__(self, smtp_server, smtp_port, username, password):
        self.smtp = SMTP(smtp_server, int(smtp_port))
        self.smtp.ehlo()
        self.smtp.starttls()
        self.smtp.ehlo()
        self.smtp.login(username, password)
        self.sender = MAIL_SENDER

    def __del__(self):
        self.smtp.close()

    def send(self, receiver_list, cc_list, subject, content):
        receiver_list.extend(cc_list)
        self.smtp.sendmail(self.sender, receiver_list, content)
        self.smtp.quit()


if __name__ == "__main__":
    send_mail("ZeusSDK", MAIL_RECEIVER_LIST, MAIL_CC_LIST)
