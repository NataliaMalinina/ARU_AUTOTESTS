import pprint
from json import loads
from random import choice
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


#Error


def test_not_found_promocode(app):
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

    use_promocode = app.order_fixture.cart_use_promocode(promoCode="999gfjgf", head=app.token_autorization())

    formatted_json_str = pprint.pformat(use_promocode.text)
    print(use_promocode.request.body)
    print(use_promocode, formatted_json_str, sep='\n\n')
    assert 'Указаный промо-код не найден' in use_promocode.text
    assert use_promocode.status_code == 404


def test_already_used_promocode(app):
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

    use_promocode = app.order_fixture.cart_use_promocode(promoCode="RIGA1", head=app.token_autorization())

    formatted_json_str = pprint.pformat(use_promocode.text)
    print(use_promocode.request.body)
    print(use_promocode, formatted_json_str, sep='\n\n')
    assert loads(use_promocode.text)['promoCodes'][0]['isUsed'] == False
    assert 'Промокод уже был использован' in use_promocode.text
    assert use_promocode.status_code == 200

    delete_promocode = app.order_fixture.delete_promocode_from_the_cart(promoCode='RIGA1',
                                                                        head=app.token_autorization())
    assert delete_promocode.status_code == 200


def test_promocode_is_not_valid_yet(app):
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

    use_promocode = app.order_fixture.cart_use_promocode(promoCode="MSKAPTEKA", head=app.token_autorization())

    formatted_json_str = pprint.pformat(use_promocode.text)
    print(use_promocode.request.body)
    print(use_promocode, formatted_json_str, sep='\n\n')
    assert loads(use_promocode.text)['promoCodes'][0]['isUsed'] == False
    assert 'Промо-код еще не действует' in use_promocode.text
    assert use_promocode.status_code == 200

    delete_promocode = app.order_fixture.delete_promocode_from_the_cart(promoCode='MSKAPTEKA',
                                                                        head=app.token_autorization())
    assert delete_promocode.status_code == 200


def test_promocode_already_not_valid(app):
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

    use_promocode = app.order_fixture.cart_use_promocode(promoCode="LEO2O15", head=app.token_autorization())

    formatted_json_str = pprint.pformat(use_promocode.text)
    print(use_promocode.request.body)
    print(use_promocode, formatted_json_str, sep='\n\n')
    assert loads(use_promocode.text)['promoCodes'][0]['isUsed'] == False
    assert 'Промо-код уже не действует' in use_promocode.text
    assert use_promocode.status_code == 200

    delete_promocode = app.order_fixture.delete_promocode_from_the_cart(promoCode='LEO2O15',
                                                                        head=app.token_autorization())
    assert delete_promocode.status_code == 200


def test_promocode_in_cart_two_times(app):
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

    use_promocode = app.order_fixture.cart_use_promocode(promoCode="RIGA2", head=app.token_autorization())

    formatted_json_str = pprint.pformat(use_promocode.text)
    print(use_promocode.request.body)
    print(use_promocode, formatted_json_str, sep='\n\n')
    assert 'Промо-код уже был добавлен в корзину' in use_promocode.text
    assert use_promocode.status_code == 409

    delete_promocode = app.order_fixture.delete_promocode_from_the_cart(promoCode='RIGA2',
                                                                        head=app.token_autorization())
    assert delete_promocode.status_code == 200


def test_delete_promocode_two_times(app):
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

    delete_promocode = app.order_fixture.delete_promocode_from_the_cart(promoCode='RIGA2',
                                                                        head=app.token_autorization())
    assert delete_promocode.status_code == 404
    assert '\"Указанный промо-код не обнаружен в корзине\"' in delete_promocode.text
    cart = app.order_fixture.get_cart_user(head=app.token_autorization())
    formatted_json_str = pprint.pformat(cart.text)
    print(cart.request.body)
    print(cart, formatted_json_str, sep='\n\n')
    assert len(loads(cart.text)['promoCodes']) == 0


