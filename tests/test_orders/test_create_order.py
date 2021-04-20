import pprint


def test_order_create(app):
    put_the_item_in_the_cart = app.order_fixture.cart(2, itemId=['5d6500842fd44a0001b0d999', '5d650d4d2fd44a0001b16943'], amount=[1, 1],
                                                      deferred=[False, False],
                                                      head=app.token_autorization())
    formatted_json_str = pprint.pformat(put_the_item_in_the_cart.text)
    print(put_the_item_in_the_cart.request.body)
    print(put_the_item_in_the_cart, formatted_json_str, sep='\n\n')
    assert "\"tradeName\"" in put_the_item_in_the_cart.text
    ordering = app.order_fixture.order(email='nat19@yandex.ru', head=app.token_autorization())





