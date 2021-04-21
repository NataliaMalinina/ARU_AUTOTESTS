from random import randint
from model import parameters

class OrdersHelper:

    def __init__(self, app):
        self.app = app                                                                                                   #self.app.wd - если нужен метод из другого класса, то вызываем его так

    def generate_payload(self, cnt):
        dataset = []
        for i in range(cnt):
            dataset.append(
                {'itemId': parameters.items.pop(randint(0, len(parameters.items) - 1)),
                 'amount': randint(1, 99),
                 'deferred': False
                 })
        return dataset

    def cart(self, head, dataset):
        body = {"items": dataset}
        return self.app._s.put(self.app.host + '/Cart', json=body, headers=head)

    def cart_su(self, head, dataset, userId=None):
        body = {"items": dataset, "userId": userId}
        return self.app._s.put(self.app.host + '/Cart', json=body, headers=head)

    def order(self, email, needEmail, needCall, mnogoRuCardId, head):
        body = {"email": f'{email}', "needEmail": needEmail, "needCall": needCall,
                "mnogoRuCardId": mnogoRuCardId}
        return self.app._s.put(self.app.host + '/Order', json=body, headers=head)

    def order_su(self, email, needEmail, needCall, mnogoRuCardId, head, userId=None):
        body = {"email": email, "needEmail": needEmail, "needCall": needCall,
                "mnogoRuCardId": mnogoRuCardId, "userId": userId}
        return self.app._s.put(self.app.host + '/Order', json=body, headers=head)

    def dataset_min_sum(self, head):
        dataset = []
        payload = {'itemId': '5d65077f2fd44a0001b12715', 'amount': 1, 'deferred': False}
        dataset.append(payload)
        body = {"items": dataset}
        return self.app._s.put(self.app.host + '/Cart', json=body, headers=head)