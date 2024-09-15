import pytest
from string_utils import StringUtils

# Принимает на вход текст, делает первую букву заглавной и возвращает этот же
# текст


@pytest.mark.parametrize('string, result', [
    # позитивные
    ('aysen', 'Aysen'),
    ('1234', '1234'),
    ('test 1', 'Test 1'),
    # негативные
    ('', ''),
    (' ', ' '),
    ('Aysen', 'Aysen'),
    ])
def test_str(string, result):
    string_utils = StringUtils()
    res = string_utils.capitilize(string)
    assert res == result

# Принимает на вход текст и удаляет пробелы в начале, если они есть


@pytest.mark.parametrize('string_trim, result', [
    # позитивные
    ('  aysen', 'aysen'),
    (' 1234', '1234'),
    (' aysen ivanov', 'aysen ivanov'),
    # негативные
    ('', '')
    ])
def test_trim(string_trim, result):
    string_utils = StringUtils()
    res = string_utils.trim(string_trim)
    assert res == result

# Принимает на вход текст с разделителем и возвращает список строк.


@pytest.mark.parametrize('string_to_list, delimetr, result', [
    # позитивные
    ('a,y,s,e,n', ',', ['a', 'y', 's', 'e', 'n']),
    ('1:2:3', ':', ['1', '2', '3']),
    # негативные
    ('', None, []),
    ('a,y,s,e n', None, ['a', 'y', 's', 'e n'])
    ])
def test_to_list(string_to_list, delimetr, result):
    string_utils = StringUtils()
    if delimetr is None:
        res = string_utils.to_list(string_to_list)
    else:
        res = string_utils.to_list(string_to_list, delimetr)
    assert res == result


# Возвращает `True`, если строка содержит искомый символ и `False` - если нет


@pytest.mark.parametrize('string_contains, symbol, result', [
    # позитивные
    ('aysen', 'a', True),
    ('123454', '3', True),
    # негативные
    ('123456', 'a', False),
    ('aysen', 'b', False),
    ('aysen', ',', False)
    ])
def test_contains(string_contains, symbol, result):
    string_utils = StringUtils()
    res = string_utils.contains(string_contains, symbol)
    assert res == result

# Удаляет все подстроки из переданной строки


@pytest.mark.parametrize('string_del_symb, symbol, result', [
    # позитивные
    ('aysen', 'a', 'ysen'),
    ('123454', '3', '12454'),
    # негативные
    ('aysen', 'z', 'aysen'),
    ('', '', ''),
    ('', '', '')
    ])
def test_delete_symb(string_del_symb, symbol, result):
    string_utils = StringUtils()
    res = string_utils.delete_symbol(string_del_symb, symbol)
    assert res == result

# Возвращает `True`, если строка начинается с заданного символа и `False` -
# если нет


@pytest.mark.parametrize('string_starts_with, symbol, result', [
    # позитивные
    ('aysen', 'a', True),
    ('123454', '1', True),
    ('', '', True),
    # негативные
    ('aysen', 'z', False),
    ('', '^', False),
    ('aysen', 'A', False)
    ])
def test_starts_with(string_starts_with, symbol, result):
    string_utils = StringUtils()
    res = string_utils.starts_with(string_starts_with, symbol)
    assert res == result

# Возвращает `True`, если строка заканчивается заданным символом и `False` -
# если нет


@pytest.mark.parametrize('string_end_with, symbol, result', [
    # позитивные
    ('aysen', 'n', True),
    ('123454', '4', True),
    ('', '', True),
    # негативные
    ('aysen', 'z', False),
    ('', '^', False),
    ('aysen', 'A', False)
    ])
def test_end_with(string_end_with, symbol, result):
    string_utils = StringUtils()
    res = string_utils.end_with(string_end_with, symbol)
    assert res == result


# Возвращает `True`, если строка пустая и `False` - если нет


@pytest.mark.parametrize('string_is_empty, result', [
    # позитивные
    ('', True),
    (' ', True),
    ('  ', True),
    # негативные
    ('aysen', False),
    (' aysen', False),
    ('123', False)
    ])
def test_is_empty(string_is_empty, result):
    string_utils = StringUtils()
    res = string_utils.is_empty(string_is_empty)
    assert res == result

# Преобразует список элементов в строку с указанным разделителем


@pytest.mark.parametrize('string_list_to, joiner, result', [
    # позитивные
    (['a', 'y', 's', 'e', 'n'], ',', 'a,y,s,e,n'),
    ([1, 2, 3], None, '1, 2, 3'),
    (['a', 'y', 's', 'e', 'n'], '', 'aysen'),
    (['aysen', 'ivanov'], 'AKA', 'aysenAKAivanov'),
    # негативные
    ([], None, ''),
    ([], 'ays', ''),
    ([], ',', '')
    ])
def test_list_to_string(string_list_to, joiner, result):
    string_utils = StringUtils()
    if joiner is None:
        res = string_utils.list_to_string(string_list_to)
    else:
        res = string_utils.list_to_string(string_list_to, joiner)
    assert res == result
