import requests


class HttpRequest:
    @staticmethod
    def make_get_request(url):
        try:
            res = requests.get(url, timeout=20)
            return {'status_code': res.status_code, 'text': res.text, 'response_time': (res.elapsed.microseconds / 1000)}
        except Exception as ex:
            raise Exception(f'Error while requesting the URL {url}. Error: {ex}')