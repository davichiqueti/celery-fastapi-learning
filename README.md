### First Steps

Create `.env` file with these environment variables
- CELERY_BROKER_URL="sqs://sqs.us-east-1.amazonaws.com/400182930435/celery_study"
- AWS_ACCESS_KEY_ID="AKIAV2LGC5QBT6LT7CO5"
- AWS_SECRET_ACCESS_KEY="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"

### Running App

``` bash
docker-compose up --build
```

After run, can use the Fast API swagger to test endpoints. URL: http://localhost:8000/docs

**/offers/add_offers/** Endpoints uses a post body like this

``` json
{
   "offers":[
        "http://example.com",
        ...
   ]
}
```