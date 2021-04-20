import pprint
from random import choice
from model import parameters


def test_order_create(app):
    put_the_item_in_the_cart = app.order_fixture.cart(dataset=app.order_fixture.generate_payload(2),
                                                      head=app.token_autorization())
    formatted_json_str = pprint.pformat(put_the_item_in_the_cart.text)
    print(put_the_item_in_the_cart.request.body)
    print(put_the_item_in_the_cart, formatted_json_str, sep='\n\n')
    assert "\"tradeName\"" in put_the_item_in_the_cart.text
    # choice_autodest_before_order = app.choice_autodest(id=choice(parameters.autodestid_for_order))
    # print(choice_autodest_before_order.request.body)
    # print(choice_autodest_before_order, formatted_json_str, sep='\n\n')
    ordering = app.order_fixture.order(email='nat19@yandex.ru', needEmail=False, needCall=False, customName=None,
                                       mnogoRuCardId=None, head=app.token_autorization())
    formatted_json_str = pprint.pformat(ordering.text)
    print(ordering.request.body)
    print(ordering, formatted_json_str, sep='\n\n')
    assert "\"orderId\"" in ordering.text
    assert "\"orderNum\"" in ordering.text





