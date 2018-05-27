import os
import scraper
from flask import Flask, render_template
app = Flask(__name__)


links = [
'https://www.twilio.com/marketing/bundles/company-brand/img/logos/red/twilio-logo-red.png',
'https://upload.wikimedia.org/wikipedia/commons/6/69/Airbnb_Logo_B%C3%A9lo.svg',
'https://upload.wikimedia.org/wikipedia/commons/a/a0/Yext-logo.svg'
]

twilio_jobs = scraper.twilio_jobs()
airbnb_jobs = scraper.airbnb_jobs()


@app.route('/')
def index():
    return render_template('index.html', links=links)

@app.route('/twilio')
def twilio(name=None):
    return render_template('show.html', data=twilio_jobs, link=links[0])

@app.route('/airbnb')
def airbnb(name=None):
    return render_template('show.html', data=airbnb_jobs, link=links[1])

@app.route('/yext')
def yext(name=None):
    data="" #No time for Yext
    return render_template('show.html', data=data, link=links[2])



if __name__ == '__main__':
    app.run()
