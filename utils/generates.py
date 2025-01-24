import datetime
import string
import random


def generate_random_email(length=10, domain="example.com"):
    """生成随机邮箱字符串"""
    username = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    email = f"{username}@{domain}"
    return email


def generate_random_email_prefix(length=10):
    """生成随机邮箱前缀"""
    username = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    email_pre = f"{username}"
    return email_pre


def generate_random_phone_number():
    """生成随机手机号"""
    prefix = "1" + str(random.choice([3, 5, 7, 8, 9]))
    body = ''.join(random.choice(string.digits) for _ in range(9))
    phone_number = prefix + body
    return phone_number


if __name__ == '__main__':
    print(generate_random_email())
    # print(datetime.date.)
