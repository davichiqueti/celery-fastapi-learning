from kombu import Queue
from dotenv import load_dotenv
import os


load_dotenv()


class BaseSettings:
    """Celery Configuration"""
    broker_url = os.getenv('CELERY_BROKER_URL')
    result_backend = None
    broker_transport = "sqs"
    task_default_queue = 'default'
    task_queues = (
        Queue("scraping-queue"),
    )
    task_routes = {
        'tasks.scrape_offer': {'queue': 'scraping-queue'},
    }
    inlude: list = ['tasks']
