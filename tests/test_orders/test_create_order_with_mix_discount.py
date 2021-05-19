import pprint
from json import loads
from random import choice
from model import parameters


def test_use_max_of_vitamins_and_max_discount_promocode(app):
    choice_autodest_before_order = app.choice_autodest(id=choice(parameters.autodestid_for_order),
                                                       head=app.token_autorization())
    formatted_json_str = pprint.pformat(choice_autodest_before_order.text)
    print(choice_autodest_before_order.request.body)
    print(choice_autodest_before_order, formatted_json_str, sep='\n\n')
    assert choice_autodest_before_order.status_code == 200

    put_the_item_in_the_cart = app.order_fixture.cart(dataset=app.order_fixture.generate_payload(2),
                                                      head=app.token_autorization())
    formatted_json_str = pprint.pformat(put_the_item_in_the_cart.text)
    print(put_the_item_in_the_cart.request.body)
    print(put_the_item_in_the_cart, formatted_json_str, sep='\n\n')
    while loads(put_the_item_in_the_cart.text)['totalSum'] < 500:
        put_the_item_in_the_cart = app.order_fixture.cart \
            (dataset=app.order_fixture.generate_payload(2), head=app.token_autorization())
        if loads(put_the_item_in_the_cart.text)['totalSum'] >= 500:
            break
    assert "\"tradeName\"" in put_the_item_in_the_cart.text
    assert put_the_item_in_the_cart.status_code == 200

    use_vitamins = app.order_fixture.cart_use_vitamins(vitaminsCount=100,
                                                       head=app.token_autorization())

    assert loads(use_vitamins.text)['vitaminsInfo']["vitaminsUsed"] > 0

    use_promocode = app.order_fixture.cart_use_promocode(promoCode="BPAЧ", head=app.token_autorization())

    formatted_json_str = pprint.pformat(use_promocode.text)
    print(use_promocode.request.body)
    print(use_promocode, formatted_json_str, sep='\n\n')
    assert loads(use_promocode.text)['promoCodes'][0]['isUsed'] == True
    assert use_promocode.status_code == 200

    ordering = app.order_fixture.create_order(email=None, needEmail=False, needCall=False, mnogoRuCardId=None,
                                              head=app.token_autorization())
    formatted_json_str = pprint.pformat(ordering.text)
    print(ordering.request.body)
    print(ordering, formatted_json_str, sep='\n\n')
    assert ordering.status_code == 200
    assert "\"orderId\"" in ordering.text
    assert "\"orderNum\"" in ordering.text
    assert len(loads(ordering.text)['order']['promoCodes']) == 1
    assert loads(ordering.text)['order']["vitaminsUsed"] == 0


def test_use_max_of_vitamins_and_any_promocode(app):
    choice_autodest_before_order = app.choice_autodest(id=choice(parameters.autodestid_for_order),
                                                       head=app.token_autorization())
    formatted_json_str = pprint.pformat(choice_autodest_before_order.text)
    print(choice_autodest_before_order.request.body)
    print(choice_autodest_before_order, formatted_json_str, sep='\n\n')
    assert choice_autodest_before_order.status_code == 200

    put_the_item_in_the_cart = app.order_fixture.cart(dataset=app.order_fixture.generate_payload(2),
                                                      head=app.token_autorization())
    formatted_json_str = pprint.pformat(put_the_item_in_the_cart.text)
    print(put_the_item_in_the_cart.request.body)
    print(put_the_item_in_the_cart, formatted_json_str, sep='\n\n')
    while loads(put_the_item_in_the_cart.text)['totalSum'] < 500:
        put_the_item_in_the_cart = app.order_fixture.cart \
            (dataset=app.order_fixture.generate_payload(2), head=app.token_autorization())
        if loads(put_the_item_in_the_cart.text)['totalSum'] >= 500:
            break
    assert "\"tradeName\"" in put_the_item_in_the_cart.text
    assert put_the_item_in_the_cart.status_code == 200

    use_vitamins = app.order_fixture.cart_use_vitamins(vitaminsCount=100,
                                                       head=app.token_autorization())

    assert loads(use_vitamins.text)['vitaminsInfo']["vitaminsUsed"] > 0

    use_promocode = app.order_fixture.cart_use_promocode(promoCode='RIGA2', head=app.token_autorization())

    formatted_json_str = pprint.pformat(use_promocode.text)
    print(use_promocode.request.body)
    print(use_promocode, formatted_json_str, sep='\n\n')
    assert loads(use_promocode.text)['promoCodes'][0]['isUsed'] == True
    assert use_promocode.status_code == 200

    ordering = app.order_fixture.create_order(email=None, needEmail=False, needCall=False, mnogoRuCardId=None,
                                              head=app.token_autorization())
    formatted_json_str = pprint.pformat(ordering.text)
    print(ordering.request.body)
    print(ordering, formatted_json_str, sep='\n\n')
    assert ordering.status_code == 200
    assert "\"orderId\"" in ordering.text
    assert "\"orderNum\"" in ordering.text
    assert len(loads(ordering.text)['order']['promoCodes']) != 0
    assert loads(ordering.text)['order']["vitaminsUsed"] == 70


