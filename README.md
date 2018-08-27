# HERE test task StringsAPI
It's a simple app wrote for fun which implements a below task.


## How to run
Create a vertualenv and install packages:
```
pipenv install -r requirements.txt
```

Then run the app:
```
flask run
```

### Run with a Docker
Biuld a container
```
docker build -t flask-sample-one:latest .
```

Run the Docker Container
```
docker run -d -p 5000:5000 flask-sample-one
```


Open a browser on address http://127.0.0.1:5000/

## API endpoints

### Random word
This endpoint returns a random word fetched from external source.
```
http://127.0.0.1:5000/random
```

Success Response 200 OK
```
{
    status: "success",
    word: "test"
}
```

#### cURL request example
```
curl -i -H "Content-Type: application/json" -XGET "http://127.0.0.1:5000/random"
```

### Wikipedia article
This endpoint returns a text from Wikipedia for given word.
```
http://127.0.0.1:5000/wikipedia/kiss
```

+ Success Response 200 OK
```
{
    status: "success",
    content: "<Text is about kiss...>"
}
```

#### cURL request example
```
curl -i -H "Content-Type: application/json" -XGET "http://127.0.0.1:5000/wikipedia/kiss"
```

### Statistics
This endpoint returns a statistic of most popular randomly selected words, where N is an integer of limits.

```
http://127.0.0.1:5000/stats/N
```

+ Success Response 200 OK
```
{
    "status": "success",
    "stats": {
        "test": 2,
        "kiss": 1,
        "love": 1
    }
}
```

### cURL request example
```
curl -i -H "Content-Type: application/json" -XGET "http://127.0.0.1:5000/stats/3"
```


### Joke
This endpoint returns a random joke fetched from icndb.com

```
http://127.0.0.1:5000/joke?firstName=<string>&lastName=<string>
```
all request params are optional.

+ Success Response 200 OK
```
{
    "status": "success",
    "content": "Chuck Norris cannot love, he can only not kill."
}
```

### cURL request example
```
curl -i -H "Content-Type: application/json" -XGET "http://127.0.0.1:5000/joke"

curl -i -H "Content-Type: application/json" -XGET "http://127.0.0.1:5000/joke?firstName=Alex&lastName=Golt"
```

# Tests
For running tests just run a command
```
python tests.py
```
