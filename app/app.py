import sys
import os
import flask

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
from classes.http_request import HttpRequest

app = flask.Flask(__name__)
app.config.from_object('config')


@app.route('/', methods=['GET'])
def home():
    return "<h1>This is vmware test project.</h1><p>Please navigate to /metrics.</p>"


@app.route('/metrics', methods=['GET'])
def get_metric():
    prometheus_metric = {
        "httpstat_url_up_metric": [],
        "httpstat_url_response_time_ms_metric": []
    }
    print('----- Starting the test -----')

    url_1 = 'https://httpstat.us/503'
    url_1_up = 0
    print(f'---Running test for {url_1}')
    response = HttpRequest.make_get_request(url_1)

    print(f"   Response Code = {response['status_code']}")
    print(f"   Response Text = {response['text']}")
    print(f"   Response Time = {response['response_time']}ms")
    print(f'   -- Preparing prometheus metric --')

    if response['text'] == '503 Service Unavailable' and response['status_code'] == 503:
        url_1_up = 1

    prometheus_metric['httpstat_url_up_metric'].append({url_1: url_1_up})
    prometheus_metric['httpstat_url_response_time_ms_metric'].append({url_1: response['response_time']})

    url_2 = 'https://httpstat.us/200'
    url_2_up = 0
    print(f'---Running test for {url_2}')
    response = HttpRequest.make_get_request(url_2)

    print(f"   Response Code = {response['status_code']}")
    print(f"   Response Text = {response['text']}")
    print(f"   Response Time = {response['response_time']}ms")
    print(f'   -- Preparing prometheus metric --')

    if response['text'] == '200 OK' and response['status_code'] == 200:
        url_2_up = 1

    prometheus_metric['httpstat_url_up_metric'].append({url_2: url_2_up})
    prometheus_metric['httpstat_url_response_time_ms_metric'].append({url_2: response['response_time']})

    print(prometheus_metric)
    return prometheus_metric


@app.errorhandler(400)
def invalid_route(e):
    return flask.Response('Some Error Occurred')


@app.errorhandler(404)
def invalid_route(e):
    return flask.Response('Invalid Route')


@app.errorhandler(500)
def invalid_route(e):
    return flask.Response('Some Error Occurred')

app.run()