def test_use_vitamins_and_promocode_for_max_discount_with_help_of_promocode(app):
    choice_autodest_before_order = app.choice_autodest(id=choice(parameters.autodestid_for_order),
                                                       head=app.token_autorization())
    formatted_json_str = pprint.pformat(choice_autodest_before_order.text)
    print(choice_autodest_before_order.request.body)
    print(choice_autodest_before_order, formatted_json_str, sep='\n\n')
    assert choice_autodest_before_order.status_code == 200

    put_the_item_in_the_cart = app.order_fixture.cart(dataset=app.order_fixture.generate_payload(2),
                                                      head=app.token_autorization())
    formatted_json_str = pprint.pformat(put_the_item_in_the_cart.text)
    print(put_the_item_in_the_cart.request.body)
    print(put_the_item_in_the_cart, formatted_json_str, sep='\n\n')
    while loads(put_the_item_in_the_cart.text)['totalSum'] < 500:
        put_the_item_in_the_cart = app.order_fixture.cart \
            (dataset=app.order_fixture.generate_payload(2), head=app.token_autorization())
        if loads(put_the_item_in_the_cart.text)['totalSum'] >= 500:
            break
    assert "\"tradeName\"" in put_the_item_in_the_cart.text
    assert put_the_item_in_the_cart.status_code == 200

    use_vitamins = app.order_fixture.cart_use_vitamins(vitaminsCount=80,
                                                       head=app.token_autorization())

    assert loads(use_vitamins.text)['vitaminsInfo']["vitaminsUsed"] > 0

    use_promocode = app.order_fixture.cart_use_promocode(promoCode='RIGA2', head=app.token_autorization())

    formatted_json_str = pprint.pformat(use_promocode.text)
    print(use_promocode.request.body)
    print(use_promocode, formatted_json_str, sep='\n\n')
    assert loads(use_promocode.text)['promoCodes'][0]['isUsed'] == True
    assert use_promocode.status_code == 200

    ordering = app.order_fixture.create_order(email=None, needEmail=False, needCall=False, mnogoRuCardId=None,
                                              head=app.token_autorization())
    formatted_json_str = pprint.pformat(ordering.text)
    print(ordering.request.body)
    print(ordering, formatted_json_str, sep='\n\n')
    assert ordering.status_code == 200
    assert "\"orderId\"" in ordering.text
    assert "\"orderNum\"" in ordering.text
    assert len(loads(ordering.text)['order']['promoCodes']) != 0
    assert loads(ordering.text)['order']["vitaminsUsed"] == 70


def test_use_vitamins_and_promocode_for_max_discount_with_help_of_vitamins(app):
    put_the_item_in_the_cart = app.order_fixture.cart(dataset=app.order_fixture.generate_payload(2),
                                                      head=app.token_autorization())
    formatted_json_str = pprint.pformat(put_the_item_in_the_cart.text)
    print(put_the_item_in_the_cart.request.body)
    print(put_the_item_in_the_cart, formatted_json_str, sep='\n\n')
    while loads(put_the_item_in_the_cart.text)['totalSum'] < 500:
        put_the_item_in_the_cart = app.order_fixture.cart \
            (dataset=app.order_fixture.generate_payload(2), head=app.token_autorization())
        if loads(put_the_item_in_the_cart.text)['totalSum'] >= 500:
            break
    assert "\"tradeName\"" in put_the_item_in_the_cart.text
    assert put_the_item_in_the_cart.status_code == 200

    use_promocode = app.order_fixture.cart_use_promocode(promoCode='MAИ', head=app.token_autorization())

    formatted_json_str = pprint.pformat(use_promocode.text)
    print(use_promocode.request.body)
    print(use_promocode, formatted_json_str, sep='\n\n')
    assert loads(use_promocode.text)['promoCodes'][0]['isUsed'] == True
    assert use_promocode.status_code == 200

    use_vitamins = app.order_fixture.cart_use_vitamins(vitaminsCount=70,
                                                       head=app.token_autorization())

    assert loads(use_vitamins.text)['vitaminsInfo']["vitaminsUsed"] > 0

    ordering = app.order_fixture.create_order(email=None, needEmail=False, needCall=False, mnogoRuCardId=None,
                                              head=app.token_autorization())
    formatted_json_str = pprint.pformat(ordering.text)
    print(ordering.request.body)
    print(ordering, formatted_json_str, sep='\n\n')
    assert ordering.status_code == 200
    assert "\"orderId\"" in ordering.text
    assert "\"orderNum\"" in ordering.text
    assert len(loads(ordering.text)['order']['promoCodes']) != 0
    assert loads(ordering.text)['order']["vitaminsUsed"] == 30


