from django.core.mail import send_mail
from django.conf import settings
from celery_tasks.main import celery_app


@celery_app.task(bind=True, name='send_reset_email', retry_backoff=3)
def send_reset_mail(self, to_email, password):
    # 标题
    subject = '重置密码邮件'
    # 内容
    html_message = '感谢您使用Fred的个人网站，您的密码重置为:{},请登录后修改密码'.format(password)

    try:
        send_mail(subject, '', settings.EMAIL_FROM, [to_email], html_message=html_message)
    except Exception as e:
        # 有异常自动重试三次
        raise self.retry(exc=e, max_retries=3)
