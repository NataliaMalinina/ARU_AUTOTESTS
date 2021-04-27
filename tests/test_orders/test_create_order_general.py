import pprint
from json import loads
from random import choice
from model import parameters


def test_general_order_create(app):
    put_the_item_in_the_cart = app.order_fixture.cart(dataset=app.order_fixture.generate_payload(3),                    #TODO надо дружиться с бд и делать выборку товаров оттуда. + написать тест на удаление заказа - дергая из бд id заказа, что бы получить 400 с текстами - уже выкуплен и уже удалён
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

    ordering = app.order_fixture.create_order(email='nat19@yandex.ru', needEmail=False, needCall=False,
                                       mnogoRuCardId=None, head=app.token_autorization())
    formatted_json_str = pprint.pformat(ordering.text)
    print(ordering.request.body)
    print(ordering, formatted_json_str, sep='\n\n')
    while ordering.status_code == 400 and "\"Минимальная сумма заказа =" in ordering.text:
        put_the_item_in_the_cart = app.order_fixture.cart(dataset=app.order_fixture.generate_payload(3),
                                                          head=app.token_autorization())
        assert "\"tradeName\"" in put_the_item_in_the_cart.text
        assert put_the_item_in_the_cart.status_code == 200
        ordering = app.order_fixture.create_order(email='nat19@yandex.ru', needEmail=False, needCall=False,
                                                  mnogoRuCardId=None, head=app.token_autorization())
        print(ordering, formatted_json_str, sep='\n\n')
        if ordering.status_code == 200:
            break
    assert "\"orderId\"" in ordering.text
    assert "\"orderNum\"" in ordering.text


def test_order_cancel(app):
    order_id = app.order_fixture.id_order_from_list(head=app.token_autorization())
    delete_order = app.order_fixture.delete_order(orderId=order_id, head=app.token_autorization())
    formatted_json_str = pprint.pformat(delete_order.text)
    print(delete_order, formatted_json_str, sep='\n\n')
    while "\"Заказ уже выкуплен.\"" in delete_order.text or "\"Заказ уже удален\"" in delete_order.text:
        order_id = app.order_fixture.id_order_from_list(head=app.token_autorization())
        delete_order = app.order_fixture.delete_order(orderId=order_id, head=app.token_autorization())
        if delete_order.status_code == 200:
            break
    assert delete_order.status_code == 200


def test_order_repeat(app):
    orderId = app.order_fixture.id_order_from_list(head=app.token_autorization())
    repeat_order = app.order_fixture.repeat_order(head=app.token_autorization(), orderId=orderId)
    ordering = app.order_fixture.create_order(email='nat19@yandex.ru', needEmail=False, needCall=False,
                                       mnogoRuCardId=None, head=app.token_autorization())
    formatted_json_str = pprint.pformat(ordering.text)
    print(ordering.request.body)
    print(ordering, formatted_json_str, sep='\n\n')

    while "\"Минимальная сумма заказа =" in ordering.text:
        put_the_item_in_the_cart = app.order_fixture.cart(dataset=app.order_fixture.generate_payload(2),
                                                          head=app.token_autorization())
        ordering2 = app.order_fixture.create_order(email='nat19@yandex.ru', needEmail=False, needCall=False,
                                                  mnogoRuCardId=None, head=app.token_autorization())
        if ordering2.status_code == 200:
            break


def test_take_from_deferred(app):
    deffered_item = app.order_fixture.cart(dataset=app.order_fixture.generate_payload(3, True),
                                                      head=app.token_autorization())
    formatted_json_str = pprint.pformat(deffered_item.text)
    print(deffered_item.request.body)
    print(deffered_item, formatted_json_str, sep='\n\n')
    assert "\"tradeName\"" in deffered_item.text
    assert deffered_item.status_code == 200

    choice_autodest_before_order = app.choice_autodest_auth_user(id=choice(parameters.autodestid_for_order),
                                                                 head=app.token_autorization())
    print(choice_autodest_before_order.request.body)
    print(choice_autodest_before_order, formatted_json_str, sep='\n\n')
    assert choice_autodest_before_order.status_code == 200

    put_the_item_in_cart = app.order_fixture.cart(dataset=app.order_fixture.item_in_cart(cart=app.order_fixture.cart(head=app.token_autorization(), dataset=deffered_item)), head=app.token_autorization())

    ordering = app.order_fixture.create_order(email='nat19@yandex.ru', needEmail=False, needCall=False,
                                              mnogoRuCardId=None, head=app.token_autorization())
    formatted_json_str = pprint.pformat(ordering.text)
    print(ordering.request.body)
    print(ordering, formatted_json_str, sep='\n\n')
    while ordering.status_code == 400 and "\"Минимальная сумма заказа =\"" in ordering.text:
        deffered_item = app.order_fixture.cart(dataset=app.order_fixture.generate_payload(3, True),
                                                          head=app.token_autorization())
        assert "\"tradeName\"" in deffered_item.text
        assert deffered_item.status_code == 200
        ordering = app.order_fixture.create_order(email='nat19@yandex.ru', needEmail=False, needCall=False,
                                                  mnogoRuCardId=None, head=app.token_autorization())
        print(ordering, formatted_json_str, sep='\n\n')
        if ordering.status_code == 200:
            break
    assert "\"orderId\"" in ordering.text
    assert "\"orderNum\"" in ordering.text

# SU

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

    ordering = app.order_fixture.create_order_su(email='nat19@yandex.ru', needEmail=False, needCall=False,
                                       mnogoRuCardId=None, head=app.token_auth_admin_user(), userId='5ee852c50521b00001edffed')
    formatted_json_str = pprint.pformat(ordering.text)
    print(ordering.request.body)
    print(ordering, formatted_json_str, sep='\n\n')
    while ordering.status_code == 400 and "\"Минимальная сумма заказа =" in ordering.text:
        put_the_item_in_the_cart = app.order_fixture.cart(dataset=app.order_fixture.generate_payload(3),
                                                          head=app.token_autorization())
        assert "\"tradeName\"" in put_the_item_in_the_cart.text
        assert put_the_item_in_the_cart.status_code == 200
        ordering = app.order_fixture.create_order(email='nat19@yandex.ru', needEmail=False, needCall=False,
                                                  mnogoRuCardId=None, head=app.token_autorization())
        print(ordering, formatted_json_str, sep='\n\n')
        if ordering.status_code == 200:
            break
    assert "\"orderId\"" in ordering.text
    assert "\"orderNum\"" in ordering.text


def test_edit_order_su(app):
    blocking_order = app.order_fixture.order_block_su(head=app.token_auth_admin_user(),
                                                      orderId=app.order_fixture.id_order_for_su(head=app.token_auth_admin_user()))
    formatted_json_str = pprint.pformat(blocking_order.text)
    print(blocking_order.request.body)
    print(blocking_order, formatted_json_str, sep='\n\n')
    while blocking_order.status_code == 400 and "\"Заказ уже удален\"" in blocking_order.text:
        blocking_order = app.order_fixture.order_block_su(head=app.token_auth_admin_user(),
                                        orderId=app.order_fixture.id_order_for_su(head=app.token_auth_admin_user()))
        if blocking_order.status_code == 200 or "\"Блокировка на данный заказ уже установлена\"" in blocking_order.text:
            break

    id = loads(blocking_order.request.body)['orderId']

    edit_order_su = app.order_fixture.edit_order_su(head=app.token_auth_admin_user(),
                                                    orderId=id, dataset=app.order_fixture.generate_payload(2),
                                                    dryRun=True)
    formatted_json_str = pprint.pformat(edit_order_su.text)
    print(edit_order_su.request.body)
    print(edit_order_su, formatted_json_str, sep='\n\n')

    while edit_order_su.status_code == 400 and "\"Минимальная сумма заказа =\"" in edit_order_su.text:
        edit_order_su = app.order_fixture.edit_order_su(head=app.token_auth_admin_user(),
                                                        orderId=id, dataset=app.order_fixture.generate_payload(2),
                                                        dryRun=True)

        if edit_order_su.status_code == 200:
            break

    edit_order_su = app.order_fixture.edit_order_su(head=app.token_auth_admin_user(),
                                                    orderId=id, dataset=app.order_fixture.generate_payload(2),
                                                    dryRun=False)

    while edit_order_su.status_code == 400 and "\"Минимальная сумма заказа =\"" in edit_order_su.text:
        edit_order_su = app.order_fixture.edit_order_su(head=app.token_auth_admin_user(),
                                                        orderId=id, dataset=app.order_fixture.generate_payload(2),
                                                        dryRun=False)
        if blocking_order.status_code == 200:
            break

    formatted_json_str = pprint.pformat(edit_order_su.text)
    print(edit_order_su.request.body)
    print(edit_order_su, formatted_json_str, sep='\n\n')


def test_cancel_order_su(app):
    orderId = app.order_fixture.id_order_for_su(head=app.token_auth_admin_user())
    delete_order_su = app.order_fixture.delete_order_su(orderId=orderId, head=app.token_auth_admin_user())
    formatted_json_str = pprint.pformat(delete_order_su.text)
    print(delete_order_su.request.body)
    print(delete_order_su, formatted_json_str, sep='\n\n')
    while delete_order_su.status_code == 400 and "\"Заказ уже удален\"" in delete_order_su.text:
        orderId = app.order_fixture.id_order_for_su(head=app.token_auth_admin_user())
        delete_order = app.order_fixture.delete_order_su(orderId=orderId, head=app.token_auth_admin_user())
        if delete_order.status_code == 200:
            break


def test_order_repeat_su(app):
    orderId = app.order_fixture.id_order_for_su(head=app.token_auth_admin_user())
    repeat_order = app.order_fixture.repeat_order_su(head=app.token_auth_admin_user(), orderId=orderId)
    ordering = app.order_fixture.create_order_su(email='nat19@yandex.ru', needEmail=False, needCall=False,
                                       mnogoRuCardId=None, head=app.token_auth_admin_user(), userId='5ee852c50521b00001edffed')
    formatted_json_str = pprint.pformat(ordering.text)
    print(ordering.request.body)
    print(ordering, formatted_json_str, sep='\n\n')

    while "\"Минимальная сумма заказа =\"" in ordering.text:
        put_the_item_in_the_cart = app.order_fixture.cart(dataset=app.order_fixture.generate_payload(2),
                                                          head=app.token_autorization())
        ordering2 = app.order_fixture.create_order(email='nat19@yandex.ru', needEmail=False, needCall=False,
                                                  mnogoRuCardId=None, head=app.token_autorization())
        if ordering2.status_code == 200:
            break

















