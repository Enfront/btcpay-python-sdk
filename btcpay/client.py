import json
import requests

from urllib.parse import urlencode
from requests.exceptions import HTTPError


class BTCPayClient:
    def __init__(self):
        from btcpay import api_key, host_url, store_id

        self.api_key = api_key
        self.host_url = host_url
        self.store_id = store_id

        self.session = requests.Session()
        self.session.verify = True
        
        self.session.headers.update(
            {
                'Authorization': 'token ' + self.api_key,
                'Content-Type': 'application/json',
                'accept': 'application/json',
                'X-accept-version': '2.0.0'
            }
        )

    def _check_response_status(self, request):
        http_error_message = None

        if not request.ok:
            if 400 <= request.status_code < 500:
                http_error_message = u'%s Client Error: %s for url: %s | body: %s' % (
                    request.status_code,
                    request.reason,
                    request.url,
                    request.text
                )
            elif 500 <= request.status_code < 600:
                http_error_message = u'%s Server Error: %s for url: %s | body: %s' % (
                    request.status_code,
                    request.reason,
                    request.url,
                    request.text
                )

            if http_error_message:
                raise HTTPError(http_error_message, response=request)

    def _return_data(self, request):
        try:
            data = request.json()
        except ValueError:
            data = None

        return data

    def _get_request(self, path, params=None):
        uri = self.host_url + 'api/v1' + path
        params = params or dict()

        request = self.session.get(uri, params=params)
        self._check_response_status(request)

        return self._return_data(request)

    def _post_request(self, path, payload):
        uri = self.host_url + 'api/v1' + path
        payload = json.dumps(payload)
        
        request = self.session.post(uri, data=payload)
        self._check_response_status(request)

        return self._return_data(request)

    def _put_request(self, path, payload):
        uri = self.host_url + 'api/v1' + path
        payload = json.dumps(payload)

        request = self.session.put(uri, payload)
        self._check_response_status(request)

        return self._return_data(request)

    def _delete_request(self, path, params=None):
        uri = self.host_url + 'api/v1' + path
        params = params or dict()

        request = self.session.delete(uri, params=params)
        self._check_response_status(request)

        return self._return_data(request)