def test_use_promocode_and_10_vitaminok(app):
    put_the_item_in_the_cart = app.order_fixture.cart(dataset=app.order_fixture.generate_payload(2),
                                                      head=app.token_autorization())
    formatted_json_str = pprint.pformat(put_the_item_in_the_cart.text)
    print(put_the_item_in_the_cart.request.body)
    print(put_the_item_in_the_cart, formatted_json_str, sep='\n\n')
    while loads(put_the_item_in_the_cart.text)['totalSum'] < 500:
        put_the_item_in_the_cart = app.order_fixture.cart \
            (dataset=app.order_fixture.generate_payload(2), head=app.token_autorization())
        if loads(put_the_item_in_the_cart.text)['totalSum'] >= 500:
            break
    assert "\"tradeName\"" in put_the_item_in_the_cart.text
    assert put_the_item_in_the_cart.status_code == 200

    use_promocode = app.order_fixture.cart_use_promocode(promoCode='MAИ', head=app.token_autorization())

    formatted_json_str = pprint.pformat(use_promocode.text)
    print(use_promocode.request.body)
    print(use_promocode, formatted_json_str, sep='\n\n')
    assert loads(use_promocode.text)['promoCodes'][0]['isUsed'] == True
    assert use_promocode.status_code == 200

    use_vitamins = app.order_fixture.cart_use_vitamins(vitaminsCount=10,
                                                       head=app.token_autorization())

    assert loads(use_vitamins.text)['vitaminsInfo']["vitaminsUsed"] > 0

    ordering = app.order_fixture.create_order(email=None, needEmail=False, needCall=False, mnogoRuCardId=None,
                                              head=app.token_autorization())
    formatted_json_str = pprint.pformat(ordering.text)
    print(ordering.request.body)
    print(ordering, formatted_json_str, sep='\n\n')
    assert ordering.status_code == 200
    assert "\"orderId\"" in ordering.text
    assert "\"orderNum\"" in ordering.text
    assert len(loads(ordering.text)['order']['promoCodes']) != 0
    assert loads(ordering.text)['order']["vitaminsUsed"] == 10


def test_use_20_vitaminok_and_promocode(app):
    put_the_item_in_the_cart = app.order_fixture.cart(dataset=app.order_fixture.generate_payload(2),
                                                      head=app.token_autorization())
    formatted_json_str = pprint.pformat(put_the_item_in_the_cart.text)
    print(put_the_item_in_the_cart.request.body)
    print(put_the_item_in_the_cart, formatted_json_str, sep='\n\n')
    while loads(put_the_item_in_the_cart.text)['totalSum'] < 500:
        put_the_item_in_the_cart = app.order_fixture.cart \
            (dataset=app.order_fixture.generate_payload(2), head=app.token_autorization())
        if loads(put_the_item_in_the_cart.text)['totalSum'] >= 500:
            break
    assert "\"tradeName\"" in put_the_item_in_the_cart.text
    assert put_the_item_in_the_cart.status_code == 200

    use_vitamins = app.order_fixture.cart_use_vitamins(vitaminsCount=20,
                                                       head=app.token_autorization())

    assert loads(use_vitamins.text)['vitaminsInfo']["vitaminsUsed"] > 0

    use_promocode = app.order_fixture.cart_use_promocode(promoCode='MOPE', head=app.token_autorization())

    formatted_json_str = pprint.pformat(use_promocode.text)
    print(use_promocode.request.body)
    print(use_promocode, formatted_json_str, sep='\n\n')
    assert loads(use_promocode.text)['promoCodes'][0]['isUsed'] == True
    assert use_promocode.status_code == 200

    ordering = app.order_fixture.create_order(email=None, needEmail=False, needCall=False, mnogoRuCardId=None,
                                              head=app.token_autorization())
    formatted_json_str = pprint.pformat(ordering.text)
    print(ordering.request.body)
    print(ordering, formatted_json_str, sep='\n\n')
    assert ordering.status_code == 200
    assert "\"orderId\"" in ordering.text
    assert "\"orderNum\"" in ordering.text
    assert len(loads(ordering.text)['order']['promoCodes']) != 0
    assert loads(ordering.text)['order']["vitaminsUsed"] == 20


def test_order_with_ordinary_good_special_good_and_vitamins(app):
    dataset = [{
        'itemId': '5d65073f2fd44a0001b124b0',
        'amount': 1,
        'deferred': False},
        {
            'itemId': '5d6504152fd44a0001b0ff62',
            'amount': 1,
            'deferred': False
        }]
    choice_autodest_before_order = app.choice_autodest(id=choice(parameters.autodestid_for_order),
                                                       head=app.token_autorization())
    formatted_json_str = pprint.pformat(choice_autodest_before_order.text)
    print(choice_autodest_before_order.request.body)
    print(choice_autodest_before_order, formatted_json_str, sep='\n\n')
    assert choice_autodest_before_order.status_code == 200

    put_the_item_in_the_cart = app.order_fixture.cart(dataset=dataset,
                                                      head=app.token_autorization())
    formatted_json_str = pprint.pformat(put_the_item_in_the_cart.text)
    print(put_the_item_in_the_cart.request.body)
    print(put_the_item_in_the_cart, formatted_json_str, sep='\n\n')
    assert "\"tradeName\"" in put_the_item_in_the_cart.text
    assert put_the_item_in_the_cart.status_code == 200

    use_promocode = app.order_fixture.cart_use_promocode(promoCode='9ZR1AOX', head=app.token_autorization())
    formatted_json_str = pprint.pformat(use_promocode.text)
    print(use_promocode.request.body)
    print(use_promocode, formatted_json_str, sep='\n\n')
    assert loads(use_promocode.text)['promoCodes'][0]['isUsed'] == True
    assert use_promocode.status_code == 200

    use_vitamins = app.order_fixture.cart_use_vitamins(vitaminsCount=30,
                                                       head=app.token_autorization())

    assert loads(use_vitamins.text)['vitaminsInfo']["vitaminsUsed"] > 0

    ordering = app.order_fixture.create_order(email=None, needEmail=False, needCall=False, mnogoRuCardId=None,
                                              head=app.token_autorization())
    formatted_json_str = pprint.pformat(ordering.text)
    print(ordering.request.body)
    print(ordering, formatted_json_str, sep='\n\n')
    assert ordering.status_code == 200
    assert "\"orderId\"" in ordering.text
    assert "\"orderNum\"" in ordering.text
    assert len(loads(ordering.text)['order']['promoCodes']) != 0
    assert loads(ordering.text)['order']["vitaminsUsed"] == 30


