import requests.api


class Application:

    _s = requests.session()
    host = None

    def __init__(self, host):
        self.host = 'https://api.apteka.tech'

    def auth(self, host, phone, code):
        data = {"type": "BySms", "code": f'{code}', "phone": f'{phone}', "timeZone": 0, "referalId": None}
        return self._s.post(self.host + '/Auth/Auth', json=data)

    def ping(self, host):
        return self._s.get(self.host + '/Auth/Ping')

    def search_random(self, host, page, pagesize, phrase, sort, cityid, withprice, withprofit, withpromoVits):
        payload = {"page": f'{page}', "pagesize": f'{pagesize}', "phrase": f'{phrase}',
                   "sort": f'{sort}', "cityid": f'{cityid}', "withprice": f'{withprice}',
                   "withprofit": f'{withprofit}', "withpromoVits": f'{withpromoVits}'}
        return self._s.get(self.host + '/Search/ByPhrase', params=payload)

    def search(self, host, phrase, sort, cityid, withprice, withprofit, withpromoVits):
        payload = {"phrase": f'{phrase}', "sort": f'{sort}', "cityid": f'{cityid}', "withprice": f'{withprice}',
                   "withprofit": f'{withprofit}', "withpromoVits": f'{withpromoVits}'}
        return self._s.get(self.host + '/Search/ByPhrase', params=payload)

    def search_with_tags(self, host, phrase, tags, sort, cityid, withprice, withprofit, withpromoVits):
        payload = {"phrase": f'{phrase}', "tags": f'{tags}', "sort": f'{sort}', "cityid": f'{cityid}',
                   "withprice": f'{withprice}', "withprofit": f'{withprofit}', "withpromoVits": f'{withpromoVits}'}
        return self._s.get(self.host + '/Search/ByPhrase', params=payload)
