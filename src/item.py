from csv import DictReader
import os


PATH_TO_FILE = os.path.join(os.path.abspath('..'), 'src', 'items.csv')


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        """
        устанавливаем имя товара. следим, тчобы оно было короче 11 символов
        """
        if len(name) < 11:
            self.__name = name
        else:
            raise Exception('Длина наименования товара превышает 10 символов.')

    def __add__(self, other):
        """
        складываем количество товара
        """
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise ValueError('Складывать можно только предметы (Item) с другими предметами (например Phone)')

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate
    @classmethod
    def instantiate_from_csv(cls):
        '''
        класс-метод, инициализирующий экземпляры класса `Item` данными из файла src/items.csv
        '''
        try:
            with open(PATH_TO_FILE, newline='', encoding='cp1251') as csvfile:
                reader = DictReader(csvfile)
                list_of_instance = [cls(i['name'], i['price'], i['quantity']) for i in reader]
                return list_of_instance
        except FileNotFoundError:
            print('Отсутствует файл item.csv')
        except KeyError:
            raise InstantiateCSVError('Файл item.csv поврежден')

    @staticmethod
    def string_to_number(string):
        '''
        статический метод, возвращающий число из числа-строки.
        работает с дробными числами по правилам математики
        '''
        if '.' in string:
            return int(round(float(string)))
        elif string.isdigit():
            return int(string)
        else:
            raise TypeError('Строка не число')


class InstantiateCSVError(Exception):
    pass