def test_use_promocode_sber_and_vitaminki(app):
    choice_autodest_before_order = app.choice_autodest(id=choice(parameters.autodestid_for_order),
                                                       head=app.token_autorization())
    formatted_json_str = pprint.pformat(choice_autodest_before_order.text)
    print(choice_autodest_before_order.request.body)
    print(choice_autodest_before_order, formatted_json_str, sep='\n\n')
    assert choice_autodest_before_order.status_code == 200

    put_the_item_in_the_cart = app.order_fixture.cart(dataset=app.order_fixture.generate_payload(2),
                                                      head=app.token_autorization())
    formatted_json_str = pprint.pformat(put_the_item_in_the_cart.text)
    print(put_the_item_in_the_cart.request.body)
    print(put_the_item_in_the_cart, formatted_json_str, sep='\n\n')
    while loads(put_the_item_in_the_cart.text)['totalSum'] < 500:
        put_the_item_in_the_cart = app.order_fixture.cart \
            (dataset=app.order_fixture.generate_payload(2), head=app.token_autorization())
        if loads(put_the_item_in_the_cart.text)['totalSum'] >= 500:
            break
    assert "\"tradeName\"" in put_the_item_in_the_cart.text
    assert put_the_item_in_the_cart.status_code == 200

    use_promocode = app.order_fixture.cart_use_promocode(promoCode="DV1NXTC81K4H", head=app.token_autorization())

    formatted_json_str = pprint.pformat(use_promocode.text)
    print(use_promocode.request.body)
    print(use_promocode, formatted_json_str, sep='\n\n')
    assert loads(use_promocode.text)['promoCodes'][0]['isUsed'] == True
    assert use_promocode.status_code == 200

    use_vitamins = app.order_fixture.cart_use_vitamins(vitaminsCount=20,
                                                       head=app.token_autorization())

    assert loads(use_vitamins.text)['vitaminsInfo']["vitaminsUsed"] > 0

    ordering = app.order_fixture.create_order(email=None, needEmail=False, needCall=False, mnogoRuCardId=None,
                                              head=app.token_autorization())
    formatted_json_str = pprint.pformat(ordering.text)
    print(ordering.request.body)
    print(ordering, formatted_json_str, sep='\n\n')
    assert ordering.status_code == 200
    assert "\"orderId\"" in ordering.text
    assert "\"orderNum\"" in ordering.text
    assert len(loads(ordering.text)['order']['promoCodes']) != 0
    assert loads(ordering.text)['order']["vitaminsUsed"] == 20


def test_use_promocode_olekstra_and_vitaminki(app):
    dataset = [{
        'itemId': '5d6509d12fd44a0001b1434b',
        'amount': 1,
        'deferred': False
    }]
    put_the_item_in_the_cart = app.order_fixture.cart(dataset=dataset,
                                                      head=app.token_autorization())
    formatted_json_str = pprint.pformat(put_the_item_in_the_cart.text)
    print(put_the_item_in_the_cart.request.body)
    print(put_the_item_in_the_cart, formatted_json_str, sep='\n\n')
    assert "\"tradeName\"" in put_the_item_in_the_cart.text
    assert put_the_item_in_the_cart.status_code == 200

    use_promocode = app.order_fixture.cart_use_promocode(promoCode='6830016944074', head=app.token_autorization())
    formatted_json_str = pprint.pformat(use_promocode.text)
    print(use_promocode.request.body)
    print(use_promocode, formatted_json_str, sep='\n\n')
    assert loads(use_promocode.text)['promoCodes'][0]['isUsed'] == True
    assert use_promocode.status_code == 200

    use_vitamins = app.order_fixture.cart_use_vitamins(vitaminsCount=30,
                                                       head=app.token_autorization())

    assert loads(use_vitamins.text)['vitaminsInfo']["vitaminsUsed"] == 0

    ordering = app.order_fixture.create_order(email=None, needEmail=False, needCall=False, mnogoRuCardId=None,
                                              head=app.token_autorization())
    formatted_json_str = pprint.pformat(ordering.text)
    print(ordering.request.body)
    print(ordering, formatted_json_str, sep='\n\n')
    assert ordering.status_code == 200
    assert "\"orderId\"" in ordering.text
    assert "\"orderNum\"" in ordering.text
    assert len(loads(ordering.text)['order']['promoCodes']) != 0


