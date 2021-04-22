from random import choice, randint, sample
import string


phrase = ('Ношпа', 'qjl', 'зелёнка', 'Гинко', 'Nivea', 'посай', 'корица', ',jkm d cgbyt', 'YFANBPBY', 'виши', 'ANAPHASE+')

sort = ('Default', 'DefaultAsc', 'ByName', 'ByNameDesc', 'ByPrice', 'ByPriceDesc')

cityid = ('5e574686defa1e000131b5df', '5e56f692524b5400014ace3f', '5e574663f4d315000196b176',
          '6040246bff6a27c8190300cb', '5e574663b1585900015edec3', '5e574883f995b1000174dd32', '5e574663b1585900015ed444')

valid_city = ('5e574663f4d315000196b176', '5e574686defa1e000131b5df', '5e56f692524b5400014ace3f')

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

autodestid_for_order = ('5d763e1d4ad2780001f5d7d2', '5d654e1ee326d700012acb6d', '5d763d8d4ad2780001f5d297', '5d654fa826306f000138a787',
                        '5d763d564ad2780001f5cfb8', '5d763d530fdde500017536e5')

not_active_autodest = ('603f3ef6cc79d08973eb6935', '603f3ef6cc79d08973eb692f', '603f3eefcc79d08973eb68b4')

rating = [1, 2, 3, 4, 5]

items = ['5d650aa084406a0001aaf8d6', '5d650bf884406a0001ab07a5', '5d65078f84406a0001aad571', '5d6504702fd44a0001b10360',
         '5d64fb2900e6ae00010111c5', '5d6504a784406a0001aab358', '5d6506b584406a0001aacce6', '5d64fb5b00e6ae0001011407',
         '5d650cd12fd44a0001b16432', '5d65037e84406a0001aaa5be', '5d6503e12fd44a0001b0fcfb', '5d65048684406a0001aab20f',
         '5d650a2384406a0001aaf48d', '5d6505352fd44a0001b10a72', '5d6507d084406a0001aad7c5', '5d64fb159d31820001f3bc0e',
         '5d650c2f2fd44a0001b15c9f', '5d64fddf2fd44a0001b0bad5', '5d6504c22fd44a0001b10698', '5d6504882fd44a0001b10447']


def random_string(length):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    random_string = "".join([choice(symbols) for i in range(length)])
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