import unittest

from app import app


class TestService(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_server_is_up_and_running(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_metrics_endpoint(self):
        result = self.app.get('/metrics')
        self.assertEqual(result.status_code, 200)


if __name__ == '__main__':
    unittest.main()
