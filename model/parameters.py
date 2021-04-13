from random import choice, randrange, randint, sample
import string

phrase = ('Ношпа', 'qjl', 'зелёнка', 'Гинко', 'Nivea', 'посай', 'корица', ',jkm d cgbyt', 'YFANBPBY', 'виши', 'ANAPHASE+')
sort = ('Default', 'DefaultAsc', 'ByName', 'ByNameDesc', 'ByPrice', 'ByPriceDesc')
cityid = ('5e574686defa1e000131b5df', '5e56f692524b5400014ace3f', '5e574663f4d315000196b176',
          '6040246bff6a27c8190300cb', '5e574663b1585900015edec3', '5e574883f995b1000174dd32', '5e574663b1585900015ed444')
withprice = ('true', 'false')
withprofit = ('true', 'false')
withpromoVits = ('true', 'false')
autodestid_without_mark_and_bezn = ('5d763ff52b14e300015c602b', '603f3ef4fd563be5e186b944',
                                '603f3ef4fd563be5e186b93f', '603f3ef4cc79d08973eb690c', '603f3ef3fd563be5e186b92d')
autodestid_with_mark_and_bezn = ('5d886ea192c02e00014cb057', '603f3ebacc79d08973eb6506', '5d653441217189000122707a',
                                 '5d88684392c02e00014c6831', '5d653c77bcf5ab00017aceaa')
autodestid_with_mark_without_bezn = ('603f3ef6fd563be5e186b967', '5d88759d92c02e00014d0a32', '603f3ef6cc79d08973eb692c',
                                     '603f3ef4fd563be5e186b935', '603f3ef7cc79d08973eb6939')
autodestid_without_mark_with_beznal = ('603f3ef7fd563be5e186b96f', '603f3ef7cc79d08973eb6936', '603f3ef6fd563be5e186b968',
                                       '603f3ef6fd563be5e186b964', '603f3ef6fd563be5e186b95a')
rating = [1, 2, 3, 4, 5]


def random_string(length):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    random_string = "".join([choice(symbols) for i in range(randrange(length))])
    return random_string


def select_autodest():
    return choice(autodestid_with_mark_and_bezn+autodestid_without_mark_and_bezn+autodestid_with_mark_without_bezn+autodestid_without_mark_with_beznal)


def random_reason():
    index = randint(0, 4)
    standardReasons = ('Staff', 'Delivery', 'Cashless', 'Location', 'Schedule')
    reason = sample(standardReasons, index)
    return reason


def random_custom_reason():
    customer_reason = random_string(99)
    null = None
    custom_reason = customer_reason or null
    return custom_reason




#TODO здесь в параметрах делать выборку id из монги, я думаю