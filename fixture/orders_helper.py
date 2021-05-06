from random import randint, choice
from model import parameters
from json import loads


class OrdersHelper:

    def __init__(self, app):
        self.app = app                                                                                                   #self.app.wd - если нужен метод из другого класса, то вызываем его так

# Корзина

    def generate_payload(self, cnt, deferred=False):
        dataset = []
        for i in range(cnt):
            dataset.append(
                {'itemId': parameters.items.pop(randint(0, len(parameters.items) - 1)),
                 'amount': randint(1, 99),
                 'deferred': deferred
                 })
        return dataset

    def dataset_min_sum(self, head):
        dataset = []
        payload = {'itemId': '5d65077f2fd44a0001b12715', 'amount': 1, 'deferred': False}
        dataset.append(payload)
        body = {"items": dataset}
        return self.app._s.put(self.app.host + '/Cart', json=body, headers=head)

    def cart(self, head, dataset, userId=None):  #метод для SU и User
        body = {"items": dataset, "userId": userId}
        return self.app._s.put(self.app.host + '/Cart', json=body, headers=head)

    def cart_use_vitamins(self, head, vitaminsCount, userId=None):  #метод для SU и User
        body = {"vitaminsCount": vitaminsCount, "userId": userId}
        return self.app._s.put(self.app.host + '/Cart/UseVitamins', json=body, headers=head)

    def cart_with_deferred_items(self, head, items):
        body = {"items": items}
        return self.app._s.put(self.app.host + '/Cart', json=body, headers=head)

    def get_cart_user(self, head, userId=None):
        parameters = {"userId": userId}
        return self.app._s.get(self.app.host + '/Cart', params=parameters, headers=head)

    def cart_use_promocode(self, head, promoCode, userId=None):
        body = {"promoCode": promoCode, "userId": userId}
        return self.app._s.put(self.app.host + '/Cart/PromoCode', json=body, headers=head)

    def delete_promocode_from_the_cart(self, head, promoCode, userId=None):
        params = {"promoCode": promoCode, "userId": userId}
        return self.app._s.delete(self.app.host + '/Cart/PromoCode', params=params)

# Заказ

    def create_order(self, email, needEmail, needCall, mnogoRuCardId, head, userId=None):  #метод для SU и User
        body = {"email": f'{email}', "needEmail": needEmail, "needCall": needCall,
                "mnogoRuCardId": mnogoRuCardId, "userId": userId}
        return self.app._s.put(self.app.host + '/Order', json=body, headers=head)

    def delete_order(self, orderId, head):
        query_params = {'orderId': orderId}
        return self.app._s.delete(self.app.host + '/Order', params=query_params, headers=head)

    def list_of_orders(self, head, page=0, size=50):
        query_params = {"page": page, "size": size}
        return self.app._s.get(self.app.host + '/Order/List', params=query_params, headers=head)

    def id_order_from_list(self, head):
        list_of_orders = loads(self.list_of_orders(head, page=0, size=100).text)
        orderId = choice(list_of_orders['data'])['id']
        return orderId

    def repeat_order(self, head, orderId, userId=None):  #метод для SU и User
        body = {"orderId": orderId, 'userId': userId}
        return self.app._s.put(self.app.host + '/Order/Repeat', json=body, headers=head)

# Для SU (оригинальные методы)

    def list_of_orders_su(self, head, page=0, pagesize=100):
        payload = {"page": page, "pagesize": pagesize}
        return self.app._s.get(self.app.host + '/SuperUser/Orders', params=payload, headers=head)

    def id_order_for_su(self, head):
        list_of_orders = loads(self.list_of_orders_su(head, page=0, pagesize=30).text)
        orderId = choice(list_of_orders['data'])['id']
        return orderId

    def order_block_su(self, head, orderId):
        body = {"orderId": orderId}
        return self.app._s.put(self.app.host + '/SuperUser/OrderBlock', json=body, headers=head)

    def edit_order_su(self, head, orderId, dataset, dryRun):
        body = {"orderId": orderId, "items": dataset, "dryRun": dryRun}
        return self.app._s.post(self.app.host + '/SuperUser/EditOrder', json=body, headers=head)

    def delete_order_su(self, orderId, head):
        query_params = {'orderId': orderId}
        return self.app._s.delete(self.app.host + '/SuperUser/Order', params=query_params, headers=head)

    def operation_with_vitamins(self, userId, head, value, updatingType= None):
        body = {"userId": userId, "updatingType": updatingType, "value": value}
        return self.app._s.put(self.app.host + '/SuperUser/UserVitaminsBalance', json=body, headers=head)
