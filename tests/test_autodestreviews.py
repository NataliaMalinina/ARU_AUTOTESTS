from random import choice, randrange
from model import parameters
from model.parameters import select_autodest, random_string, random_reason, random_custom_reason
import pprint
import pytest

#TODO подружить с монгой потом в плане id review

def test_autodest_review(app):
    autodest_review = app.autodest_review(head=app.token_autorization(), autoDestId=select_autodest(),
                                          rating=choice(parameters.rating),
                                          review=random_string(200), fio=random_string(15), orderNum=None,
                                          complaints=[],
                                          customReason=None)
    formatted_json_str = pprint.pformat(autodest_review.text)
    print(autodest_review.url, formatted_json_str, sep='\n\n')
    assert autodest_review.status_code == 200


@pytest.mark.repeat(5)
def test_add_autodest_review_with_reason(app):
    autodest_review = app.autodest_review(head=app.token_autorization(), autoDestId=select_autodest(),
                                          rating=choice(parameters.rating),
                                          review=random_string(200), fio=random_string(15), orderNum=None,
                                          complaints=random_reason(),
                                          customReason=None)
    formatted_json_str = pprint.pformat(autodest_review.text)
    print(autodest_review.request.body)
    print(autodest_review.url, formatted_json_str, sep='\n\n')
    assert autodest_review.status_code == 200


def test_add_autodest_review_with_custom_reason(app):
    autodest_review = app.autodest_review(head=app.token_autorization(), autoDestId=select_autodest(),
                                          rating=choice(parameters.rating),
                                          review=random_string(250), fio=random_string(15), orderNum=None,
                                          complaints=[],
                                          customReason=random_custom_reason())
    formatted_json_str = pprint.pformat(autodest_review.text)
    print(autodest_review.request.body)
    print(autodest_review.url, formatted_json_str, sep='\n\n')
    assert autodest_review.status_code == 200


def test_add_autodest_review_with_all_reasons(app):
    autodest_review = app.autodest_review(head=app.token_autorization(), autoDestId=select_autodest(),
                                          rating=choice(parameters.rating),
                                          review=random_string(300), fio=random_string(15), orderNum=None,
                                          complaints=random_reason(),
                                          customReason=random_custom_reason())
    formatted_json_str = pprint.pformat(autodest_review.text)
    print(autodest_review.request.body)
    print(autodest_review.url, formatted_json_str, sep='\n\n')
    assert autodest_review.status_code == 200


def test_add_autodest_review_all_complaints_reasons(app):
    autodest_review = app.autodest_review(head=app.token_autorization(), autoDestId=select_autodest(),
                                          rating=choice(parameters.rating),
                                          review=random_string(350), fio=random_string(15), orderNum=None,
                                          complaints=['Staff', 'Delivery', 'Cashless', 'Location', 'Schedule'],
                                          customReason=random_custom_reason())
    formatted_json_str = pprint.pformat(autodest_review.text)
    print(autodest_review.request.body)
    print(autodest_review.url, formatted_json_str, sep='\n\n')
    assert autodest_review.status_code == 200


def test_add_autodest_review_order_num(app):
    autodest_review = app.autodest_review(head=app.token_autorization(), autoDestId='5d763feb2b14e300015c5f9f',
                                          rating=choice(parameters.rating),
                                          review=random_string(322), fio=random_string(15), orderNum='AD-DEV-21000348',
                                          complaints=random_reason(),
                                          customReason=random_custom_reason())
    formatted_json_str = pprint.pformat(autodest_review.text)
    print(autodest_review.request.body)
    print(autodest_review.url, formatted_json_str, sep='\n\n')
    assert autodest_review.status_code == 200


def test_add_autodest_review_wrong_order_num(app):
    autodest_review = app.autodest_review(head=app.token_autorization(), autoDestId='5d763feb2b14e300015c5f9f',
                                          rating=choice(parameters.rating),
                                          review=random_string(105), fio=random_string(15), orderNum='AD-DEV-21000349',
                                          complaints=random_reason(),
                                          customReason=random_custom_reason())
    formatted_json_str = pprint.pformat(autodest_review.text)
    print(autodest_review.request.body)
    print(autodest_review.url, formatted_json_str, sep='\n\n')
    assert autodest_review.status_code == 400
    assert 'Заказ с указанным номером не найден' in autodest_review.text


def test_add_autodest_review_over_5000(app):
    review_over_5000 = random_string(randrange(5001, 10000))
    autodest_review = app.autodest_review(head=app.token_autorization(), autoDestId=select_autodest(),
                                          rating=choice(parameters.rating),
                                          review=review_over_5000, fio=random_string(15), orderNum=None,
                                          complaints=[],
                                          customReason=random_custom_reason())
    formatted_json_str = pprint.pformat(autodest_review.text)
    print(autodest_review.request.body)
    print(autodest_review.url, formatted_json_str, sep='\n\n')
    assert "Отзыв не может быть длинее 5000 символов" in autodest_review.text
    assert autodest_review.status_code == 400