def test_use_promocode_vtb_and_vitaminki(app):
    choice_autodest_before_order = app.choice_autodest(id=choice(parameters.autodestid_for_order),
                                                       head=app.token_autorization())
    formatted_json_str = pprint.pformat(choice_autodest_before_order.text)
    print(choice_autodest_before_order.request.body)
    print(choice_autodest_before_order, formatted_json_str, sep='\n\n')
    assert choice_autodest_before_order.status_code == 200

    put_the_item_in_the_cart = app.order_fixture.cart(dataset=app.order_fixture.generate_payload(2),
                                                      head=app.token_autorization())
    formatted_json_str = pprint.pformat(put_the_item_in_the_cart.text)
    print(put_the_item_in_the_cart.request.body)
    print(put_the_item_in_the_cart, formatted_json_str, sep='\n\n')
    while loads(put_the_item_in_the_cart.text)['totalSum'] < 500:
        put_the_item_in_the_cart = app.order_fixture.cart \
            (dataset=app.order_fixture.generate_payload(2), head=app.token_autorization())
        if loads(put_the_item_in_the_cart.text)['totalSum'] >= 500:
            break
    assert "\"tradeName\"" in put_the_item_in_the_cart.text
    assert put_the_item_in_the_cart.status_code == 200

    use_promocode = app.order_fixture.cart_use_promocode(promoCode="485242O874OOO1O3", head=app.token_autorization())

    formatted_json_str = pprint.pformat(use_promocode.text)
    print(use_promocode.request.body)
    print(use_promocode, formatted_json_str, sep='\n\n')
    assert loads(use_promocode.text)['promoCodes'][0]['isUsed'] == True
    assert use_promocode.status_code == 200

    use_vitamins = app.order_fixture.cart_use_vitamins(vitaminsCount=70,
                                                       head=app.token_autorization())

    assert loads(use_vitamins.text)['vitaminsInfo']["vitaminsUsed"] > 0

    ordering = app.order_fixture.create_order(email=None, needEmail=False, needCall=False, mnogoRuCardId=None,
                                              head=app.token_autorization())
    formatted_json_str = pprint.pformat(ordering.text)
    print(ordering.request.body)
    print(ordering, formatted_json_str, sep='\n\n')
    assert ordering.status_code == 200
    assert "\"orderId\"" in ordering.text
    assert "\"orderNum\"" in ordering.text
    assert len(loads(ordering.text)['order']['promoCodes']) != 0
    assert loads(ordering.text)['order']["vitaminsUsed"] == 50


def test_use_promocode_for_special_good_and_more_vitamins(app):
    dataset = [{
        'itemId': '5d6509c484406a0001aaf096',
        'amount': 1,
        'deferred': False
    }]
    put_the_item_in_the_cart = app.order_fixture.cart(dataset=dataset,
                                                      head=app.token_autorization())
    formatted_json_str = pprint.pformat(put_the_item_in_the_cart.text)
    print(put_the_item_in_the_cart.request.body)
    print(put_the_item_in_the_cart, formatted_json_str, sep='\n\n')
    assert "\"tradeName\"" in put_the_item_in_the_cart.text
    assert put_the_item_in_the_cart.status_code == 200

    use_promocode = app.order_fixture.cart_use_promocode(promoCode='5HZVHCJ', head=app.token_autorization())
    formatted_json_str = pprint.pformat(use_promocode.text)
    print(use_promocode.request.body)
    print(use_promocode, formatted_json_str, sep='\n\n')
    assert loads(use_promocode.text)['promoCodes'][0]['isUsed'] == True
    assert use_promocode.status_code == 200

    use_vitamins = app.order_fixture.cart_use_vitamins(vitaminsCount=20,
                                                       head=app.token_autorization())

    assert loads(use_vitamins.text)['vitaminsInfo']["vitaminsUsed"] > 0
    assert loads(use_vitamins.text)['promoCodes'][0]['isUsed'] == False
    assert loads(use_vitamins.text)['promoCodes'][0]['hint'] == 'Промо-код не дает наилучшую скидку по данной корзине'

    ordering = app.order_fixture.create_order(email=None, needEmail=False, needCall=False, mnogoRuCardId=None,
                                              head=app.token_autorization())
    formatted_json_str = pprint.pformat(ordering.text)
    print(ordering.request.body)
    print(ordering, formatted_json_str, sep='\n\n')
    assert ordering.status_code == 200
    assert "\"orderId\"" in ordering.text
    assert "\"orderNum\"" in ordering.text
    assert len(loads(ordering.text)['order']['promoCodes']) == 0
    assert loads(ordering.text)['order']["vitaminsUsed"] == 20

