import pprint
from json import loads
from random import choice
from model import parameters

def test_migration_shadow_user_to_auth_user_city(app):
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
