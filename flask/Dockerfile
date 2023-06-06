FROM python:3

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD gunicorn --bind 0.0.0.0:5000 fetch_gpt_usage:app

#app1  == filename
#app referes to app instance in app = Flask(__name__)