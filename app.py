# from flask import Flask
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello():
#     return "Hello World!"
#
# @app.route('/<name>')
# def hello_name(name):
#     return "Hello {}!".format(name)
#
#
#
#
# if __name__ == '__main__':
#     app.run()

import os
import scraper
from flask import Flask, render_template
app = Flask(__name__)#, instance_relative_config=True)
# app.config.from_mapping(
#     SECRET_KEY='dev',
#     DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
# )
#
# if test_config is None:
#     # load the instance config, if it exists, when not testing
#     app.config.from_pyfile('config.py', silent=True)
# else:
#     # load the test config if passed in
#     app.config.from_mapping(test_config)
#
# # ensure the instance folder exists
# try:
#     os.makedirs(app.instance_path)
# except OSError:
#     pass

# twilio = scraper.twilio_jobs()
airbnb = scraper.airbnb_jobs()

temp = [ ['Software Engineer, Android', 'San Francisco, California '], ['Software Engineer, Android (China)', 'Beijing, China'], ['Software Engineer (Back-end)', 'Beijing, China'], ['Software Engineer, Booking Experience', 'San Francisco, California '], ['Software Engineer, Build Infrastructure ', 'Seattle, Washington & San Francisco, CA'], ['Software Engineer, Business Travel', 'San Francisco, California '], ['Software Engineer, China Infrastructure (SF)', 'San Francisco, California '], ['Software Engineer, Cities', 'San Francisco, California'], ['Software Engineer, Data Platform ', 'San Francisco, California'], ['Software Engineer, Data Security', 'San Francisco, California '], ['Software Engineer, Developer Infrastructure', 'San Francisco, California '], ['Software Engineer, Experiences', 'San Francisco, California '], ['Software Engineer, Frontend', 'San Francisco, California '], ['Software Engineer(Front-end)', 'Beijing, China'], ['Software Engineer, Full Stack', 'San Francisco, California'], ['Software Engineer, Full Stack (Portland)', 'Portland, Oregon'], ['Software Engineer, Growth', 'San Francisco, California '], ['Software Engineer, Homes Infrastructure', 'San Francisco, California '], ['Software Engineer, Human Team', 'San Francisco, California'], ['Software Engineer, Infrastructure', 'San Francisco, California '], ['Software Engineer, iOS', 'San Francisco, California '], ['Software Engineer, iOS (China)', 'Beijing, China'], ['Software Engineer, Lux', 'San Francisco, California '], ['Software Engineer, Machine Learning', 'San Francisco, California '], ['Software Engineer, Native Infrastructure', 'San Francisco, California '], ['Software Engineer, Notifications Infrastructure', 'San Francisco, California '], ['Software Engineer, Payments', 'San Francisco, California & Seattle, Washington'], ['Software Engineer, Pricing', 'San Francisco, California '], ['Software Engineer, Pricing Optimization ', 'San Francisco, California '], ['Software Engineer, Search', 'San Francisco, California'], ['Software Engineer, Search Relevance', 'San Francisco, California '], ['Software Engineer (Seattle)', 'Seattle, Washington'], ['Software Engineer, Site Reliability', 'San Francisco, California '], ['Software Engineer, Trips', 'San Francisco, California '], ['Software Engineer, Trust', 'San Francisco, California'], ['Software Engineer, Web Accessibility', 'San Francisco, California '], ['Technical Program Manager, Data Quality', 'San Francisco, California '], ['Technical Program Manager - Payments', 'San Francisco, California '], ['Data Science Manager - Analytics, China', 'Beijing, China'], ['Data Science Manager - Analytics, Lux', 'San Francisco, California '], ['Data Science Manager - Analytics, Trips', 'San Francisco, California '], ['Data Science Manager, Payments', 'San Francisco, California '], ['Data Science Manager, Trips Platform', 'San Francisco, California '], [' Data Scientist - Algorithms ', 'San Francisco, California '], [' Data Scientist - Algorithms, China ', 'Beijing, China'], ['Data Scientist - Algorithms, Pricing ', 'San Francisco, California '], ['Data Scientist - Algorithms, Risk (China)', 'San Francisco, California '], ['Data Scientist - Analytics', 'San Francisco, California '], ['Data Scientist - Analytics, China', 'Beijing, China'], ['Data Scientist - Analytics, Payments', 'San Francisco, California '], ['Data Scientist - Analytics, Policy (APAC)', 'Singapore, Singapore'], ['Data Scientist - Analytics, Product Quality', 'San Francisco, California '], ['Data Scientist - Analytics, Pro Host', 'San Francisco, California '], ['Data Scientist - Analytics, Risk ', 'San Francisco, California '], ['Data Scientist - Inference', 'San Francisco, California '], ['Data Scientist - Inference', 'Beijing, China'], ['Data Scientist - Inference, Guest Activation', 'San Francisco, California '], ['Data Scientist - Inference, Host Growth', 'San Francisco, California '], ['Data Scientist - Inference, Pro Host', 'San Francisco, California ']]

links = [
    'https://www.twilio.com/marketing/bundles/company-brand/img/logos/red/twilio-logo-red.png',
    'https://upload.wikimedia.org/wikipedia/commons/6/69/Airbnb_Logo_B%C3%A9lo.svg',
    'https://upload.wikimedia.org/wikipedia/commons/a/a0/Yext-logo.svg'
]

@app.route('/')
def index():
    return render_template('index.html', links=links)


@app.route('/twilio')
def twilio(name=None):
    # data = scraper.twilio_jobs()
    return render_template('show.html', data=twilio, link=links[0])

@app.route('/airbnb')
def airbnb(name=None):
    # data = scraper.airbnb_jobs()
    return render_template('show.html', data=temp, link=links[1])

@app.route('/yext')
def yext(name=None):
    # data = scraper.yext()
    data=""
    return render_template('show.html', data=data, link=links[2])



if __name__ == '__main__':
    app.run()
