import pprint
from json import loads
from model import parameters
from random import choice

# TODO: подружить с монгой, взять id городов из монги, для чистоты теста, чтобы данные не были захардкожены


def test_choice_city(app):
    cityid = choice(parameters.cityid)
    choice_city = app.choice_city_shadow_user(id=cityid, manualChange=True)
    formatted_json_str = pprint.pformat(choice_city.text)
    print(choice_city.url, formatted_json_str, sep='\n\n')
    if cityid == '5e574663b1585900015ed444':
        assert "\"Указан некорректный Id города (Parameter \'cityId\')\"" in choice_city.text
    else:
        assert choice_city.status_code == 200


def test_choice_city_auth_user(app):
    cityid = choice(parameters.cityid)
    choice_city = app.choice_city(id=cityid, manualChange=True, head=app.token_autorization())
    formatted_json_str = pprint.pformat(choice_city.text)
    print(choice_city.url, formatted_json_str, sep='\n\n')
    if cityid == '5e574663b1585900015ed444':
        assert "\"Указан некорректный Id города (Parameter \'cityId\')\"" in choice_city.text
    else:
        assert choice_city.status_code == 200


def test_choice_city_admin_user(app):
    choice_city = app.choice_city(id='5e574663f4d315000196b176', manualChange=True,
                                        userId='5ee852c50521b00001edffed', head=app.token_auth_super_user())
    formatted_json_str = pprint.pformat(choice_city.text)
    print(choice_city.url, formatted_json_str, sep='\n\n')
    assert choice_city.status_code == 200