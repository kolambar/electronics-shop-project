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

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) < 11:
            self.__name = name


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
        класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv
        '''
        with open(PATH_TO_FILE, newline='', encoding='cp1251') as csvfile:
            reader = DictReader(csvfile)
            list_of_instance = [cls(i['name'], i['price'], i['quantity']) for i in reader]
        return list_of_instance

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
