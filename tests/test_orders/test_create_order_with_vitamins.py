import pprint
from json import loads
from random import randrange, choice
from model import parameters

# User


def test_create_order_with_vitamins(app):
    put_the_item_in_the_cart = app.order_fixture.cart(dataset=app.order_fixture.generate_payload(2),
                                                      head=app.token_autorization())
    formatted_json_str = pprint.pformat(put_the_item_in_the_cart.text)
    print(put_the_item_in_the_cart.request.body)
    print(put_the_item_in_the_cart, formatted_json_str, sep='\n\n')
    assert "\"tradeName\"" in put_the_item_in_the_cart.text
    assert put_the_item_in_the_cart.status_code == 200

    use_vitamins = app.order_fixture.cart_use_vitamins(vitaminsCount=randrange(20, 100, 10),
                                                       head=app.token_autorization())
    try:
        assert loads(use_vitamins.text)['vitaminsInfo']["vitaminsUsed"] > 0
    except AssertionError:
        test_add_vitamins_to_user(app)
        use_vitamins = app.order_fixture.cart_use_vitamins(vitaminsCount=randrange(20, 100, 10),
                                                           head=app.token_autorization())

    choice_autodest_before_order = app.choice_autodest(id=choice(parameters.autodestid_for_order),
                                                       head=app.token_autorization())
    print(choice_autodest_before_order.request.body)
    print(choice_autodest_before_order, formatted_json_str, sep='\n\n')
    assert choice_autodest_before_order.status_code == 200

    ordering = app.order_fixture.create_order(email=None, needEmail=False, needCall=False, mnogoRuCardId=None,
                                              head=app.token_autorization())
    formatted_json_str = pprint.pformat(ordering.text)
    print(ordering.request.body)
    print(ordering, formatted_json_str, sep='\n\n')

    while ordering.status_code == 400 and "\"Минимальная сумма заказа =\"" in ordering.text:
        put_the_item_in_the_cart = app.order_fixture.cart(dataset=app.order_fixture.generate_payload(3),
                                                          head=app.token_autorization())
        assert "\"tradeName\"" in put_the_item_in_the_cart.text
        assert put_the_item_in_the_cart.status_code == 200

        use_vitamins = app.order_fixture.cart_use_vitamins(vitaminsCount=randrange(20, 100, 10),
                                                           head=app.token_autorization())

        ordering = app.order_fixture.create_order(email=None, needEmail=False, needCall=False, mnogoRuCardId=None,
                                              head=app.token_autorization())
        print(ordering, formatted_json_str, sep='\n\n')
        if ordering.status_code == 200:
            break
    assert "\"orderId\"" in ordering.text
    assert "\"orderNum\"" in ordering.text
    assert loads(ordering.text)['order']["vitaminsUsed"] > 0


def test_create_order_with_invalid_count_vitamins(app):
    put_the_item_in_the_cart = app.order_fixture.cart(dataset=app.order_fixture.generate_payload(2),
                                                      head=app.token_autorization())
    formatted_json_str = pprint.pformat(put_the_item_in_the_cart.text)
    print(put_the_item_in_the_cart.request.body)
    print(put_the_item_in_the_cart, formatted_json_str, sep='\n\n')
    assert "\"tradeName\"" in put_the_item_in_the_cart.text
    assert put_the_item_in_the_cart.status_code == 200

    use_vitamins = app.order_fixture.cart_use_vitamins(vitaminsCount=10,
                                                       head=app.token_autorization())

    assert loads(use_vitamins.text)['vitaminsInfo']["vitaminsUsed"] == 0

    choice_autodest_before_order = app.choice_autodest(id=choice(parameters.autodestid_for_order),
                                                       head=app.token_autorization())
    print(choice_autodest_before_order.request.body)
    print(choice_autodest_before_order, formatted_json_str, sep='\n\n')
    assert choice_autodest_before_order.status_code == 200

    ordering = app.order_fixture.create_order(email=None, needEmail=False, needCall=False, mnogoRuCardId=None,
                                              head=app.token_autorization())
    formatted_json_str = pprint.pformat(ordering.text)
    print(ordering.request.body)
    print(ordering, formatted_json_str, sep='\n\n')

    while ordering.status_code == 400 and "\"Минимальная сумма заказа =\"" in ordering.text:
        put_the_item_in_the_cart = app.order_fixture.cart(dataset=app.order_fixture.generate_payload(3),
                                                          head=app.token_autorization())
        assert "\"tradeName\"" in put_the_item_in_the_cart.text
        assert put_the_item_in_the_cart.status_code == 200

        use_vitamins = app.order_fixture.cart_use_vitamins(vitaminsCount=10,
                                                           head=app.token_autorization())

        ordering = app.order_fixture.create_order(email=None, needEmail=False, needCall=False, mnogoRuCardId=None,
                                              head=app.token_autorization())
        print(ordering, formatted_json_str, sep='\n\n')
        if ordering.status_code == 200:
            break
    assert "\"orderId\"" in ordering.text
    assert "\"orderNum\"" in ordering.text
    assert loads(ordering.text)['order']["vitaminsUsed"] == 0


