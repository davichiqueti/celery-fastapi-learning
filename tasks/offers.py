from celery_app.celery_scrape import create_celery
from database import execute_query
from sqlalchemy import text


celery = create_celery()


@celery.task(ignore_result=True)
def delete_offers():
    query = "DELETE FROM hooklab_monitoring.offers WHERE store_id = 0"
    execute_query(query)
    print('Deleted offers with store_id "0"')

def select_offers():
    query = "SELECT offer_link, title FROM hooklab_monitoring.offers WHERE store_id = 0"
    result = execute_query(query)
    return result.fetchall()
