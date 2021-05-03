import pprint
from random import choice
from model import parameters
from json import loads


def test_choice_autodest_without_mark_and_beznal_shadow_user(app):
    autodest_info = app.autodest_info(autoDestId=choice(parameters.autodestid_without_mark_and_bezn))
    formatted_json_str = pprint.pformat(autodest_info.text)
    print(autodest_info.url, formatted_json_str, sep='\n\n')
    assert "\"eDrug\":false" in autodest_info.text

    choice_autodest_id = loads(autodest_info.text)['id']
    choice_autodest = app.choice_autodest_shadow_user(id=choice_autodest_id)
    formatted_json_str = pprint.pformat(choice_autodest.text)
    print(choice_autodest.request.body)
    print(choice_autodest.url, formatted_json_str, sep='\n\n')
    assert choice_autodest.status_code == 200


def test_choice_autodest_with_mark_and_beznal_shadow_user(app):
    autodest_info = app.autodest_info(autoDestId=choice(parameters.autodestid_with_mark_and_bezn))
    formatted_json_str = pprint.pformat(autodest_info.text)
    print(autodest_info.url, formatted_json_str, sep='\n\n')
    assert "\"eDrug\":true" in autodest_info.text

    choice_autodest_id = loads(autodest_info.text)['id']
    choice_autodest = app.choice_autodest_shadow_user(id=choice_autodest_id)
    formatted_json_str = pprint.pformat(choice_autodest.text)
    print(choice_autodest.url, formatted_json_str, sep='\n\n')
    assert choice_autodest.status_code == 200


def test_choice_autodest_with_mark_without_beznal_shadow_user(app):
    autodest_info = app.autodest_info(autoDestId=choice(parameters.autodestid_with_mark_without_bezn))
    formatted_json_str = pprint.pformat(autodest_info.text)
    print(autodest_info.url, formatted_json_str, sep='\n\n')
    assert "\"eDrug\":true" in autodest_info.text

    choice_autodest_id = loads(autodest_info.text)['id']
    choice_autodest = app.choice_autodest_shadow_user(id=choice_autodest_id)
    formatted_json_str = pprint.pformat(choice_autodest.text)
    print(choice_autodest.url, formatted_json_str, sep='\n\n')
    assert choice_autodest.status_code == 200


def test_choice_autodest_without_mark_with_beznal_shadow_user(app):
    autodest_info = app.autodest_info(autoDestId=choice(parameters.autodestid_without_mark_with_beznal))
    formatted_json_str = pprint.pformat(autodest_info.text)
    print(autodest_info.url, formatted_json_str, sep='\n\n')
    assert "\"eDrug\":false" in autodest_info.text

    choice_autodest_id = loads(autodest_info.text)['id']
    choice_autodest = app.choice_autodest_shadow_user(id=choice_autodest_id)
    formatted_json_str = pprint.pformat(choice_autodest.text)
    print(choice_autodest.url, formatted_json_str, sep='\n\n')
    assert choice_autodest.status_code == 200


def test_choice_autodest_without_mark_and_beznal_auth_user(app):
    autodest_info = app.autodest_info(autoDestId=choice(parameters.autodestid_without_mark_and_bezn))
    formatted_json_str = pprint.pformat(autodest_info.text)
    print(autodest_info.url, formatted_json_str, sep='\n\n')
    assert "\"eDrug\":false" in autodest_info.text

    choice_autodest_id = loads(autodest_info.text)['id']
    choice_autodest = app.choice_autodest\
        (id=choice_autodest_id, head=app.token_autorization())
    formatted_json_str = pprint.pformat(choice_autodest.text)
    print(choice_autodest.url, formatted_json_str, sep='\n\n')
    assert choice_autodest.status_code == 200


def test_choice_autodest_with_mark_and_beznal_auth_user(app):
    autodest_info = app.autodest_info(autoDestId=choice(parameters.autodestid_with_mark_and_bezn))
    formatted_json_str = pprint.pformat(autodest_info.text)
    print(autodest_info.url, formatted_json_str, sep='\n\n')
    assert "\"eDrug\":true" in autodest_info.text

    choice_autodest_id = loads(autodest_info.text)['id']
    choice_autodest = app.choice_autodest(id=choice_autodest_id,
                                          head=app.token_autorization())
    formatted_json_str = pprint.pformat(choice_autodest.text)
    print(choice_autodest.url, formatted_json_str, sep='\n\n')
    assert choice_autodest.status_code == 200


def test_choice_autodest_with_mark_without_beznal_auth_user(app):
    autodest_info = app.autodest_info(autoDestId=choice(parameters.autodestid_with_mark_without_bezn))
    formatted_json_str = pprint.pformat(autodest_info.text)
    print(autodest_info.url, formatted_json_str, sep='\n\n')
    assert "\"eDrug\":true" in autodest_info.text

    choice_autodest_id = loads(autodest_info.text)['id']
    choice_autodest = app.choice_autodest(id=choice_autodest_id,
                                          head=app.token_autorization())
    formatted_json_str = pprint.pformat(choice_autodest.text)
    print(choice_autodest.url, formatted_json_str, sep='\n\n')
    assert choice_autodest.status_code == 200


def test_choice_autodest_without_mark_with_beznal_auth_user(app):
    autodest_info = app.autodest_info(autoDestId=choice(parameters.autodestid_without_mark_with_beznal))
    formatted_json_str = pprint.pformat(autodest_info.text)
    print(autodest_info.url, formatted_json_str, sep='\n\n')
    assert "\"eDrug\":false" in autodest_info.text

    choice_autodest_id = loads(autodest_info.text)['id']
    choice_autodest = app.choice_autodest(id=choice_autodest_id,
                                          head=app.token_autorization())
    formatted_json_str = pprint.pformat(choice_autodest.text)
    print(choice_autodest.url, formatted_json_str, sep='\n\n')
    assert choice_autodest.status_code == 200


def test_choice_autodest_su(app):
    choice_autodest = app.choice_autodest(id=parameters.select_autodest(),
                                             userId='5ee852c50521b00001edffed', head=app.token_auth_super_user())
    formatted_json_str = pprint.pformat(choice_autodest.text)
    print(choice_autodest.request.body)
    print(choice_autodest.url, formatted_json_str, sep='\n\n')
    assert choice_autodest.status_code == 200

