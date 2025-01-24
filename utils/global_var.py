from utils.generates import *

email_pre = None
email_number = None
phone_number = None


def generate_email_pre():
    global email_pre
    email_pre = generate_random_email_prefix()


def generate_email_number():
    global email_number
    email_number = generate_random_email()


def generate_phone_number():
    global phone_number
    phone_number = generate_random_phone_number()
