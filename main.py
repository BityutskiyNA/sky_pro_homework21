from cls.courier import Courier
from cls.request import Request
from cls.shop import Shop
from cls.store import Store

store = Store(items={
    'печеньки': 10,
    'бисквит': 3,
    'сок': 5,
    'кола': 2,
})

shop = Shop(items={
    'печеньки': 1,
    'кола': 1,
})


storages = {
    'магазин': shop,
    'склад': store,
}


def main():
    while True:
        for st_name in storages:
            print(f'На складе {st_name}: \n {storages[st_name].get_items()}')

        user_input = input(
            'Введите строчку в формате Доставить 3 печеньки из склад в магазин \n'
            'Введите стоп для прекращения программы\n'
        )
        if user_input == 'стоп':
            break

        try:
            rek = Request(user_input, storages)
        except BaseException:
            continue
        courier = Courier(rek, storages)

        try:
            courier.move()
        except BaseException:
            continue

if __name__ == '__main__':
    main()
