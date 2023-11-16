from typing import List, Dict


class Pizza():
    """
    Класс для Пиццы
    """

    size = ['L', 'XL']

    def __init__(self, size: str, ingredients: List[str]):
        """
        Инициализация объектов класса Pizza.

        Аргументы:
        - size: Размер пиццы
        - ingredients: Список с ингредиентами пиццы
        """
        self.size = size
        self.ingredients = ingredients

    def __dict__(self) -> Dict[str, List[str]]:
        """
        Возвращает словарь с размером и списком ингредиентов для пиццы.
        """
        return {
            'size': self.size,
            'ingredients': self.ingredients
        }

    def __eq__(self, other) -> bool:
        """
        Сравнивает две пиццы между собой.

        Аргументы:
        - other: Другой объект типа Pizza для сравнения
        """
        if not isinstance(other, Pizza):
            raise ValueError('Invalid type')
        else:
            return (
                    self.size == other.size
                    and self.ingredients == other.ingredients
            )


class Margherita(Pizza):
    """ Класс для пиццы Маргарита """

    ingredients = ['tomato sauce', 'mozzarella', 'tomatoes']

    def __init__(self, size: str):
        super().__init__(size, self.ingredients)


class Pepperoni(Pizza):
    """ Класс для пиццы Пепперони """

    ingredients = ['tomato sauce', 'mozzarella', 'pepperoni']

    def __init__(self, size: str):
        super().__init__(size, self.ingredients)


class Hawaiian(Pizza):
    """ Класс для пиццы Гавайская """

    ingredients = ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']

    def __init__(self, size: str):
        super().__init__(size, self.ingredients)
