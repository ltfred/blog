
# 为 celery 使用 django 配置文件进行设置
import os
if not os.getenv('DJANGO_SETTINGS_MODULE'):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'my_blog.settings'

from celery import Celery

# 创建celery实例
celery_app = Celery('blog')

# 给celery添加配置
celery_app.config_from_object('celery_tasks.config')

# 让 celery_app 自动捕获目标地址下的任务
celery_app.autodiscover_tasks(['celery_tasks.email'])