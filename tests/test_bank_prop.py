from trollfactory.props.bank import Bank
from schwifty import IBAN

generated_bank_info = Bank.generate({'language': {'language': 'polish'},
                                     'birthdate': {'age': 15}})


def test_bank_info_generated():
    assert generated_bank_info['prop_title'] == 'Bank'


def test_valid_pekao_iban():
    assert (IBAN(generated_bank_info['iban_pekao']) and ''.join(
            generated_bank_info['iban_pekao'].split(' ')[1:3]) == '12400001')


def test_valid_mbank_iban():
    assert (IBAN(generated_bank_info['iban_mbank']) and ''.join(
            generated_bank_info['iban_mbank'].split(' ')[1:3]) == '11402004')


def test_valid_ing_iban():
    assert (IBAN(generated_bank_info['iban_ing']) and ''.join(
            generated_bank_info['iban_ing'].split(' ')[1:3]) == '10501012')


def test_valid_pko_iban():
    assert (IBAN(generated_bank_info['iban_pko']) and ''.join(
            generated_bank_info['iban_pko'].split(' ')[1:3]) == '10205561')


def test_no_account_under_13():
    assert Bank.generate({'language': {'language': 'polish'},
                          'birthdate': {'age': 12}})['iban'] is None