def test_put_promocode_in_empty_cart(app):
    cart = app.order_fixture.get_cart_user(head=app.token_autorization())
    cart_json = loads(cart.text)
    replace_deferred_items = cart_json['items']
    for item in replace_deferred_items:
        item['amount'] = 0

    cart = app.order_fixture.cart(dataset=replace_deferred_items, head=app.token_autorization())
    use_promocode = app.order_fixture.cart_use_promocode(promoCode="RIGA2", head=app.token_autorization())

    formatted_json_str = pprint.pformat(use_promocode.text)
    print(use_promocode.request.body)
    print(use_promocode, formatted_json_str, sep='\n\n')
    assert loads(use_promocode.text)['promoCodes'][0]['hint'] == 'Промо-код не дает наилучшую скидку по данной корзине'
    assert loads(use_promocode.text)['promoCodes'][0]['isUsed'] == False
    assert use_promocode.status_code == 200

    delete_promocode = app.order_fixture.delete_promocode_from_the_cart(promoCode='RIGA2',
                                                                        head=app.token_autorization())
    assert delete_promocode.status_code == 200


def test_use_two_promocode_with_similar_discount(app):
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

    use_promocode2 = app.order_fixture.cart_use_promocode(promoCode="999999", head=app.token_autorization())
    formatted_json_str = pprint.pformat(use_promocode2.text)
    print(use_promocode2.request.body)
    print(use_promocode2, formatted_json_str, sep='\n\n')
    assert loads(use_promocode2.text)['promoCodes'][1]['hint'] == 'Промо-код не дает наилучшую скидку по данной корзине'
    assert loads(use_promocode2.text)['promoCodes'][1]['isUsed'] == False
    assert use_promocode2.status_code == 200

    delete_promocode = app.order_fixture.delete_promocode_from_the_cart(promoCode='RIGA2',
                                                                        head=app.token_autorization())
    assert delete_promocode.status_code == 200

    delete_promocode = app.order_fixture.delete_promocode_from_the_cart(promoCode='999999',
                                                                        head=app.token_autorization())
    assert delete_promocode.status_code == 200


def test_use_two_promocode_with_different_discount_first_is_less(app):
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

    sleep(2)
    use_promocode2 = app.order_fixture.cart_use_promocode(promoCode="LEO2O15", head=app.token_autorization())
    formatted_json_str = pprint.pformat(use_promocode2.text)
    print(use_promocode2.request.body)
    print(use_promocode2, formatted_json_str, sep='\n\n')
    assert loads(use_promocode2.text)['promoCodes'][0]['hint'] == 'Промо-код не дает наилучшую скидку по данной корзине'
    assert loads(use_promocode2.text)['promoCodes'][0]['isUsed'] == False
    assert use_promocode2.status_code == 200
    assert loads(use_promocode2.text)['promoCodes'][1]['isUsed'] == True
    assert use_promocode2.status_code == 200

    delete_promocode = app.order_fixture.delete_promocode_from_the_cart(promoCode='RIGA2',
                                                                        head=app.token_autorization())
    assert delete_promocode.status_code == 200

    delete_promocode = app.order_fixture.delete_promocode_from_the_cart(promoCode='LEO2O15',
                                                                        head=app.token_autorization())
    assert delete_promocode.status_code == 200


def test_use_two_promocode_with_different_discount_first_is_more_expensive(app):
    use_promocode = app.order_fixture.cart_use_promocode(promoCode="LEO2O15", head=app.token_autorization())

    formatted_json_str = pprint.pformat(use_promocode.text)
    print(use_promocode.request.body)
    print(use_promocode, formatted_json_str, sep='\n\n')
    assert loads(use_promocode.text)['promoCodes'][0]['isUsed'] == True
    assert use_promocode.status_code == 200

    sleep(2)
    use_promocode2 = app.order_fixture.cart_use_promocode(promoCode="RIGA2", head=app.token_autorization())
    formatted_json_str = pprint.pformat(use_promocode2.text)
    print(use_promocode2.request.body)
    print(use_promocode2, formatted_json_str, sep='\n\n')
    assert loads(use_promocode2.text)['promoCodes'][1]['hint'] == 'Промо-код не дает наилучшую скидку по данной корзине'
    assert loads(use_promocode2.text)['promoCodes'][1]['isUsed'] == False
    assert use_promocode2.status_code == 200
    assert loads(use_promocode2.text)['promoCodes'][0]['isUsed'] == True
    assert use_promocode2.status_code == 200

    delete_promocode = app.order_fixture.delete_promocode_from_the_cart(promoCode='RIGA2',
                                                                        head=app.token_autorization())
    assert delete_promocode.status_code == 200

    delete_promocode = app.order_fixture.delete_promocode_from_the_cart(promoCode='LEO2O15',
                                                                        head=app.token_autorization())
    assert delete_promocode.status_code == 200


