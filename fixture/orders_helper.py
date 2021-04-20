

class OrdersHelper:

    def __init__(self, app):
        self.app = app                                                                                                   #self.app.wd - если нужен метод из другого класса, то вызываем его так

    def cart(self, amt, head, itemId, amount, deferred):
        payload = []
        for i in range(amt):
            n = {"itemId": itemId[i], "amount": amount[i], "deferred": deferred[i]}
            payload.append(n)
        body = {"items": payload}
        return self.app._s.put(self.app.host + '/Cart', json=body, headers=head)

    def order(self, email, needEmail, needCall, customName, mnogoRuCardId, head):
        body = {"email": f'{email}', "needEmail": needEmail, "needCall": needCall, "customName": f'{customName}',
                "mnogoRuCardId": mnogoRuCardId}
        return self.app._s.put(self.app.host + '/Order', json=body, headers=head)