def test_add_autodest_review_shadow_user(app):
    autodest_review = app.autodest_review(head=app.token_shadow_user(), autoDestId=select_autodest(),
                                          rating=choice(parameters.rating),
                                          review=random_string(155), fio=random_string(15), orderNum=None,
                                          complaints=random_reason(),
                                          customReason=random_custom_reason())
    formatted_json_str = pprint.pformat(autodest_review.text)
    print(autodest_review.request.body)
    print(autodest_review.url, formatted_json_str, sep='\n\n')
    assert autodest_review.status_code == 403


def test_add_autodest_review_without_token(app):
    autodest_review = app.autodest_review(head=None, autoDestId=select_autodest(),
                                          rating=choice(parameters.rating),
                                          review=random_string(350), fio=random_string(15), orderNum=None,
                                          complaints=random_reason(),
                                          customReason=random_custom_reason())
    formatted_json_str = pprint.pformat(autodest_review.text)
    print(autodest_review.request.body)
    print(autodest_review.url, formatted_json_str, sep='\n\n')
    assert autodest_review.status_code == 401


def test_edit_autodest_review_edit(app):
    autodest_review = app.autodest_review(head=app.token_autorization(), autoDestId=select_autodest(),
                                          rating=choice(parameters.rating),
                                          review=random_string(455), fio=random_string(15), orderNum=None,
                                          complaints=random_reason(),
                                          customReason=random_custom_reason())
    id_review = autodest_review.text.replace('\"', '')
    edit_review = app.edit_autodest_review(head=app.token_autorization(), id=id_review, rating=choice(parameters.rating), review=random_string(5050))
    formatted_json_str = pprint.pformat(edit_review.text)
    print(edit_review.request.body)
    print(edit_review.url, formatted_json_str, sep='\n\n')
    assert autodest_review.status_code == 200
    assert edit_review.status_code == 200


def test_edit_autodest_review_other_user(app):
    autodest_review = app.autodest_review(head=app.token_autorization(), autoDestId=select_autodest(),
                                          rating=choice(parameters.rating),
                                          review=random_string(455), fio=random_string(15), orderNum=None,
                                          complaints=random_reason(),
                                          customReason=random_custom_reason())
    id_review = autodest_review.text.replace('\"', '')
    edit_review = app.edit_autodest_review(head=app.token_shadow_user(), id=id_review, rating=choice(parameters.rating), review=random_string(150))
    formatted_json_str = pprint.pformat(edit_review.text)
    print(edit_review.request.body)
    print(edit_review.url, formatted_json_str, sep='\n\n')
    assert autodest_review.status_code == 200
    assert edit_review.status_code == 403


def test_edit_autodest_review_without_token(app):
    autodest_review = app.autodest_review(head=app.token_autorization(), autoDestId=select_autodest(),
                                          rating=choice(parameters.rating),
                                          review=random_string(455), fio=random_string(15), orderNum=None,
                                          complaints=random_reason(),
                                          customReason=random_custom_reason())
    id_review = autodest_review.text.replace('\"', '')
    edit_review = app.edit_autodest_review(head=None, id=id_review, rating=choice(parameters.rating), review=random_string(150))
    formatted_json_str = pprint.pformat(edit_review.text)
    print(edit_review.request.body)
    print(edit_review.url, formatted_json_str, sep='\n\n')
    assert autodest_review.status_code == 200
    assert edit_review.status_code == 401


def test_delete_autodest_review(app):
    autodest_review = app.autodest_review(head=app.token_autorization(), autoDestId=select_autodest(),
                                          rating=choice(parameters.rating),
                                          review=random_string(455), fio=random_string(15), orderNum=None,
                                          complaints=random_reason(),
                                          customReason=random_custom_reason())
    id_review = autodest_review.text.replace('\"', '')
    delete_review = app.delete_autodest_review(head=app.token_autorization(), reviewId=id_review)
    formatted_json_str = pprint.pformat(delete_review.text)
    print(delete_review.request.body)
    print(delete_review.url, formatted_json_str, sep='\n\n')
    assert autodest_review.status_code == 200
    assert delete_review.status_code == 200


def test_delete_autodest_review_other_user(app):
    autodest_review = app.autodest_review(head=app.token_autorization(), autoDestId=select_autodest(),
                                          rating=choice(parameters.rating),
                                          review=random_string(455), fio=random_string(15), orderNum=None,
                                          complaints=random_reason(),
                                          customReason=random_custom_reason())
    id_review = autodest_review.text.replace('\"', '')
    delete_review = app.delete_autodest_review(head=app.token_shadow_user(), reviewId=id_review)
    formatted_json_str = pprint.pformat(delete_review.text)
    print(delete_review.request.body)
    print(delete_review.url, formatted_json_str, sep='\n\n')
    assert autodest_review.status_code == 200
    assert delete_review.status_code == 403


def test_delete_autodest_review_without_token(app):
    autodest_review = app.autodest_review(head=app.token_autorization(), autoDestId=select_autodest(),
                                          rating=choice(parameters.rating),
                                          review=random_string(455), fio=random_string(15), orderNum=None,
                                          complaints=random_reason(),
                                          customReason=random_custom_reason())
    id_review = autodest_review.text.replace('\"', '')
    delete_review = app.delete_autodest_review(head=None, reviewId=id_review)
    formatted_json_str = pprint.pformat(delete_review.text)
    print(delete_review.request.body)
    print(delete_review.url, formatted_json_str, sep='\n\n')
    assert autodest_review.status_code == 200
    assert delete_review.status_code == 401




