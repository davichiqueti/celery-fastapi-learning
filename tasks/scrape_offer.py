from celery_app.celery_scrape import create_celery
from bs4 import BeautifulSoup
import requests
import time
from database import execute_query


celery = create_celery()


@celery.task(ignore_result=True)
def scrape_offer(offer_link: str):
    response = requests.get(offer_link)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = get_title(soup)
    # Updating result
    query = f"""
        INSERT INTO hooklab_monitoring.offers (store_id, variation, offer_link, title)
        VALUES (
        0,
        'Unique',
        '{offer_link}',
        '{title}'
        )
        ON CONFLICT ON CONSTRAINT offers_un
        DO UPDATE SET
            title = '{title}'
    """.strip()
    execute_query(query)
    print(f'Updated offer "{offer_link}"')
    print(f'Scraped title "{title}"')
    time.sleep(5)

def get_title(soup: BeautifulSoup):
    return soup.title.text
