from model import parameters
from random import choice
import pprint
import pytest

#TODO: подружить с монгой(?) чтобы взять сити id из БД

@pytest.mark.repeat(5)
def test_search_random(app):
    cityid = choice(parameters.cityid)
    search = app.search_random(page=0, pagesize=5, phrase=choice(parameters.phrase), sort=choice(parameters.sort),
                             cityid=cityid, withprice=choice(parameters.withprice),
                             withprofit=choice(parameters.withprofit), withpromoVits=choice(parameters.withpromoVits))
    formatted_json_str = pprint.pformat(search.text)
    print(search.url, formatted_json_str, sep='\n\n')
    #print(search.url, search.text, sep='\n')
    if cityid == '5e574663b1585900015ed444':
        assert search.status_code == 400
    else:
        assert search.status_code == 200


def test_search_tags(app):
    search = app.search_with_tags(phrase='зубная паста', tags='splat', sort='Default',
                        cityid='5e574686defa1e000131b5df', withprice='false', withprofit='false',
                        withpromoVits='false')
    formatted_json_str = pprint.pformat(search.text)
    print(search.url, formatted_json_str, sep='\n\n')
    #print(search.url, search.text, sep='\n')
    assert "<em>ЗУБНАЯ</em> <em>ПАСТА</em>" in search.text
    assert search.status_code == 200
    assert "minGroupPrice" in search.text
    assert "\"result\":[{" in search.text
    assert "\"result\": []" not in search.text


def test_search_hyphen(app):
    cityid = choice(parameters.cityid)
    search = app.search(phrase='крем-гель', sort='Default',
                        cityid=cityid, withprice='false', withprofit='false',
                        withpromoVits='false')
    formatted_json_str = pprint.pformat(search.text)
    print(search.url, formatted_json_str, sep='\n\n')
    #print(search.url, search.text, sep='\n')
    if cityid == '5e574663b1585900015ed444':
        assert search.status_code == 400
    else:
        assert search.status_code == 200
        assert "<em>КРЕМ-ГЕЛЬ</em>" in search.text


def test_search_hyphen2(app):
    cityid = choice(parameters.cityid)
    search = app.search(phrase='кремгель', sort='Default',
                        cityid=cityid, withprice='false', withprofit='false',
                        withpromoVits='false')
    formatted_json_str = pprint.pformat(search.text)
    print(search.url, formatted_json_str, sep='\n\n')
    #print(search.url, search.text, sep='\n')
    if cityid == '5e574663b1585900015ed444':
        assert search.status_code == 400
    else:
        assert search.status_code == 200
        assert "<em>КРЕМ-ГЕЛЬ</em>" in search.text


def test_search_hyphen3(app):
    cityid = choice(parameters.cityid)
    search = app.search(phrase='крем гель', sort='Default',
                        cityid=cityid, withprice='false', withprofit='false',
                        withpromoVits='false')
    formatted_json_str = pprint.pformat(search.text)
    print(search.url, formatted_json_str, sep='\n\n')
    #print(search.url, search.text, sep='\n')
    if cityid == '5e574663b1585900015ed444':
        assert search.status_code == 400
    else:
        assert search.status_code == 200
        assert "<em>КРЕМ</em>-<em>ГЕЛЬ</em>" in search.text


def test_search_translit(app):
    cityid = choice(parameters.cityid)
    search = app.search(phrase='авене', sort='Default',
                        cityid=cityid, withprice='false', withprofit='false',
                        withpromoVits='false')
    #print(search.url, search.text, sep='\n')
    formatted_json_str = pprint.pformat(search.text)
    print(search.url, formatted_json_str, sep='\n\n')
    if cityid == '5e574663b1585900015ed444':
        assert search.status_code == 400
    else:
        assert "<em>AVENE</em>" in search.text
        assert search.status_code == 200


def test_search_rus_in_eng_letters(app):
    search = app.search(phrase='cgfpufy', sort='Default',
                            cityid='5e574686defa1e000131b5df', withprice='false', withprofit='false',
                            withpromoVits='false')
    formatted_json_str = pprint.pformat(search.text)
    print(search.url, formatted_json_str, sep='\n\n')
    # print(search.url, search.text, sep='\n')
    assert "СПАЗГАН" in search.text
    assert search.status_code == 200


def test_search_eng_in_rus_letters(app):
    search = app.search(phrase='гарниер', sort='Default',
                        cityid='5e574686defa1e000131b5df', withprice='false', withprofit='false',
                        withpromoVits='false')
    formatted_json_str = pprint.pformat(search.text)
    print(search.url, formatted_json_str, sep='\n\n')
    # print(search.url, search.text, sep='\n')
    assert "GARNIER" in search.text
    assert search.status_code == 200


def test_search_typo(app):
    search = app.search(phrase='кафеин', sort='Default',
                        cityid='5e574686defa1e000131b5df', withprice='false', withprofit='false',
                        withpromoVits='false')
    formatted_json_str = pprint.pformat(search.text)
    print(search.url, formatted_json_str, sep='\n\n')
    # print(search.url, search.text, sep='\n')
    assert "<em>КОФЕИН</em>" in search.text
    assert "\"suggestion\":\"кофеин\"" in search.text
    assert search.status_code == 200


def test_search_over_pagination(app):
    cityid = choice(parameters.cityid)
    search = app.search_random(page=1000, pagesize=5, phrase=choice(parameters.phrase),
                               sort=choice(parameters.sort),
                               cityid=cityid, withprice=choice(parameters.withprice),
                               withprofit=choice(parameters.withprofit),
                               withpromoVits=choice(parameters.withpromoVits))
    formatted_json_str = pprint.pformat(search.text)
    print(search.url, formatted_json_str, sep='\n\n')
    #print(search.url, search.text, sep='\n')
    if cityid == '5e574663b1585900015ed444':
        assert search.status_code == 400
    else:
        assert search.status_code == 200
        assert "\"result\":[{" not in search.text
        assert "\"result\":[]" in search.text
