import click
from decorator import log
from pizza import Pizza, Margherita, Pepperoni, Hawaiian


@click.group()
def cli():
    pass


@log('🔥 Приготовили за ')
def baked(pizza: str) -> None:
    pass


@log('🛵 Доставили за ')
def delivered(pizza: str) -> None:
    pass


@log('🏠 Забрали за ')
def pickedup(pizza: str) -> None:
    pass


@cli.command()
def menu():
    """Выводит меню"""
    pizzas = {
        'Margherita 🧀': Margherita,
        'Pepperoni 🍕': Pepperoni,
        'Hawaiian 🍍': Hawaiian
    }

    main_pizza = Pizza

    print('Меню:')
    for pizza_name, pizza_class in pizzas.items():
        print(f"{pizza_name}: {', '.join(pizza_class.ingredients)}")

    print(f"Доступные размеры пиццы: {', '.join(main_pizza.size)}")


@cli.command()
@click.option('--delivery', default=False, is_flag=True, help='Доставка')
@click.option('--takeout', default=False, is_flag=True, help='Самовывоз')
@click.argument('pizza', nargs=1)
@click.argument('size', nargs=1)
def order(delivery: bool, takeout: bool, pizza: str, size: str):
    """
    Заказ пиццы
    """
    orders = {
        'Margherita': Margherita(size),
        'Pepperoni': Pepperoni(size),
        'Hawaiian': Hawaiian(size)
    }

    sizes = Pizza.size
    size_upper = size.upper()
    pizza_title = pizza.title()

    if pizza_title not in orders:
        print(
            '''
            Мы пока еще не умеем готовить такую пиццу :(
            Выберите, пожалуйста, из доступных пицц. Спасибо!
            '''
            )
        return

    if size_upper not in sizes:
        print(
            '''
            Такого размера нет:(
            Выберите, пожалуйста, доступный размер. Спасибо!
            '''
            )
        return

    if delivery:
        baked(orders[pizza_title])
        delivered(orders[pizza_title])
        print('✨ Заказ доставлен! Приятного аппетита! ✨')

    elif takeout:
        baked(orders[pizza_title])
        pickedup(orders[pizza_title])
        print('✨ Спасибо, что пользуетесь самовывозом! Приятного аппетита! ✨')

    else:
        baked(orders[pizza_title])
        print('✨ Ваша пицца готова! Приятного аппетита! ✨')


if __name__ == '__main__':
    cli()
