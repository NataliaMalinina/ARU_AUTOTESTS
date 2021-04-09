from random import choice
from model import parameters
from model.parameters import select_autodest
from model.parameters import random_string
import pprint


def test_autodest_review(app):
    autodest_review = app.autodest_review(head=app.token_autorization(), autoDestId=select_autodest(), rating=choice(parameters.rating),
                                          review=random_string(89), fio=random_string(15), orderNum=None, complaints=["Staff"],
                                          customReason=random_string(45))
    formatted_json_str = pprint.pformat(autodest_review.text)
    print(autodest_review.url, formatted_json_str, sep='\n\n')