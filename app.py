import fastapi
import fastapi.encoders
import pydantic
from celery_app.celery_scrape import create_celery
from tasks.scrape_offer import scrape_offer
import csv
from typing import List, Dict


app = fastapi.FastAPI()
app.celery_app = create_celery()
celery = app.celery_app

@app.get("/offers")
def read_offers():
    with open("offers.csv", "r") as file:
        reader = csv.reader(file)
        data = []
        next(reader)
        for line in reader:
            data.append({'offer_link': line[0], 'title': line[1]})
    response_json = {'total_offers': (reader.line_num - 1), 'message': 'sucess', 'data': data}
    return response_json

@app.post('/offers/add_offers/v2')
def add_offers(data: Dict):
    for offer_link in data['offers']:
        scrape_offer.apply_async(args=[offer_link], queue='scraping-queue')
    response_json = {'message': "Sucess. The offer will be processed soon"}
    return response_json

@app.post('/offers/add_offers/v1')
def add_offers(data: Dict):
    for offer_link in data['offers']:
        scrape_offer(offer_link)
    response_json = {'message': "Sucess. Offers processed"}
    return response_json