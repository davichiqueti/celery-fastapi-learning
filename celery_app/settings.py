from kombu import Queue
from dotenv import load_dotenv
import os
from celery.schedules import crontab


load_dotenv()
broker_url = os.getenv('CELERY_BROKER_URL')
result_backend = None
broker_transport = "sqs"
task_default_queue = 'default'
worker_concurrency = 4
task_queues = (
    Queue("scraping-queue"),
    Queue("schedules-tasks")
)
task_routes = {
    'tasks.scrape_offer.scrape_offer': {'queue': 'scraping-queue'},
    'tasks.offers.delete_offers': {'queue': 'schedules-tasks'},
}
inlude: list = ['tasks']
beat_schedule = {
    'clear-offers': {
        'task': 'tasks.offers.delete_offers',
        'schedule': 120,
    }
}
schedule = "./celery_app/celerybeat-schedule"