# Баг тест не закончен - т.к 409
def test_use_promocode_for_special_good_and_less_vitamins(app):
    dataset = [{
        'itemId': '5d65073f2fd44a0001b124b0',
        'amount': 1,
        'deferred': False
    }]
    put_the_item_in_the_cart = app.order_fixture.cart(dataset=dataset,
                                                      head=app.token_autorization())
    formatted_json_str = pprint.pformat(put_the_item_in_the_cart.text)
    print(put_the_item_in_the_cart.request.body)
    print(put_the_item_in_the_cart, formatted_json_str, sep='\n\n')
    assert "\"tradeName\"" in put_the_item_in_the_cart.text
    assert put_the_item_in_the_cart.status_code == 200

    use_promocode = app.order_fixture.cart_use_promocode(promoCode='9ZR1AOX', head=app.token_autorization())
    formatted_json_str = pprint.pformat(use_promocode.text)
    print(use_promocode.request.body)
    print(use_promocode, formatted_json_str, sep='\n\n')
    assert loads(use_promocode.text)['promoCodes'][0]['isUsed'] == True

    use_vitamins = app.order_fixture.cart_use_vitamins(vitaminsCount=100,
                                                       head=app.token_autorization())
    assert loads(use_vitamins.text)['vitaminsInfo']["vitaminsUsed"] == 0
    formatted_json_str = pprint.pformat(use_vitamins.text)
    print(use_vitamins.request.body)
    print(use_vitamins, formatted_json_str, sep='\n\n')

    ordering = app.order_fixture.create_order(email=None, needEmail=False, needCall=False, mnogoRuCardId=None,
                                              head=app.token_autorization())
    formatted_json_str = pprint.pformat(ordering.text)
    print(ordering.request.body)
    print(ordering, formatted_json_str, sep='\n\n')
    assert ordering.status_code == 200
    assert "\"orderId\"" in ordering.text
    assert "\"orderNum\"" in ordering.text
    assert len(loads(ordering.text)['order']['promoCodes']) > 0
    assert loads(ordering.text)['order']["vitaminsUsed"] == 0


def test_use_promocode_sberbank_and_vtb_discount_sber_more(app):
    put_the_item_in_the_cart = app.order_fixture.cart(dataset=app.order_fixture.generate_payload(2),
                                                      head=app.token_autorization())
    formatted_json_str = pprint.pformat(put_the_item_in_the_cart.text)
    print(put_the_item_in_the_cart.request.body)
    print(put_the_item_in_the_cart, formatted_json_str, sep='\n\n')
    while loads(put_the_item_in_the_cart.text)['totalSum'] < 10000:
        put_the_item_in_the_cart = app.order_fixture.cart \
            (dataset=app.order_fixture.generate_payload(2), head=app.token_autorization())
        if loads(put_the_item_in_the_cart.text)['totalSum'] >= 10000:
            break
    assert "\"tradeName\"" in put_the_item_in_the_cart.text
    assert put_the_item_in_the_cart.status_code == 200

    use_promocode = app.order_fixture.cart_use_promocode(promoCode='DV11N7C8117U', head=app.token_autorization())

    formatted_json_str = pprint.pformat(use_promocode.text)
    print(use_promocode.request.body)
    print(use_promocode, formatted_json_str, sep='\n\n')
    assert loads(use_promocode.text)['promoCodes'][0]['isUsed'] == True
    assert use_promocode.status_code == 200

    use_promocode2 = app.order_fixture.cart_use_promocode(promoCode='775353O836OOO117', head=app.token_autorization())
    formatted_json_str = pprint.pformat(use_promocode2.text)
    print(use_promocode2.request.body)
    print(use_promocode2, formatted_json_str, sep='\n\n')
    assert loads(use_promocode2.text)['promoCodes'][1]['isUsed'] == False
    assert loads(use_promocode2.text)['promoCodes'][1]['hint'] == 'Промо-код не дает наилучшую скидку по данной корзине'
    assert use_promocode2.status_code == 200

    ordering = app.order_fixture.create_order(email=None, needEmail=False, needCall=False, mnogoRuCardId=None,
                                              head=app.token_autorization())
    formatted_json_str = pprint.pformat(ordering.text)
    print(ordering.request.body)
    print(ordering, formatted_json_str, sep='\n\n')
    assert ordering.status_code == 200
    assert "\"orderId\"" in ordering.text
    assert "\"orderNum\"" in ordering.text
    assert len(loads(ordering.text)['order']['promoCodes']) > 0

    delete_promocode = app.order_fixture.delete_promocode_from_the_cart(promoCode='775353O836OOO117',
                                                                              head=app.token_autorization())


