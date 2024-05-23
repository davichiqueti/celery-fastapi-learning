
Running Worker
``` bash
celery -A app.celery worker -P gevent -Q scraping-queue
```

Running Fast API application
``` bash
uvicorn app:app --host 127.0.0.1 --port 8000
```

After run, can use the Fast API swagger to test endpoints. URL: http://127.0.0.1:8000/docs

**/offers/add_offers/** Endpoints uses a post body like this

``` json
{
   "offers":[
        "http://example.com",
        ...
   ]
}
```