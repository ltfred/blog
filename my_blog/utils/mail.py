from django.conf import settings
from django.core.mail import send_mail


def send_reset_mail(to_email, password):
    # 标题
    subject = '重置密码邮件'
    # 内容
    html_message = '感谢您使用Fred的个人网站，您的密码重置为:{},请登录后修改密码'.format(password)

    send_mail(subject, '', settings.EMAIL_FROM, [to_email], html_message=html_message)