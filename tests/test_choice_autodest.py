import pprint
from random import choice
from model import parameters


def test_choice_autodest_without_mark_and_beznal_shadow_user(app):
    choice_autodest = app.choice_autodest(id=choice(parameters.autodestid_without_mark_and_bezn))
    formatted_json_str = pprint.pformat(choice_autodest.text)
    print(choice_autodest.url, formatted_json_str, sep='\n\n')
    assert choice_autodest.status_code == 200


def test_choice_autodest_with_mark_and_beznal_shadow_user(app):
    choice_autodest = app.choice_autodest(id=choice(parameters.autodestid_with_mark_and_bezn))
    formatted_json_str = pprint.pformat(choice_autodest.text)
    print(choice_autodest.url, formatted_json_str, sep='\n\n')
    assert choice_autodest.status_code == 200


def test_choice_autodest_with_mark_without_beznal_shadow_user(app):
    choice_autodest = app.choice_autodest(id=choice(parameters.autodestid_with_mark_without_bezn))
    formatted_json_str = pprint.pformat(choice_autodest.text)
    print(choice_autodest.url, formatted_json_str, sep='\n\n')
    assert choice_autodest.status_code == 200


def test_choice_autodest_without_mark_with_beznal_shadow_user(app):
    choice_autodest = app.choice_autodest(id=choice(parameters.autodestid_without_mark_with_beznal))
    formatted_json_str = pprint.pformat(choice_autodest.text)
    print(choice_autodest.url, formatted_json_str, sep='\n\n')
    assert choice_autodest.status_code == 200


def test_choice_autodest_without_mark_and_beznal_auth_user(app):
    choice_autodest = app.choice_autodest_auth_user\
        (id=choice(parameters.autodestid_without_mark_and_bezn), head=app.token_autorization())
    formatted_json_str = pprint.pformat(choice_autodest.text)
    print(choice_autodest.url, formatted_json_str, sep='\n\n')
    assert choice_autodest.status_code == 200


def test_choice_autodest_with_mark_and_beznal_auth_user(app):
    choice_autodest = app.choice_autodest_auth_user(id=choice(parameters.autodestid_with_mark_and_bezn),
                                                    head=app.token_autorization())
    formatted_json_str = pprint.pformat(choice_autodest.text)
    print(choice_autodest.url, formatted_json_str, sep='\n\n')
    assert choice_autodest.status_code == 200

def test_choice_autodest_with_mark_without_beznal_auth_user(app):
    choice_autodest = app.choice_autodest_auth_user(id=choice(parameters.autodestid_with_mark_without_bezn),
                                                    head=app.token_autorization())
    formatted_json_str = pprint.pformat(choice_autodest.text)
    print(choice_autodest.url, formatted_json_str, sep='\n\n')
    assert choice_autodest.status_code == 200


def test_choice_autodest_without_mark_with_beznal_auth_user(app):
    choice_autodest = app.choice_autodest_auth_user(id=choice(parameters.autodestid_without_mark_with_beznal),
                                                    head=app.token_autorization())
    formatted_json_str = pprint.pformat(choice_autodest.text)
    print(choice_autodest.url, formatted_json_str, sep='\n\n')
    assert choice_autodest.status_code == 200


def test_choice_autodest_su(app):
    choice_autodest = app.choice_autodest_su(id=choice(parameters.autodestid_with_mark_and_bezn),
                                             userid='5ee852c50521b00001edffed', head=app.token_auth_admin_user())
    formatted_json_str = pprint.pformat(choice_autodest.text)
    print(choice_autodest.url, formatted_json_str, sep='\n\n')
    assert choice_autodest.status_code == 200