def test_create_order_with_invalid_count_vitamins_overrange(app):
    put_the_item_in_the_cart = app.order_fixture.cart(dataset=app.order_fixture.generate_payload(2),
                                                      head=app.token_autorization())
    formatted_json_str = pprint.pformat(put_the_item_in_the_cart.text)
    print(put_the_item_in_the_cart.request.body)
    print(put_the_item_in_the_cart, formatted_json_str, sep='\n\n')
    assert "\"tradeName\"" in put_the_item_in_the_cart.text
    assert put_the_item_in_the_cart.status_code == 200

    use_vitamins = app.order_fixture.cart_use_vitamins(vitaminsCount=179,
                                                       head=app.token_autorization())

    assert loads(use_vitamins.text)['vitaminsInfo']["vitaminsUsed"] > 0

    choice_autodest_before_order = app.choice_autodest(id=choice(parameters.autodestid_for_order),
                                                       head=app.token_autorization())
    print(choice_autodest_before_order.request.body)
    print(choice_autodest_before_order, formatted_json_str, sep='\n\n')
    assert choice_autodest_before_order.status_code == 200

    ordering = app.order_fixture.create_order(email=None, needEmail=False, needCall=False, mnogoRuCardId=None,
                                              head=app.token_autorization())
    formatted_json_str = pprint.pformat(ordering.text)
    print(ordering.request.body)
    print(ordering, formatted_json_str, sep='\n\n')

    while ordering.status_code == 400 and "\"Минимальная сумма заказа =\"" in ordering.text:
        put_the_item_in_the_cart = app.order_fixture.cart(dataset=app.order_fixture.generate_payload(3),
                                                          head=app.token_autorization())
        assert "\"tradeName\"" in put_the_item_in_the_cart.text
        assert put_the_item_in_the_cart.status_code == 200

        use_vitamins = app.order_fixture.cart_use_vitamins(vitaminsCount=150,
                                                           head=app.token_autorization())

        ordering = app.order_fixture.create_order(email=None, needEmail=False, needCall=False, mnogoRuCardId=None,
                                              head=app.token_autorization())
        print(ordering, formatted_json_str, sep='\n\n')
        if ordering.status_code == 200:
            break
    assert "\"orderId\"" in ordering.text
    assert "\"orderNum\"" in ordering.text
    assert loads(ordering.text)['order']["vitaminsUsed"] > 0


def test_order_with_vitamins_but_min_summ_failed(app):
    cart = app.order_fixture.get_cart_user(head=app.token_autorization())
    cart_json = loads(cart.text)

    replace_deferred_items = cart_json['items']
    for item in replace_deferred_items:
        item['amount'] = 0

    cart = app.order_fixture.cart(dataset=replace_deferred_items, head=app.token_autorization())

    dataset = []
    payload = {'itemId': '5d64fd832fd44a0001b0b662', 'amount': 1, 'deferred': False}
    dataset.append(payload)

    put_the_item_in_the_cart = app.order_fixture.cart(dataset=dataset,
                                                      head=app.token_autorization())

    formatted_json_str = pprint.pformat(put_the_item_in_the_cart.text)
    print(put_the_item_in_the_cart.request.body)
    print(put_the_item_in_the_cart, formatted_json_str, sep='\n\n')
    assert "\"tradeName\"" in put_the_item_in_the_cart.text
    assert put_the_item_in_the_cart.status_code == 200

    use_vitamins = app.order_fixture.cart_use_vitamins(vitaminsCount=50,
                                                        head=app.token_autorization())

    assert loads(use_vitamins.text)['vitaminsInfo']["vitaminsUsed"] > 0

    choice_autodest_before_order = app.choice_autodest(id=choice(parameters.autodestid_for_order),
                                                       head=app.token_autorization())
    print(choice_autodest_before_order.request.body)
    print(choice_autodest_before_order, formatted_json_str, sep='\n\n')
    assert choice_autodest_before_order.status_code == 200

    ordering = app.order_fixture.create_order(email=None, needEmail=False, needCall=False, mnogoRuCardId=None,
                                               head=app.token_autorization())
    formatted_json_str = pprint.pformat(ordering.text)
    print(ordering.request.body)
    print(ordering, formatted_json_str, sep='\n\n')

    assert ordering.status_code == 400 and "\"Минимальная сумма заказа =" in ordering.text

