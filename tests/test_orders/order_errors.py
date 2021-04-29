import pprint
from json import loads
from random import choice, randint
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


def test_not_auth_user_order(app):
    ordering = app.order_fixture.create_order(email='nat19@yandex.ru', needEmail=False, needCall=False,
                                                  mnogoRuCardId=None, head=app.token_shadow_user())
    formatted_json_str = pprint.pformat(ordering.text)
    print(ordering.request.body)
    print(ordering, formatted_json_str, sep='\n\n')
    assert ordering.status_code == 403


def test_without_token_user_order(app):
    ordering = app.order_fixture.create_order(email='nat19@yandex.ru', needEmail=False, needCall=False,
                                       mnogoRuCardId=None, head=None)
    formatted_json_str = pprint.pformat(ordering.text)
    print(ordering.request.body)
    print(ordering, formatted_json_str, sep='\n\n')
    assert ordering.status_code == 401


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


def test_incorrect_id_for_delete_order(app):
    delete_order = app.order_fixture.delete_order(orderId=parameters.autodestid_for_order, head=app.token_autorization()) #берём id любой - чтобы он не нашёлся
    formatted_json_str = pprint.pformat(delete_order.text)
    print(delete_order, formatted_json_str, sep='\n\n')
    assert delete_order.status_code == 404
    assert "\"Совпадений по указанному Id не найдено\"" in delete_order.text


def test_duplicate_order(app):
    dataset = [{
        'itemId': '5d64fe6084406a0001aa6e06',
        'amount': 1,
        'deferred': False
    }]

    put_the_item_in_the_cart = app.order_fixture.cart(dataset=dataset,                                                  #ПОКА ЗАХАРДКОДИЛА ДАННЫЕ ТОВАРОВ И АПТЕК, ТАК КАК НА ТЕХЕ КАКАЯ-ТО ХЕРНЯ ТВОРИТСЯ ТОВАРЫ ДОБАВЛЯЮТСЯ И ТУТ ЖЕ СТАНОВЯТСЯ НЕ В НАЛИЧИИ ИЛИ ЦЕНА МЕНЯЕТСЯ app.order_fixture.generate_payload(3),
                                                      head=app.token_autorization())
    formatted_json_str = pprint.pformat(put_the_item_in_the_cart.text)
    print(put_the_item_in_the_cart.request.body)
    print(put_the_item_in_the_cart, formatted_json_str, sep='\n\n')
    assert "\"tradeName\"" in put_the_item_in_the_cart.text
    assert put_the_item_in_the_cart.status_code == 200

    choice_autodest_before_order = app.choice_autodest_auth_user(id='5d654e1e26306f000138a750',
                                                                 head=app.token_autorization())
    print(choice_autodest_before_order.request.body)
    print(choice_autodest_before_order, formatted_json_str, sep='\n\n')
    assert choice_autodest_before_order.status_code == 200

    ordering = app.order_fixture.create_order(email='nat19@yandex.ru', needEmail=False, needCall=False,
                                              mnogoRuCardId=None, head=app.token_autorization())

    # while ordering.status_code == 400 and "\"Минимальная сумма заказа =" in ordering.text:
    #     put_the_item_in_the_cart = app.order_fixture.cart(dataset=app.order_fixture.generate_payload(3),
    #                                                       head=app.token_autorization())
    #     assert "\"tradeName\"" in put_the_item_in_the_cart.text
    #     assert put_the_item_in_the_cart.status_code == 200
    #     ordering = app.order_fixture.create_order(email='nat19@yandex.ru', needEmail=False, needCall=False,
    #                                               mnogoRuCardId=None, head=app.token_autorization())
    #     print(ordering, formatted_json_str, sep='\n\n')
    #     if ordering.status_code == 200:
    #         break
    formatted_json_str = pprint.pformat(ordering.text)
    print(ordering.request.body)
    print(ordering, formatted_json_str, sep='\n\n')

    id_from_response = loads(ordering.text)['orderId']

    put_the_item_in_the_cart_order2 = app.order_fixture.cart(dataset=dataset, head=app.token_autorization())            #dataset=loads(put_the_item_in_the_cart.text)['items']
    print(put_the_item_in_the_cart_order2.request.body)
    print(put_the_item_in_the_cart_order2, formatted_json_str, sep='\n\n')
    assert "\"tradeName\"" in put_the_item_in_the_cart.text
    assert put_the_item_in_the_cart.status_code == 200
    ordering2 = app.order_fixture.create_order(email='nat19@yandex.ru', needEmail=False, needCall=False,
                                              mnogoRuCardId=None, head=app.token_autorization())
    formatted_json_str = pprint.pformat(ordering2.text)
    print(ordering2.request.body)
    print(ordering2, formatted_json_str, sep='\n\n')

    id_from_response_2 = loads(ordering2.text)['orderId']

    assert id_from_response == id_from_response_2


def test_incorrect_number_mnoro_ru(app):
    put_the_item_in_the_cart = app.order_fixture.cart(dataset=app.order_fixture.generate_payload(3),
                                                      head=app.token_autorization())
    formatted_json_str = pprint.pformat(put_the_item_in_the_cart.text)
    print(put_the_item_in_the_cart.request.body)
    print(put_the_item_in_the_cart, formatted_json_str, sep='\n\n')
    assert "\"tradeName\"" in put_the_item_in_the_cart.text
    assert put_the_item_in_the_cart.status_code == 200

    choice_autodest_before_order = app.choice_autodest_auth_user(id=choice(parameters.autodestid_for_order),
                                                                 head=app.token_autorization())
    print(choice_autodest_before_order.request.body)
    print(choice_autodest_before_order, formatted_json_str, sep='\n\n')
    assert choice_autodest_before_order.status_code == 200

    ordering = app.order_fixture.create_order(email='nat19@yandex.ru', needEmail=False, needCall=False,
                                              mnogoRuCardId='1234567890123', head=app.token_autorization())
    formatted_json_str = pprint.pformat(ordering.text)
    print(ordering.request.body)
    print(ordering, formatted_json_str, sep='\n\n')
    assert "\"Номер карты Много.Ру должен состоять из восьми цифр\"" in ordering.text
    assert ordering.status_code == 400

