def test_use_promocode_sberbank_and_vtb_discount_vtb_more(app):
    put_the_item_in_the_cart = app.order_fixture.cart(dataset=app.order_fixture.generate_payload(2),
                                                      head=app.token_autorization())
    formatted_json_str = pprint.pformat(put_the_item_in_the_cart.text)
    print(put_the_item_in_the_cart.request.body)
    print(put_the_item_in_the_cart, formatted_json_str, sep='\n\n')
    while loads(put_the_item_in_the_cart.text)['totalSum'] < 400:
        put_the_item_in_the_cart = app.order_fixture.cart \
            (dataset=app.order_fixture.generate_payload(2), head=app.token_autorization())
        if loads(put_the_item_in_the_cart.text)['totalSum'] >= 400:
            break
    assert "\"tradeName\"" in put_the_item_in_the_cart.text
    assert put_the_item_in_the_cart.status_code == 200

    use_promocode = app.order_fixture.cart_use_promocode(promoCode='DV1QDUC81NDM', head=app.token_autorization())

    formatted_json_str = pprint.pformat(use_promocode.text)
    print(use_promocode.request.body)
    print(use_promocode, formatted_json_str, sep='\n\n')
    assert loads(use_promocode.text)['promoCodes'][0]['isUsed'] == True
    assert use_promocode.status_code == 200

    use_promocode2 = app.order_fixture.cart_use_promocode(promoCode='O8549OO848OOOO53', head=app.token_autorization())
    formatted_json_str = pprint.pformat(use_promocode2.text)
    print(use_promocode2.request.body)
    print(use_promocode2, formatted_json_str, sep='\n\n')
    assert loads(use_promocode2.text)['promoCodes'][0]['isUsed'] == False
    assert loads(use_promocode2.text)['promoCodes'][0]['hint'] == 'Промо-код не дает наилучшую скидку по данной корзине'
    assert use_promocode2.status_code == 200

    ordering = app.order_fixture.create_order(email=None, needEmail=False, needCall=False, mnogoRuCardId=None,
                                              head=app.token_autorization())
    formatted_json_str = pprint.pformat(ordering.text)
    print(ordering.request.body)
    print(ordering, formatted_json_str, sep='\n\n')
    assert ordering.status_code == 200
    assert "\"orderId\"" in ordering.text
    assert "\"orderNum\"" in ordering.text
    assert len(loads(ordering.text)['order']['promoCodes']) == 1

    delete_promocode = app.order_fixture.delete_promocode_from_the_cart(promoCode='DV1QDUC81NDM',
                                                                        head=app.token_autorization())


def test_use_promocode_olekstra_and_sber(app):
    dataset = [{
        'itemId': '5d6509d12fd44a0001b1434b',
        'amount': 1,
        'deferred': False
    }]
    put_the_item_in_the_cart = app.order_fixture.cart(dataset=dataset,
                                                      head=app.token_autorization())
    formatted_json_str = pprint.pformat(put_the_item_in_the_cart.text)
    print(put_the_item_in_the_cart.request.body)
    print(put_the_item_in_the_cart, formatted_json_str, sep='\n\n')
    assert "\"tradeName\"" in put_the_item_in_the_cart.text
    assert put_the_item_in_the_cart.status_code == 200

    use_promocode = app.order_fixture.cart_use_promocode(promoCode='6830016944074', head=app.token_autorization())
    formatted_json_str = pprint.pformat(use_promocode.text)
    print(use_promocode.request.body)
    print(use_promocode, formatted_json_str, sep='\n\n')
    assert loads(use_promocode.text)['promoCodes'][0]['isUsed'] == True
    assert use_promocode.status_code == 200

    use_promocode2 = app.order_fixture.cart_use_promocode(promoCode='DV2K3CC82JBL', head=app.token_autorization())
    formatted_json_str = pprint.pformat(use_promocode2.text)
    print(use_promocode2.request.body)
    print(use_promocode2, formatted_json_str, sep='\n\n')
    assert loads(use_promocode2.text)['promoCodes'][0]['isUsed'] == False
    assert loads(use_promocode2.text)['promoCodes'][0]['hint'] == 'Промо-код не дает наилучшую скидку по данной корзине'
    assert use_promocode2.status_code == 200

    ordering = app.order_fixture.create_order(email=None, needEmail=False, needCall=False, mnogoRuCardId=None,
                                              head=app.token_autorization())
    formatted_json_str = pprint.pformat(ordering.text)
    print(ordering.request.body)
    print(ordering, formatted_json_str, sep='\n\n')
    assert ordering.status_code == 200
    assert "\"orderId\"" in ordering.text
    assert "\"orderNum\"" in ordering.text
    assert len(loads(ordering.text)['order']['promoCodes']) == 1

    delete_promocode = app.order_fixture.delete_promocode_from_the_cart(promoCode='6830016944074',
                                                                        head=app.token_autorization())


