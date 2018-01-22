import json

from utils.base import BaseVKClient


class VKClientGetID(BaseVKClient):
    method = 'users.get'
    http_method = 'GET'

    def __init__(self, user_ids):
        self.user_ids = user_ids

    def response_handler(self, response):
        loaded = json.loads(response.content)
        users = loaded['response']
        return [user['uid'] for user in users]

    def _get_data(self, method, http_method):
        request_provider = self._request_mapper.get(http_method)

        if request_provider is None or self.user_ids is None:
            return None

        url = self.generate_url(method)
        payload = {'user_ids': ','.join(self.user_ids)}
        response = request_provider(url, params=payload)

        return self.response_handler(response)


class VKClientGetFriends(BaseVKClient):
    method = 'friends.get'
    http_method = 'GET'

    def __init__(self, user_id):
        self.user_id = user_id

    def response_handler(self, response):
        loaded = json.loads(response.content)
        users = loaded['response']
        return users

    def _get_data(self, method, http_method):
        request_provider = self._request_mapper.get(http_method)

        if request_provider is None or self.user_id is None:
            return None

        url = self.generate_url(method)
        payload = {'user_id': self.user_id, 'fields': 'bdate'}
        response = request_provider(url, params=payload)

        return self.response_handler(response)
