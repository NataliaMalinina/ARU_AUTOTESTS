import pprint
from random import choice
from model import parameters


def test_min_sum_failed(app):                                                                                           #TODO надо дружиться с бд и делать выборку товаров оттуда
    put_the_item_in_the_cart = app.order_fixture.dataset_min_sum(head=app.token_autorization())
    formatted_json_str = pprint.pformat(put_the_item_in_the_cart.text)
    print(put_the_item_in_the_cart.request.body)
    print(put_the_item_in_the_cart, formatted_json_str, sep='\n\n')
    assert "\"tradeName\"" in put_the_item_in_the_cart.text
    assert put_the_item_in_the_cart.status_code == 200

    choice_autodest_before_order = app.choice_autodest_auth_user(id=choice(parameters.autodestid_for_order), head=app.token_autorization())
    print(choice_autodest_before_order.request.body)
    print(choice_autodest_before_order, formatted_json_str, sep='\n\n')
    assert choice_autodest_before_order.status_code == 200

    ordering = app.order_fixture.create_order(email=None, needEmail=False, needCall=False,
                                       mnogoRuCardId=None, head=app.token_autorization())
    formatted_json_str = pprint.pformat(ordering.text)
    print(ordering.request.body)
    print(ordering, formatted_json_str, sep='\n\n')
    assert "\"Минимальная сумма заказа =" in ordering.text
    assert ordering.status_code == 400


def test_order_autodest_false(app):
    put_the_item_in_the_cart = app.order_fixture.cart(dataset=app.order_fixture.generate_payload(2),
                                                      head=app.token_autorization())
    formatted_json_str = pprint.pformat(put_the_item_in_the_cart.text)
    print(put_the_item_in_the_cart.request.body)
    print(put_the_item_in_the_cart, formatted_json_str, sep='\n\n')
    assert "\"tradeName\"" in put_the_item_in_the_cart.text
    assert put_the_item_in_the_cart.status_code == 200

    choice_autodest_before_order = app.choice_autodest_auth_user(id=choice(parameters.not_active_autodest),
                                                                 head=app.token_autorization())
    print(choice_autodest_before_order.request.body)
    print(choice_autodest_before_order, formatted_json_str, sep='\n\n')
    assert choice_autodest_before_order.status_code == 404

    ordering = app.order_fixture.create_order(email=None, needEmail=False, needCall=False,
                                       mnogoRuCardId=None, head=app.token_autorization())
    formatted_json_str = pprint.pformat(ordering.text)
    print(ordering.request.body)
    print(ordering, formatted_json_str, sep='\n\n')
    assert ordering.status_code == 409
    assert "\"Невозможно определить пункт выдачи для формирования заказа\"" in ordering.text


def test_order_without_autodest(app):
    put_the_item_in_the_cart = app.order_fixture.cart(dataset=app.order_fixture.generate_payload(2),
                                                      head=app.token_autorization())
    formatted_json_str = pprint.pformat(put_the_item_in_the_cart.text)
    print(put_the_item_in_the_cart.request.body)
    print(put_the_item_in_the_cart, formatted_json_str, sep='\n\n')
    assert "\"tradeName\"" in put_the_item_in_the_cart.text
    assert put_the_item_in_the_cart.status_code == 200

    choice_city = app.choice_city_auth_user(id='5e56f692524b5400014ace3f', manualChange=True,
                                            head=app.token_autorization())
    assert choice_city.status_code == 200
    assert '{"id":' in choice_city.text

    choice_city = app.choice_city_auth_user(id='5e574686defa1e000131b5df', manualChange=True,
                                            head=app.token_autorization())
    assert choice_city.status_code == 200
    assert '{"id":' in choice_city.text

    ordering = app.order_fixture.create_order(email=None, needEmail=False, needCall=False,
                                       mnogoRuCardId=None, head=app.token_autorization())
    formatted_json_str = pprint.pformat(ordering.text)
    print(ordering.request.body)
    print(ordering, formatted_json_str, sep='\n\n')
    assert ordering.status_code == 409
    assert "\"Невозможно определить пункт выдачи для формирования заказа\"" in ordering.text