#Sber Promo


def test_promocode_sber_100(app):
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

    use_promocode = app.order_fixture.cart_use_promocode(promoCode="DLIYAVTOTESTOV10O", head=app.token_autorization())

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


def test_promocode_sber_250(app):
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

    use_promocode = app.order_fixture.cart_use_promocode(promoCode="DLIYAVTOTESTOV25O", head=app.token_autorization())

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


def test_promocode_sber_500(app):
    put_the_item_in_the_cart = app.order_fixture.cart(dataset=app.order_fixture.generate_payload(2),
                                                      head=app.token_autorization())
    formatted_json_str = pprint.pformat(put_the_item_in_the_cart.text)
    print(put_the_item_in_the_cart.request.body)
    print(put_the_item_in_the_cart, formatted_json_str, sep='\n\n')
    while loads(put_the_item_in_the_cart.text)['totalSum'] < 1000:
        put_the_item_in_the_cart = app.order_fixture.cart \
            (dataset=app.order_fixture.generate_payload(2), head=app.token_autorization())
        if loads(put_the_item_in_the_cart.text)['totalSum'] >= 1000:
            break
    assert "\"tradeName\"" in put_the_item_in_the_cart.text
    assert put_the_item_in_the_cart.status_code == 200

    use_promocode = app.order_fixture.cart_use_promocode(promoCode="DLIYAVTOTESTOV50O", head=app.token_autorization())

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


def test_promocode_sber_reuse_100(app):
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

    use_promocode = app.order_fixture.cart_use_promocode(promoCode="DLIYAVTOTESTOV10O", head=app.token_autorization())

    formatted_json_str = pprint.pformat(use_promocode.text)
    print(use_promocode.request.body)
    print(use_promocode, formatted_json_str, sep='\n\n')
    assert 'Промокод уже был использован' in use_promocode.text
    assert use_promocode.status_code == 200

    delete_promocode = app.order_fixture.delete_promocode_from_the_cart(promoCode='DLIYAVTOTESTOV10O',
                                                                        head=app.token_autorization())
    assert delete_promocode.status_code == 200


#def test_use_promocode_100_but_summ_order_not_200(app):




#SU

