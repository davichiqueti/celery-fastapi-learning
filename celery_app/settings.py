from kombu import Queue
from dotenv import load_dotenv
import os


load_dotenv()
broker_url = os.getenv('CELERY_BROKER_URL')
result_backend = None
broker_transport = "sqs"
task_default_queue = 'default'
concurrency = 8
task_queues = (
    Queue("scraping-queue"),
)
task_routes = {
    'tasks.scrape_offer': {'queue': 'scraping-queue'},
}
inlude: list = ['tasks']
