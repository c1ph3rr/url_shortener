# Django URL Shortener

A simple URL shortener based on base62 encoding with API support.

### How to run the project
1) Clone this repository
2) Navigate to the main project directory and install the python dependencies with `pip install -r requirements.txt`
3) Run `python manage.py runserver` to start the development server and browse to `http://127.0.0.1:8000`

### How to consume API
#### Request
URL `http://127.0.0.1:8000/api/` <br>
Method `POST` <br>
Body <br>
```json
{
  "url": "long_url"
}
```
#### Response
```json
{
  "url": "long_url",
  "hash": "hash",
  "short_url": "short_url"
}
```

### Demo app running on Heroku
https://short---ly.herokuapp.com/
