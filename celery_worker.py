from celery_app.celery_scrape import create_celery
from tasks import scrape_offer


celery = create_celery()
