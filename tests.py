import pytest
from click.testing import CliRunner
from pizza import Margherita, Pepperoni, Hawaiian
from cli import cli


def test_menu_output():
    """
    Проверяет корректный вывод меню
    """
    runner = CliRunner()
    result = runner.invoke(cli, ['menu'])

    assert 'Меню:' in result.output
    assert 'Margherita 🧀: ' in result.output
    assert 'Pepperoni 🍕: ' in result.output
    assert 'Hawaiian 🍍: ' in result.output
    assert 'Доступные размеры' in result.output


def test_wrong_size():
    """
    Проверяет случай, если размера нет в списке размеров.
    """
    runner = CliRunner()
    result = runner.invoke(cli, ['order', 'pepperoni', 's'])

    assert 'Такого размера нет:(' in result.output


def test_wrong_pizza():
    """
    Проверяет случай, если заказывают пиццу, которой нет в меню.
    """
    runner = CliRunner()
    result = runner.invoke(cli, ['order', 'diavola', 'l'])

    assert 'Мы пока еще не умеем готовить такую пиццу :(' in result.output


def test_no_size():
    """
    Проверяет случай, если в заказе размер не указан.
    """
    runner = CliRunner()
    result = runner.invoke(cli, ['order', 'margherita'])

    assert result.exit_code != 0
    assert 'Missing argument' in result.output


def test_no_pizza():
    """
    Проверяет случай, если в заказе не указана пицца.
    """
    runner = CliRunner()
    result = runner.invoke(cli, ['order'])

    assert result.exit_code != 0
    assert 'Missing argument' in result.output


def test_order():
    """
    Проверяет корректный вывод заказа без флагов.
    """
    runner = CliRunner()
    result = runner.invoke(cli, ['order', 'margherita', 'xl'])

    assert 'Приготовили за' in result.output
    assert 'Ваша пицца готова!' in result.output


def test_order_delivery():
    """
    Проверяет корректный вывод заказа с флагом доставки.
    """
    runner = CliRunner()
    result = runner.invoke(cli, ['order', 'margherita', 'xl', '--delivery'])

    assert 'Приготовили за' in result.output
    assert 'Доставили за' in result.output
    assert 'Заказ доставлен!' in result.output


def test_order_takeout():
    """
    Проверяет корректный вывод заказа с флагом самовывоза.
    """
    runner = CliRunner()
    result = runner.invoke(cli, ['order', 'margherita', 'xl', '--takeout'])

    assert 'Приготовили за' in result.output
    assert 'Забрали за' in result.output
    assert 'Спасибо, что пользуетесь самовывозом!' in result.output


def test_margherita_dict():
    """
    Тестирует вывод рецепт Маргариты.
    """
    margherita = Margherita('L')
    assert margherita.__dict__() == {
        'size': 'L',
        'ingredients': ['tomato sauce', 'mozzarella', 'tomatoes']
    }


def test_pepperoni_dict():
    """
    Тестирует вывод рецепт Пепперони.
    """
    pepperoni = Pepperoni('L')
    assert pepperoni.__dict__() == {
        'size': 'L',
        'ingredients': ['tomato sauce', 'mozzarella', 'pepperoni']
    }


def test_hawaiian_dict():
    """
    Тестирует вывод рецепт Гавайской пиццы.
    """
    hawaiian = Hawaiian('XL')
    assert hawaiian.__dict__() == {
        'size': 'XL',
        'ingredients': ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']
    }


def test_eq_true():
    """
    Тестирует сравнение пиццы в случае, если они одинаковые.
    """
    margherita = Margherita('XL')
    assert margherita.__eq__(Margherita('XL')) is True


def test_eq_false():
    """
    Тестирует сравнение пиццы в случае, если они разные.
    """
    margherita = Margherita('XL')
    assert margherita.__eq__(Pepperoni('XL')) is False


def test_eq_wrong_type():
    """
    Сравнивает пиццы в случае, если тип пиццы
    не тот, который ожидался.
    """
    with pytest.raises(ValueError):
        margherita = Margherita('XL')
        margherita.__eq__('pepperoni')
