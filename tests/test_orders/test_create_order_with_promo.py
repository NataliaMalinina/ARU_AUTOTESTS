import pprint
from json import loads
from random import randrange, choice
from model import parameters
from time import sleep


def test_order_with_promocode_onceonly_true_unlimited_false(app):  #TODO чтобы полноценно выполнять тест нужна интеграция с БД для удаления Used в промокоде после прохождения теста

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
        put_the_item_in_the_cart = app.order_fixture.cart\
            (dataset=app.order_fixture.generate_payload(2), head=app.token_autorization())
        if loads(put_the_item_in_the_cart.text)['totalSum'] >= 500:
            break
    assert "\"tradeName\"" in put_the_item_in_the_cart.text
    assert put_the_item_in_the_cart.status_code == 200

    use_promocode = app.order_fixture.cart_use_promocode(promoCode="RIGA1", head=app.token_autorization())
    formatted_json_str = pprint.pformat(use_promocode.text)
    print(use_promocode.request.body)
    print(use_promocode, formatted_json_str, sep='\n\n')
    if loads(use_promocode.text)['promoCodes'][0]['isUsed'] == False:
        print('У промокода не очищен массив isUsedSynonyms')
    else:
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


def test_order_with_promocode_onceonly_false_unlimited_true(app):
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

    use_promocode = app.order_fixture.cart_use_promocode(promoCode="RIGA2", head=app.token_autorization())

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


def test_order_with_promocode_onceonly_true_unlimited_true(app):
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

    use_promocode = app.order_fixture.cart_use_promocode(promoCode="RIGA3", head=app.token_autorization())
    formatted_json_str = pprint.pformat(use_promocode.text)
    print(use_promocode.request.body)
    print(use_promocode, formatted_json_str, sep='\n\n')
    if loads(use_promocode.text)['promoCodes'][0]['isUsed'] == False:
        print('У промокода не очищен массив isUsedSynonyms')
    else:
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


def test_order_with_promocode_onceonly_false_unlimited_false(app):
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

    use_promocode = app.order_fixture.cart_use_promocode(promoCode="RIGA4", head=app.token_autorization())
    formatted_json_str = pprint.pformat(use_promocode.text)
    print(use_promocode.request.body)
    print(use_promocode, formatted_json_str, sep='\n\n')
    if loads(use_promocode.text)['promoCodes'][0]['isUsed'] == False:
        print('У промокода не очищен массив isUsedSynonyms')
    else:
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


def test_delete_promocode_from_the_cart(app):
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

    delete_promocode = app.order_fixture.delete_promocode_from_the_cart(promoCode='RIGA2',
                                                                        head=app.token_autorization())
    assert delete_promocode.status_code == 200
    cart = app.order_fixture.get_cart_user(head=app.token_autorization())
    formatted_json_str = pprint.pformat(cart.text)
    print(cart.request.body)
    print(cart, formatted_json_str, sep='\n\n')
    assert len(loads(cart.text)['promoCodes']) == 0


def test_promocode_doesnt_give_the_best_discount_in_cart(app):
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

    use_promocode = app.order_fixture.cart_use_promocode(promoCode="RIGA2", head=app.token_autorization())
    formatted_json_str = pprint.pformat(use_promocode.text)
    print(use_promocode.request.body)
    print(use_promocode, formatted_json_str, sep='\n\n')

    use_promocode2 = app.order_fixture.cart_use_promocode(promoCode="VATUTINA", head=app.token_autorization())
    formatted_json_str = pprint.pformat(use_promocode2.text)
    print(use_promocode2.request.body)
    print(use_promocode2, formatted_json_str, sep='\n\n')
    assert loads(use_promocode2.text)['promoCodes'][0]['hint'] == 'Промо-код не дает наилучшую скидку по данной корзине'
    assert loads(use_promocode2.text)['promoCodes'][1]['hint'] == 'Промо-код применен'
    assert use_promocode.status_code == 200

    delete_first_promocode = app.order_fixture.delete_promocode_from_the_cart(promoCode='RIGA2',
                                                                              head=app.token_autorization())
    delete_second_promocode = app.order_fixture.delete_promocode_from_the_cart(promoCode='VATUTINA',
                                                                         head=app.token_autorization())
    cart = app.order_fixture.get_cart_user(head=app.token_autorization())


def test_cancel_order_with_promocode(app):
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

    use_promocode = app.order_fixture.cart_use_promocode(promoCode='TANGO', head=app.token_autorization())

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

    cancel_order = app.order_fixture.delete_order(orderId=loads(ordering.text)['orderId'],
                                                  head=app.token_autorization())
    formatted_json_str = pprint.pformat(cancel_order.text)
    print(cancel_order.request.body)
    print(cancel_order, formatted_json_str, sep='\n\n')
    assert cancel_order.status_code == 200

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

    sleep(5)
    use_promocode = app.order_fixture.cart_use_promocode(promoCode='TANGO', head=app.token_autorization())
    formatted_json_str = pprint.pformat(use_promocode.text)
    print(use_promocode.request.body)
    print(use_promocode, formatted_json_str, sep='\n\n')
    assert loads(use_promocode.text)['promoCodes'][0]['isUsed'] == True
    assert use_promocode.status_code == 200

    delete_promocode = app.order_fixture.delete_promocode_from_the_cart(promoCode='TANGO',
                                                                        head=app.token_autorization())
    assert delete_promocode.status_code == 200















