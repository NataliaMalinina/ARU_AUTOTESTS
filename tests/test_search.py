from model import parameters
import random
import pprint
import pytest


@pytest.mark.repeat(3)
def test_search_random(app):
    search = app.search_random(app, page=0, pagesize=5, phrase=random.choice(parameters.phrase), sort=random.choice(parameters.sort),
                             cityid=random.choice(parameters.cityid), withprice=random.choice(parameters.withprice),
                             withprofit=random.choice(parameters.withprofit), withpromoVits=random.choice(parameters.withpromoVits))
    formatted_json_str = pprint.pformat(search.text)
    print(search.url, formatted_json_str, sep='\n\n')
    #print(search.url, search.text, sep='\n')
    assert search.status_code == 200


def test_search_tags(app):
    search = app.search_with_tags(app, phrase='зубная паста', tags='splat', sort='Default',
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
    search = app.search(app, phrase='крем-гель', sort='Default',
                        cityid=random.choice(parameters.cityid), withprice='false', withprofit='false',
                        withpromoVits='false')
    formatted_json_str = pprint.pformat(search.text)
    print(search.url, formatted_json_str, sep='\n\n')
    #print(search.url, search.text, sep='\n')
    assert "<em>КРЕМ-ГЕЛЬ</em>" in search.text
    assert search.status_code == 200


def test_search_hyphen2(app):
    search = app.search(app, phrase='кремгель', sort='Default',
                        cityid=random.choice(parameters.cityid), withprice='false', withprofit='false',
                        withpromoVits='false')
    formatted_json_str = pprint.pformat(search.text)
    print(search.url, formatted_json_str, sep='\n\n')
    #print(search.url, search.text, sep='\n')
    assert "<em>КРЕМ-ГЕЛЬ</em>" in search.text
    assert search.status_code == 200


def test_search_hyphen3(app):
    search = app.search(app, phrase='крем гель', sort='Default',
                        cityid=random.choice(parameters.cityid), withprice='false', withprofit='false',
                        withpromoVits='false')
    formatted_json_str = pprint.pformat(search.text)
    print(search.url, formatted_json_str, sep='\n\n')
    #print(search.url, search.text, sep='\n')
    assert "<em>КРЕМ</em>-<em>ГЕЛЬ</em>" in search.text
    assert search.status_code == 200


def test_search_translit(app):
    search = app.search(app, phrase='авене', sort='Default',
                        cityid=random.choice(parameters.cityid), withprice='false', withprofit='false',
                        withpromoVits='false')
    #print(search.url, search.text, sep='\n')
    formatted_json_str = pprint.pformat(search.text)
    print(search.url, formatted_json_str, sep='\n\n')
    assert "<em>AVENE</em>" in search.text
    assert search.status_code == 200


def test_search_rus_in_eng_letters(app):
    search = app.search(app, phrase='cgfpufy', sort='Default',
                            cityid='5e574686defa1e000131b5df', withprice='false', withprofit='false',
                            withpromoVits='false')
    formatted_json_str = pprint.pformat(search.text)
    print(search.url, formatted_json_str, sep='\n\n')
    # print(search.url, search.text, sep='\n')
    assert "СПАЗГАН" in search.text
    assert search.status_code == 200


def test_search_eng_in_rus_letters(app):
    search = app.search(app, phrase='гарниер', sort='Default',
                        cityid='5e574686defa1e000131b5df', withprice='false', withprofit='false',
                        withpromoVits='false')
    formatted_json_str = pprint.pformat(search.text)
    print(search.url, formatted_json_str, sep='\n\n')
    # print(search.url, search.text, sep='\n')
    assert "GARNIER" in search.text
    assert search.status_code == 200


def test_search_typo(app):
    search = app.search(app, phrase='кафеин', sort='Default',
                        cityid='5e574686defa1e000131b5df', withprice='false', withprofit='false',
                        withpromoVits='false')
    formatted_json_str = pprint.pformat(search.text)
    print(search.url, formatted_json_str, sep='\n\n')
    # print(search.url, search.text, sep='\n')
    assert "<em>КОФЕИН</em>" in search.text
    assert "\"suggestion\":\"кофеин\"" in search.text
    assert search.status_code == 200


def test_search_over_pagination(app):
    search = app.search_random(app, page=1000, pagesize=5, phrase=random.choice(parameters.phrase),
                               sort=random.choice(parameters.sort),
                               cityid=random.choice(parameters.cityid), withprice=random.choice(parameters.withprice),
                               withprofit=random.choice(parameters.withprofit),
                               withpromoVits=random.choice(parameters.withpromoVits))
    formatted_json_str = pprint.pformat(search.text)
    print(search.url, formatted_json_str, sep='\n\n')
    #print(search.url, search.text, sep='\n')
    assert "\"result\":[{" not in search.text
    assert "\"result\":[]" in search.text