def test_use_vitamins_and_mnogo_ru_cart(app):
    put_the_item_in_the_cart = app.order_fixture.cart(dataset=app.order_fixture.generate_payload(2),
                                                      head=app.token_autorization())
    formatted_json_str = pprint.pformat(put_the_item_in_the_cart.text)
    print(put_the_item_in_the_cart.request.body)
    print(put_the_item_in_the_cart, formatted_json_str, sep='\n\n')
    while loads(put_the_item_in_the_cart.text)['totalSum'] < 500:
        put_the_item_in_the_cart = app.order_fixture.cart \
            (dataset=app.order_fixture.generate_payload(2), head=app.token_autorization())
        if loads(put_the_item_in_the_cart.text)['totalSum'] >= 500:
            break
    assert "\"tradeName\"" in put_the_item_in_the_cart.text
    assert put_the_item_in_the_cart.status_code == 200

    use_vitamins = app.order_fixture.cart_use_vitamins(vitaminsCount=40,
                                                       head=app.token_autorization())
    assert loads(use_vitamins.text)['vitaminsInfo']["vitaminsUsed"] > 0

    ordering = app.order_fixture.create_order(email='nat19@yandex.ru', needEmail=False, needCall=False,
                                              mnogoRuCardId='12345678', head=app.token_autorization())
    formatted_json_str = pprint.pformat(ordering.text)
    print(ordering.request.body)
    print(ordering, formatted_json_str, sep='\n\n')
    assert "\"orderId\"" in ordering.text
    assert "\"orderNum\"" in ordering.text
    assert "\"MnogoRu\"" in ordering.text
    assert loads(ordering.text)['order']["vitaminsUsed"] == 40


def test_use_promocode_and_mnogo_ru_cart(app):
    put_the_item_in_the_cart = app.order_fixture.cart(dataset=app.order_fixture.generate_payload(2),
                                                      head=app.token_autorization())
    formatted_json_str = pprint.pformat(put_the_item_in_the_cart.text)
    print(put_the_item_in_the_cart.request.body)
    print(put_the_item_in_the_cart, formatted_json_str, sep='\n\n')
    while loads(put_the_item_in_the_cart.text)['totalSum'] < 500:
        put_the_item_in_the_cart = app.order_fixture.cart \
            (dataset=app.order_fixture.generate_payload(2), head=app.token_autorization())
        if loads(put_the_item_in_the_cart.text)['totalSum'] >= 500:
            break
    assert "\"tradeName\"" in put_the_item_in_the_cart.text
    assert put_the_item_in_the_cart.status_code == 200

    use_promocode = app.order_fixture.cart_use_promocode(promoCode="RIGA2", head=app.token_autorization())

    formatted_json_str = pprint.pformat(use_promocode.text)
    print(use_promocode.request.body)
    print(use_promocode, formatted_json_str, sep='\n\n')
    assert loads(use_promocode.text)['promoCodes'][0]['isUsed'] == True
    assert use_promocode.status_code == 200

    ordering = app.order_fixture.create_order(email='nat19@yandex.ru', needEmail=False, needCall=False,
                                              mnogoRuCardId='12345678', head=app.token_autorization())
    formatted_json_str = pprint.pformat(ordering.text)
    print(ordering.request.body)
    print(ordering, formatted_json_str, sep='\n\n')
    assert "\"orderId\"" in ordering.text
    assert "\"orderNum\"" in ordering.text
    assert "\"MnogoRu\"" in ordering.text
    assert len(loads(ordering.text)['order']['promoCodes']) == 1


def test_use_vitamins_promocode_and_mnogo_ru_cart(app):
    put_the_item_in_the_cart = app.order_fixture.cart(dataset=app.order_fixture.generate_payload(2),
                                                      head=app.token_autorization())
    formatted_json_str = pprint.pformat(put_the_item_in_the_cart.text)
    print(put_the_item_in_the_cart.request.body)
    print(put_the_item_in_the_cart, formatted_json_str, sep='\n\n')
    while loads(put_the_item_in_the_cart.text)['totalSum'] < 500:
        put_the_item_in_the_cart = app.order_fixture.cart \
            (dataset=app.order_fixture.generate_payload(2), head=app.token_autorization())
        if loads(put_the_item_in_the_cart.text)['totalSum'] >= 500:
            break
    assert "\"tradeName\"" in put_the_item_in_the_cart.text
    assert put_the_item_in_the_cart.status_code == 200

    use_vitamins = app.order_fixture.cart_use_vitamins(vitaminsCount=30,
                                                       head=app.token_autorization())

    assert loads(use_vitamins.text)['vitaminsInfo']["vitaminsUsed"] > 0

    use_promocode = app.order_fixture.cart_use_promocode(promoCode="RIGA2", head=app.token_autorization())

    formatted_json_str = pprint.pformat(use_promocode.text)
    print(use_promocode.request.body)
    print(use_promocode, formatted_json_str, sep='\n\n')
    assert loads(use_promocode.text)['promoCodes'][0]['isUsed'] == True
    assert use_promocode.status_code == 200

    ordering = app.order_fixture.create_order(email='nat19@yandex.ru', needEmail=False, needCall=False,
                                              mnogoRuCardId='12345678', head=app.token_autorization())
    formatted_json_str = pprint.pformat(ordering.text)
    print(ordering.request.body)
    print(ordering, formatted_json_str, sep='\n\n')
    assert "\"orderId\"" in ordering.text
    assert "\"orderNum\"" in ordering.text
    assert "\"MnogoRu\"" in ordering.text
    assert len(loads(ordering.text)['order']['promoCodes']) == 1
    assert loads(ordering.text)['order']["vitaminsUsed"] == 30













