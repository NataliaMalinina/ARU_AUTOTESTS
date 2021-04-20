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
        print(dataset)
        return dataset

    def cart(self, head, dataset):
        body = {"items": dataset}
        return self.app._s.put(self.app.host + '/Cart', json=body, headers=head)

    def order(self, email, needEmail, needCall, customName, mnogoRuCardId, head):
        body = {"email": f'{email}', "needEmail": needEmail, "needCall": needCall, "customName": f'{customName}',
                "mnogoRuCardId": mnogoRuCardId}
        return self.app._s.put(self.app.host + '/Order', json=body, headers=head)


