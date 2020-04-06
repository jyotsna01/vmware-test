import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
from classes.http_request import HttpRequest


class TestHttpRequest(unittest.TestCase):

    url = 'https://httpstat.us/200'

    def test_make_get_request_keys(self):
        response = HttpRequest.make_get_request(TestHttpRequest.url)
        self.assertTrue('status_code' in response.keys())
        self.assertTrue('text' in response.keys())
        self.assertTrue('response_time' in response.keys())

    def test_make_get_request_value(self):
        response = HttpRequest.make_get_request(TestHttpRequest.url)
        self.assertEqual(200, response['status_code'])


if __name__ == '__main__':
    unittest.main()
