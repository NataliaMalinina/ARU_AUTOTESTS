from random import choice
from model import parameters
from model.parameters import select_autodest, random_string, random_reason, random_custom_reason
import pprint
import pytest


def test_autodest_review(app):
    autodest_review = app.autodest_review(head=app.token_autorization(), autoDestId=select_autodest(),
                                          rating=choice(parameters.rating),
                                          review=random_string(5050), fio=random_string(15), orderNum=None,
                                          complaints=[],
                                          customReason=None)
    formatted_json_str = pprint.pformat(autodest_review.text)
    print(autodest_review.url, formatted_json_str, sep='\n\n')
    if "Отзыв не может быть длинее 5000 символов" in autodest_review.text:
        assert autodest_review.status_code == 400
    else:
        assert autodest_review.status_code == 200


@pytest.mark.repeat(5)
def test_autodest_review_with_reason(app):
    autodest_review = app.autodest_review(head=app.token_autorization(), autoDestId=select_autodest(),
                                          rating=choice(parameters.rating),
                                          review=random_string(5050), fio=random_string(15), orderNum=None,
                                          complaints=random_reason(),
                                          customReason=None)
    formatted_json_str = pprint.pformat(autodest_review.text)
    print(autodest_review.request.body)
    print(autodest_review.url, formatted_json_str, sep='\n\n')
    if "Отзыв не может быть длинее 5000 символов" in autodest_review.text:
        assert autodest_review.status_code == 400
    else:
        assert autodest_review.status_code == 200


def test_autodest_review_with_custom_reason(app):
    autodest_review = app.autodest_review(head=app.token_autorization(), autoDestId=select_autodest(),
                                          rating=choice(parameters.rating),
                                          review=random_string(5050), fio=random_string(15), orderNum=None,
                                          complaints=[],
                                          customReason=random_custom_reason())
    formatted_json_str = pprint.pformat(autodest_review.text)
    print(autodest_review.request.body)
    print(autodest_review.url, formatted_json_str, sep='\n\n')
    if "Отзыв не может быть длинее 5000 символов" in autodest_review.text:
        assert autodest_review.status_code == 400
    else:
        assert autodest_review.status_code == 200


def test_autodest_review_with_all_reasons(app):
    autodest_review = app.autodest_review(head=app.token_autorization(), autoDestId=select_autodest(),
                                          rating=choice(parameters.rating),
                                          review=random_string(5050), fio=random_string(15), orderNum=None,
                                          complaints=random_reason(),
                                          customReason=random_custom_reason())
    formatted_json_str = pprint.pformat(autodest_review.text)
    print(autodest_review.request.body)
    print(autodest_review.url, formatted_json_str, sep='\n\n')
    if "Отзыв не может быть длинее 5000 символов" in autodest_review.text:
        assert autodest_review.status_code == 400
    else:
        assert autodest_review.status_code == 200


def test_autodest_review_order_num(app):
    autodest_review = app.autodest_review(head=app.token_autorization(), autoDestId='5d763feb2b14e300015c5f9f',
                                          rating=choice(parameters.rating),
                                          review=random_string(5050), fio=random_string(15), orderNum='AD-DEV-21000348',
                                          complaints=random_reason(),
                                          customReason=random_custom_reason())
    formatted_json_str = pprint.pformat(autodest_review.text)
    print(autodest_review.request.body)
    print(autodest_review.url, formatted_json_str, sep='\n\n')
    if "Отзыв не может быть длинее 5000 символов" in autodest_review.text:
        assert autodest_review.status_code == 400
    else:
        assert autodest_review.status_code == 200


def test_autodest_review_wrong_order_num(app):
    autodest_review = app.autodest_review(head=app.token_autorization(), autoDestId='5d763feb2b14e300015c5f9f',
                                          rating=choice(parameters.rating),
                                          review=random_string(5050), fio=random_string(15), orderNum='AD-DEV-21000349',
                                          complaints=random_reason(),
                                          customReason=random_custom_reason())
    formatted_json_str = pprint.pformat(autodest_review.text)
    print(autodest_review.request.body)
    print(autodest_review.url, formatted_json_str, sep='\n\n')
    if "Отзыв не может быть длинее 5000 символов" in autodest_review.text:
        assert autodest_review.status_code == 400
    else:
        assert autodest_review.status_code == 400
        assert 'Заказ с указанным номером не найден' in autodest_review.text


def test_autodest_review_shadow_user(app):
    autodest_review = app.autodest_review(head=app.token_shadow_user(), autoDestId=select_autodest(),
                                          rating=choice(parameters.rating),
                                          review=random_string(5050), fio=random_string(15), orderNum=None,
                                          complaints=random_reason(),
                                          customReason=random_custom_reason())
    formatted_json_str = pprint.pformat(autodest_review.text)
    print(autodest_review.request.body)
    print(autodest_review.url, formatted_json_str, sep='\n\n')
    if "Отзыв не может быть длинее 5000 символов" in autodest_review.text:
        assert autodest_review.status_code == 400
    else:
        assert autodest_review.status_code == 403
