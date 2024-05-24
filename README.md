### First Steps

Create `.env` file with these environment variables
- CELERY_BROKER_URL
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- DB_USER
- DB_PASSWORD
- DB_ADDRESS
- DB_NAME
- DB_PORT
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