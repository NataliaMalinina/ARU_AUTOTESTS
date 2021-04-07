                                                                      # TODO: для тестов регистрации возможно реализовать MOCK - сервис, который отправляет смс напр-р смс-код даты 07.04.2021 был бы 0704
def test_auth(app):
    authorization = app.auth(code='9213', phone='+79139519213')
    assert authorization.status_code == 200
    assert "\"token\":" in authorization.text


def test_auth8(app):
    authorization = app.auth(code='9213', phone='89139519213')
    assert authorization.status_code == 200
    assert "\"token\":" in authorization.text


def test_auth_not_valid_password(app):
    authorization = app.auth(code='9999', phone='+79139519213')
    assert authorization.status_code == 400
    assert "\"Указан некорректный пароль/код смс\"" in authorization.text


def test_auth_not_valid_phone(app):
    authorization = app.auth(code='9213', phone='лаавпалвпавда')
    assert authorization.status_code == 400
    assert "\"Не указан номер телефона для авторизации\"" in authorization.text


def test_auth_empty_phone(app):
    authorization = app.auth(code='9213', phone=None)
    assert authorization.status_code == 400
    assert "\"Не указан номер телефона для авторизации\"" in authorization.text


def test_auth_empty_password(app):
    authorization = app.auth(code=None, phone='+79139519213')
    assert authorization.status_code == 400
    assert "\"Указан некорректный пароль/код смс\"" in authorization.text


def test_auth_empty_parameters(app):
    authorization = app.auth(code=None, phone=None)
    assert authorization.status_code == 400
    assert "\"Не указан номер телефона для авторизации\"" in authorization.text


def test_auth_banned_user(app):
    authorization = app.auth(code='5596', phone='+79994651210')
    assert authorization.status_code == 400
    assert "\"Указан некорректный пароль/код смс\"" in authorization.text