def test_su_use_promocode_for_user(app):
    put_the_item_in_the_cart = app.order_fixture.cart(dataset=app.order_fixture.generate_payload(2),
                                                      head=app.token_auth_super_user(),
                                                      userId='5ee852c50521b00001edffed')
    formatted_json_str = pprint.pformat(put_the_item_in_the_cart.text)
    print(put_the_item_in_the_cart.request.body)
    print(put_the_item_in_the_cart, formatted_json_str, sep='\n\n')
    while loads(put_the_item_in_the_cart.text)['totalSum'] < 500:
        put_the_item_in_the_cart = app.order_fixture.cart \
            (dataset=app.order_fixture.generate_payload(2), head=app.token_auth_super_user(),
                                                      userId='5ee852c50521b00001edffed')
        if loads(put_the_item_in_the_cart.text)['totalSum'] >= 500:
            break
    assert "\"tradeName\"" in put_the_item_in_the_cart.text
    assert put_the_item_in_the_cart.status_code == 200

    choice_autodest_before_order = app.choice_autodest(id=choice(parameters.autodestid_for_order),
                                                       head=app.token_auth_super_user(),
                                                       userId='5ee852c50521b00001edffed')
    print(choice_autodest_before_order.request.body)
    print(choice_autodest_before_order, formatted_json_str, sep='\n\n')
    assert choice_autodest_before_order.status_code == 200

    use_promocode = app.order_fixture.cart_use_promocode(promoCode="RIGA2", head=app.token_auth_super_user(),
                                                       userId='5ee852c50521b00001edffed')

    formatted_json_str = pprint.pformat(use_promocode.text)
    print(use_promocode.request.body)
    print(use_promocode, formatted_json_str, sep='\n\n')
    assert loads(use_promocode.text)['promoCodes'][0]['isUsed'] == True
    assert use_promocode.status_code == 200

    ordering = app.order_fixture.create_order(email='nat19@yandex.ru', needEmail=False, needCall=False,
                                              mnogoRuCardId=None,
                                              head=app.token_auth_super_user(),
                                              userId='5ee852c50521b00001edffed')
    formatted_json_str = pprint.pformat(ordering.text)
    print(ordering.request.body)
    print(ordering, formatted_json_str, sep='\n\n')
    assert "\"orderId\"" in ordering.text
    assert "\"orderNum\"" in ordering.text
    assert len(loads(ordering.text)['order']['promoCodes']) != 0


def test_su_delete_promocode_for_user(app):
    put_the_item_in_the_cart = app.order_fixture.cart(dataset=app.order_fixture.generate_payload(2),
                                                      head=app.token_auth_super_user(),
                                                      userId='5ee852c50521b00001edffed')
    formatted_json_str = pprint.pformat(put_the_item_in_the_cart.text)
    print(put_the_item_in_the_cart.request.body)
    print(put_the_item_in_the_cart, formatted_json_str, sep='\n\n')
    while loads(put_the_item_in_the_cart.text)['totalSum'] < 500:
        put_the_item_in_the_cart = app.order_fixture.cart \
            (dataset=app.order_fixture.generate_payload(2), head=app.token_auth_super_user(),
                                                      userId='5ee852c50521b00001edffed')
        if loads(put_the_item_in_the_cart.text)['totalSum'] >= 500:
            break
    assert "\"tradeName\"" in put_the_item_in_the_cart.text
    assert put_the_item_in_the_cart.status_code == 200

    choice_autodest_before_order = app.choice_autodest(id=choice(parameters.autodestid_for_order),
                                                       head=app.token_auth_super_user(),
                                                       userId='5ee852c50521b00001edffed')
    print(choice_autodest_before_order.request.body)
    print(choice_autodest_before_order, formatted_json_str, sep='\n\n')
    assert choice_autodest_before_order.status_code == 200

    use_promocode = app.order_fixture.cart_use_promocode(promoCode='RIGA2', head=app.token_auth_super_user(),
                                                      userId='5ee852c50521b00001edffed')

    formatted_json_str = pprint.pformat(use_promocode.text)
    print(use_promocode.request.body)
    print(use_promocode, formatted_json_str, sep='\n\n')
    assert loads(use_promocode.text)['promoCodes'][0]['isUsed'] == True
    assert use_promocode.status_code == 200

    delete_promocode = app.order_fixture.delete_promocode_from_the_cart(promoCode='RIGA2',
                                                                        head=app.token_auth_super_user(),
                                                                        userId='5ee852c50521b00001edffed')
    assert delete_promocode.status_code == 200

    ordering = app.order_fixture.create_order(email='nat19@yandex.ru', needEmail=False, needCall=False,
                                              mnogoRuCardId=None,
                                              head=app.token_auth_super_user(),
                                              userId='5ee852c50521b00001edffed')
    formatted_json_str = pprint.pformat(ordering.text)
    print(ordering.request.body)
    print(ordering, formatted_json_str, sep='\n\n')
    assert "\"orderId\"" in ordering.text
    assert "\"orderNum\"" in ordering.text
    assert len(loads(ordering.text)['order']['promoCodes']) == 0








