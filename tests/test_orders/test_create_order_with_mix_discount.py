import pprint
from json import loads
from random import choice
from model import parameters
from time import sleep


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

    use_promocode = app.order_fixture.cart_use_promocode(promoCode="KUPON", head=app.token_autorization())

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
    assert len(loads(ordering.text)['order']['promoCodes']) == 0
    assert loads(ordering.text)['order']["vitaminsUsed"] == 100  #тест пока не работает - так как 500 - когда поправят - запустить для отладки


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





