import fastapi
import fastapi.encoders
from tasks.scrape_offer import scrape_offer
from tasks.offers import delete_offers, select_offers
import csv
from typing import List, Dict


app = fastapi.FastAPI()


@app.get("/offers")
def read_offers():
    data = select_offers()
    data = [{'offer_link': row[0], 'title': row[1]} for row in data]
    response_json = {'total_offers': len(data), 'message': 'sucess', 'data': data}
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