# SU


def test_add_vitamins_to_user(app):
    add_vitamins = app.order_fixture.actions_with_vitamins(userId='5ee852c50521b00001edffed', head=app.token_auth_super_user(),
                                                           value=100, updatingType='Credit')

    formatted_json_str = pprint.pformat(add_vitamins.text)
    print(add_vitamins.request.body)
    print(add_vitamins, formatted_json_str, sep='\n\n')
    assert add_vitamins.status_code == 200
    assert add_vitamins.text.isdigit()


def test_remove_vitamins_from_user(app):
    remove_vitamins = app.order_fixture.actions_with_vitamins(userId='5ee852c50521b00001edffed', head=app.token_auth_super_user(),
                                                              value=20, updatingType='Debit')
    if remove_vitamins.status_code == 409 and "\"Запрошенная сумма списания больше текущего баланса пользователя\"" in remove_vitamins.text:
        add_vitamins = app.order_fixture.actions_with_vitamins(userId='5ee852c50521b00001edffed', head=app.token_auth_super_user(),
                                                               value=20, updatingType='Credit')
        assert add_vitamins.status_code == 200
        assert add_vitamins.text.isdigit()

        remove_vitamins = app.order_fixture.actions_with_vitamins(userId='5ee852c50521b00001edffed', head=app.token_auth_super_user(),
                                                                  value=1, updatingType='Debit')

    formatted_json_str = pprint.pformat(remove_vitamins.text)
    print(remove_vitamins.request.body)
    print(remove_vitamins, formatted_json_str, sep='\n\n')
    assert remove_vitamins.status_code == 200
    assert remove_vitamins.text.isdigit()


def test_create_order_with_vitamins_su(app):
    put_the_item_in_the_cart = app.order_fixture.cart(dataset=app.order_fixture.generate_payload(2),
                                                      head=app.token_auth_super_user(), userId='5ee852c50521b00001edffed')
    formatted_json_str = pprint.pformat(put_the_item_in_the_cart.text)
    print(put_the_item_in_the_cart.request.body)
    print(put_the_item_in_the_cart, formatted_json_str, sep='\n\n')
    assert "\"tradeName\"" in put_the_item_in_the_cart.text
    assert put_the_item_in_the_cart.status_code == 200

    use_vitamins = app.order_fixture.cart_use_vitamins(vitaminsCount=randrange(20, 100, 10),
                                                       head=app.token_auth_super_user(), userId='5ee852c50521b00001edffed')
    try:
        assert loads(use_vitamins.text)['vitaminsInfo']["vitaminsUsed"] > 0
    except AssertionError:
        test_add_vitamins_to_user(app)
        use_vitamins = app.order_fixture.cart_use_vitamins(vitaminsCount=randrange(20, 100, 10),
                                                           head=app.token_auth_super_user(), userId='5ee852c50521b00001edffed')

    choice_autodest_before_order = app.choice_autodest(id=choice(parameters.autodestid_for_order),
                                                            head=app.token_auth_super_user(), userId='5ee852c50521b00001edffed')
    print(choice_autodest_before_order.request.body)
    print(choice_autodest_before_order, formatted_json_str, sep='\n\n')
    assert choice_autodest_before_order.status_code == 200

    ordering = app.order_fixture.create_order(email=None, needEmail=False, needCall=False, mnogoRuCardId=None,
                                              head=app.token_auth_super_user(), userId='5ee852c50521b00001edffed')
    formatted_json_str = pprint.pformat(ordering.text)
    print(ordering.request.body)
    print(ordering, formatted_json_str, sep='\n\n')

    while ordering.status_code == 400 and "\"Минимальная сумма заказа =\"" in ordering.text:
        put_the_item_in_the_cart = app.order_fixture.cart(dataset=app.order_fixture.generate_payload(3),
                                                          head=app.token_auth_super_user(),
                                                          userId='5ee852c50521b00001edffed')
        assert "\"tradeName\"" in put_the_item_in_the_cart.text
        assert put_the_item_in_the_cart.status_code == 200

        use_vitamins = app.order_fixture.cart_use_vitamins(vitaminsCount=randrange(20, 100, 10),
                                                           head=app.token_auth_super_user(),
                                                           userId='5ee852c50521b00001edffed')

        ordering = app.order_fixture.create_order(email=None, needEmail=False, needCall=False, mnogoRuCardId=None,
                                                  head=app.token_auth_super_user(),
                                                  userId='5ee852c50521b00001edffed')
        print(ordering, formatted_json_str, sep='\n\n')
        if ordering.status_code == 200:
            break
    assert "\"orderId\"" in ordering.text
    assert "\"orderNum\"" in ordering.text
    assert loads(ordering.text)['order']["vitaminsUsed"] > 0














