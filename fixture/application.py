import requests.api


class Application:

    _s = requests.session()
    host = None

    def __init__(self, host):
        self.host = host

    def auth(self, phone, code):
        data = {"type": "BySms", "code": f'{code}', "phone": f'{phone}', "timeZone": 0, "referalId": None}
        return self._s.post(self.host + '/Auth/Auth', json=data)

    def auth_admin_user(self):
        data = {"userName": "MNS", "password": "Prokhorova23"}
        return self._s.post(self.host + '/AdminUser/Auth', json=data).text

    def search_random(self, page, pagesize, phrase, sort, cityid, withprice, withprofit, withpromoVits):
        payload = {"page": f'{page}', "pagesize": f'{pagesize}', "phrase": f'{phrase}',
                   "sort": f'{sort}', "cityid": f'{cityid}', "withprice": f'{withprice}',
                   "withprofit": f'{withprofit}', "withpromoVits": f'{withpromoVits}'}
        return self._s.get(self.host + '/Search/ByPhrase', params=payload)

    def search(self, phrase, sort, cityid, withprice, withprofit, withpromoVits):
        payload = {"phrase": f'{phrase}', "sort": f'{sort}', "cityid": f'{cityid}', "withprice": f'{withprice}',
                   "withprofit": f'{withprofit}', "withpromoVits": f'{withpromoVits}'}
        return self._s.get(self.host + '/Search/ByPhrase', params=payload)

    def search_with_tags(self, phrase, tags, sort, cityid, withprice, withprofit, withpromoVits):
        payload = {"phrase": f'{phrase}', "tags": f'{tags}', "sort": f'{sort}', "cityid": f'{cityid}',
                   "withprice": f'{withprice}', "withprofit": f'{withprofit}', "withpromoVits": f'{withpromoVits}'}
        return self._s.get(self.host + '/Search/ByPhrase', params=payload)

    def choice_city(self, id, manualChange):
        data = {"id": id, "manualChange": manualChange}
        return self._s.put(self.host + '/City/UserCity', json=data)

    def choice_city_admin(self, id, manualChange, userid, head):
        data = {"id": f'{id}', "manualChange": manualChange, "userId": userid}
        return self._s.put(self.host + '/City/UserCity', json=data, headers=head)

    # def choice_autodest(self, host):
