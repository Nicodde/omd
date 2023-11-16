
## cli.py
Требуется пакет click.

Установить click можно следующим образом:

    pip install click

### Команды для заказа пицц:


Вывести меню:

    python cli.py menu

Заказать пиццу

    python cli.py order <pizza_name> <pizza_size>

Заказать пиццу с доставкой

    python cli.py order <pizza_name> <pizza_size> --delivery

Заказать пиццу с самовывозом

    python cli.py order <pizza_name> <pizza_size> --takeout

## tests.py

Требуется пакет pytest.

Установить pytest можно следующим образом:

    pip install pytest

Для запуска теста запустить команду:

    python -m pytest -v tests.py
