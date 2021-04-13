import requests.api
from json import loads


class Application:

    _s = requests.session()
    host = None

    def __init__(self, host):
        self.host = host

# Авторизация

    def auth(self, phone, code):
        data = {"type": "BySms", "code": f'{code}', "phone": f'{phone}', "timeZone": 0, "referalId": None}
        return self._s.post(self.host + '/Auth/Auth', json=data)

    def auth_admin_user(self):
        data = {"userName": "MNS", "password": "Prokhorova23"}
        return self._s.post(self.host + '/AdminUser/Auth', json=data)

# Получение токена

    def token_autorization(self):
        authorization = loads(self.auth(phone='+79139519213', code='9213').text)
        head = {'Authorization': f"Bearer {authorization['token']}"}
        return head

    def token_auth_admin_user(self):
        authorization = loads(self.auth_admin_user().text)
        head = {'Authorization': f"Bearer {authorization['token']}"}
        return head

    def token_shadow_user(self):
        authorization = self.choice_city(id='5e574663f4d315000196b176', manualChange=True).headers
        head = {'Authorization': f"Bearer {authorization['X-Shadowuser']}"}
        return head

# Поиск по фразе

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

# Выбор города

    def choice_city(self, id, manualChange):
        data = {"id": id, "manualChange": manualChange}
        return self._s.put(self.host + '/City/UserCity', json=data)

    def choice_city_admin(self, id, manualChange, userid, head):
        data = {"id": f'{id}', "manualChange": manualChange, "userId": userid}
        return self._s.put(self.host + '/City/UserCity', json=data, headers=head)

    def choice_city_auth_user(self, id, manualChange, head):
        data = {"id": f'{id}', "manualChange": manualChange}
        return self._s.put(self.host + '/City/UserCity', json=data, headers=head)

# Выбор аптеки

    def choice_autodest(self, id):
        data = {"id": f'{id}'}
        return self._s.put(self.host + '/AutoDest/UserAutoDest', json=data)

    def choice_autodest_auth_user(self, id, head):
        data = {"id": f'{id}'}
        return self._s.put(self.host + '/AutoDest/UserAutoDest', json=data, headers=head)

    def choice_autodest_su(self, id, userid, head):
        data = {"id": f'{id}', "userId": f'{userid}'}
        return self._s.put(self.host + '/AutoDest/UserAutoDest', json=data, headers=head)

# Отзыв на аптеку

    def autodest_review(self, head, autoDestId, rating, review, fio, orderNum, customReason, complaints):
        body = {"autoDestId": f'{autoDestId}', "rating": rating, "review": f'{review}', "fio": fio,
                "orderNum": orderNum, "complaints": {"standardReasons": complaints, "customReason": customReason}}
        return self._s.put(self.host + '/AutoDest/Review', json=body, headers=head)

    def edit_autodest_review(self, head, id, rating, review):
        body = {"id": f'{id}', "rating": rating, "review": f'{review}'}
        return self._s.put(self.host + '/AutoDest/EditReview', json=body, headers=head)

    def delete_autodest_review(self, head, reviewId):
        parameters = {"reviewId": reviewId}
        return self._s.delete(self.host + '/AutoDest/Review', params=parameters, headers=head)

