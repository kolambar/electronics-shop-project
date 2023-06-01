from src.item import Item


class MixinLang:
    def __init__(self, name, price, quantity):
        self.__language = 'EN'
        super().__init__(name, price, quantity)

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
            return self
        else:
            self.__language = 'EN'
            return self


class Keyboard(MixinLang, Item):

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
