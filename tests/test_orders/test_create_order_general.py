import pprint
from random import choice
from model import parameters


def test_general_order_create(app):
    put_the_item_in_the_cart = app.order_fixture.cart(dataset=app.order_fixture.generate_payload(3),                    #TODO надо дружиться с бд и делать выборку товаров оттуда
                                                      head=app.token_autorization())
    formatted_json_str = pprint.pformat(put_the_item_in_the_cart.text)
    print(put_the_item_in_the_cart.request.body)
    print(put_the_item_in_the_cart, formatted_json_str, sep='\n\n')
    assert "\"tradeName\"" in put_the_item_in_the_cart.text
    assert put_the_item_in_the_cart.status_code == 200

    choice_autodest_before_order = app.choice_autodest_auth_user(id=choice(parameters.autodestid_for_order), head=app.token_autorization())
    print(choice_autodest_before_order.request.body)
    print(choice_autodest_before_order, formatted_json_str, sep='\n\n')
    assert choice_autodest_before_order.status_code == 200

    ordering = app.order_fixture.order(email='nat19@yandex.ru', needEmail=False, needCall=False,
                                       mnogoRuCardId=None, head=app.token_autorization())
    formatted_json_str = pprint.pformat(ordering.text)
    print(ordering.request.body)
    print(ordering, formatted_json_str, sep='\n\n')
    if "\"Минимальная сумма заказа =" in ordering.text:
        assert ordering.status_code == 400
    else:
        assert ordering.status_code == 200
        assert "\"orderId\"" in ordering.text
        assert "\"orderNum\"" in ordering.text


def test_not_auth_user_order(app):
    ordering = app.order_fixture.order(email='nat19@yandex.ru', needEmail=False, needCall=False,
                                       mnogoRuCardId=None, head=app.token_shadow_user())
    formatted_json_str = pprint.pformat(ordering.text)
    print(ordering.request.body)
    print(ordering, formatted_json_str, sep='\n\n')
    assert ordering.status_code == 403


def test_without_token_user_order(app):
    ordering = app.order_fixture.order(email='nat19@yandex.ru', needEmail=False, needCall=False,
                                       mnogoRuCardId=None, head=None)
    formatted_json_str = pprint.pformat(ordering.text)
    print(ordering.request.body)
    print(ordering, formatted_json_str, sep='\n\n')
    assert ordering.status_code == 401


def test_su_order(app):
    put_the_item_in_the_cart = app.order_fixture.cart_su(dataset=app.order_fixture.generate_payload(2),
                                                      head=app.token_auth_admin_user(), userId='5ee852c50521b00001edffed')
    formatted_json_str = pprint.pformat(put_the_item_in_the_cart.text)
    print(put_the_item_in_the_cart.request.body)
    print(put_the_item_in_the_cart, formatted_json_str, sep='\n\n')
    assert "\"tradeName\"" in put_the_item_in_the_cart.text
    assert put_the_item_in_the_cart.status_code == 200

    choice_autodest_before_order = app.choice_autodest_su(id=choice(parameters.autodestid_for_order),
                                                          head=app.token_auth_admin_user(), userid='5ee852c50521b00001edffed')
    print(choice_autodest_before_order.request.body)
    print(choice_autodest_before_order, formatted_json_str, sep='\n\n')
    assert choice_autodest_before_order.status_code == 200

    ordering = app.order_fixture.order_su(email='nat19@yandex.ru', needEmail=False, needCall=False,
                                       mnogoRuCardId=None, head=app.token_auth_admin_user(), userId='5ee852c50521b00001edffed')
    formatted_json_str = pprint.pformat(ordering.text)
    print(ordering.request.body)
    print(ordering, formatted_json_str, sep='\n\n')
    if "\"Минимальная сумма заказа =" in ordering.text:
        assert ordering.status_code == 400
    else:
        assert ordering.status_code == 200
        assert "\"orderId\"" in ordering.text
        assert "\"orderNum\"" in ordering.text







