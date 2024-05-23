from celery_app.celery_scrape import create_celery
from bs4 import BeautifulSoup
import requests
import csv
import re
import biip
import time


celery = create_celery()


@celery.task(ignore_result=True)
def scrape_offer(offer_link: str):
    response = requests.get(offer_link)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = get_title(soup)
    time.sleep(5)
    with open('offers.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([offer_link, title])
    print(offer_link)
    print(title)

def get_title(soup: BeautifulSoup):
    return soup.title.text
