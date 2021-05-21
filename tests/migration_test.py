import pprint
from json import loads
from random import choice
from model import parameters


def test_migration_shadow_user_to_auth_user_city(app):
    auth_user = app.auth(phone='+79139519213', code='9213')
    choice_city = app.choice_city(id='5e574665ddc33b0001041fc7', manualChange=True, head=app.token_autorization())

    cityid = choice(parameters.cityid)
    choice_city = app.choice_city_shadow_user(id=cityid, manualChange=True)
    formatted_json_str = pprint.pformat(choice_city.text)
    print(choice_city.url, formatted_json_str, sep='\n\n')
    while cityid == '5e574663b1585900015ed444':
        assert "\"Указан некорректный Id города (Parameter \'cityId\')\"" in choice_city.text
    if cityid != '5e574663b1585900015ed444':
        assert choice_city.status_code == 200

    access_token = choice_city.headers['X-Shadowuser']
    auth_user = app.auth_for_migration(code='9213', phone='+79139519213', access_token=access_token)
    user_preferences = app.user_preferences(head=app.token_autorization())
    assert auth_user.status_code == 200
    assert "\"token\":" in auth_user.text
    assert loads(user_preferences.text)['selectedCity']['id'] == cityid


def test_migration_shadow_user_to_auth_user_autodest(app):
    choice_autodest = app.choice_autodest(id='5d65561426306f000138b01b',
                                          head=app.token_autorization())
    formatted_json_str = pprint.pformat(choice_autodest.text)
    print(choice_autodest.url, formatted_json_str, sep='\n\n')
    assert choice_autodest.status_code == 200

    autodest_info = app.autodest_info(autoDestId=choice(parameters.autodestid_for_order))
    choice_autodest_id = loads(autodest_info.text)['id']
    choice_autodest = app.choice_autodest_shadow_user(id=choice_autodest_id)
    formatted_json_str = pprint.pformat(choice_autodest.text)
    print(choice_autodest.request.body)
    print(choice_autodest.url, formatted_json_str, sep='\n\n')
    assert choice_autodest.status_code == 200

    access_token = choice_autodest.headers['X-Shadowuser']
    auth_user = app.auth_for_migration(code='9213', phone='+79139519213', access_token=access_token)
    user_preferences = app.user_preferences(head=app.token_autorization())
    assert auth_user.status_code == 200
    assert "\"token\":" in auth_user.text
    assert loads(user_preferences.text)['selectedAutoDest']['id'] == choice_autodest_id


def test_migration_shadow_user_have_goods_to_auth_user_cart_not_have_any_good(app):
    cart = app.order_fixture.get_cart_user(head=app.token_autorization())
    cart_json = loads(cart.text)
    items = cart_json['items']
    for item in items:
        item['amount'] = 0
    cart = app.order_fixture.cart(head=app.token_autorization(), dataset=items)

    token_shadow_user = app.token_shadow_user()

    put_the_item_in_the_cart_shadow_user = app.order_fixture.cart(head=token_shadow_user, dataset=app.order_fixture.generate_payload(2))

    formatted_json_str = pprint.pformat(put_the_item_in_the_cart_shadow_user.text)
    print(put_the_item_in_the_cart_shadow_user.request.body)
    print(put_the_item_in_the_cart_shadow_user.url, formatted_json_str, sep='\n\n')
    assert put_the_item_in_the_cart_shadow_user.status_code == 200

    auth_user = app.auth_for_migration(code='9213', phone='+79139519213', access_token=token_shadow_user)
    token_autn_user = loads(auth_user.text)['token']
    assert auth_user.status_code == 200
    assert "\"token\":" in auth_user.text

    cart_auth_user = app.order_fixture.get_cart_user(head={'Authorization': 'Bearer {}'.format(token_autn_user)})
    formatted_json_str = pprint.pformat(cart_auth_user.text)
    print(cart_auth_user.request.body)
    print(cart_auth_user.url, formatted_json_str, sep='\n\n')
    assert cart_auth_user.status_code == 200
    assert loads(cart_auth_user.text)['items'] == loads(put_the_item_in_the_cart_shadow_user.text)['items']

















