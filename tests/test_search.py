from model import parameters
import random
import json


def test_search(app):
    search = app.search(app, phrase=random.choice(parameters.phrase), sort=random.choice(parameters.sort),
                             cityid=random.choice(parameters.cityid), withprice=random.choice(parameters.withprice),
                             withprofit=random.choice(parameters.withprofit), withpromoVits=random.choice(parameters.withpromoVits))
    print(search.url, search.content, sep='\n')
    assert search.status_code == 200


def test_search_tags(app):
    search = app.search_with_tags(app, phrase='зубная паста', tags='splat', sort='Default',
                        cityid='5e574686defa1e000131b5df', withprice='false', withprofit='false',
                        withpromoVits='false')
    print(search.url, search.text, sep='\n')
    assert "minGroupPrice" in json.loads(search.content) and search.status_code == 200


def test_search_hyphen(app):
    search = app.search(app, phrase='но-шпа', sort='Default',
                        cityid=random.choice(parameters.cityid), withprice='false', withprofit='false',
                        withpromoVits='false')
    print(search.url, search.text, sep='\n')


def test_search_translit(app):
    search = app.search(app, phrase='авене', sort='Default',
                        cityid=random.choice(parameters.cityid), withprice='false', withprofit='false',
                        withpromoVits='false')
    print(search.url, search.text, sep='\n')
    assert "<em>AVENE</em>" in json.loads(search.content) and search.status_code == 200


