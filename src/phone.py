from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, sim_quantity: int) -> None:
        super().__init__(name, price, quantity)
        self.sim_quantity = sim_quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.sim_quantity})"

    @property
    def number_of_sim(self):
        return self.sim_quantity

    @number_of_sim.setter
    def number_of_sim(self, num):
        '''
        контролируем, чтобы телефон имел целое количество симок и минимум одну
        '''
        if num > 0 and isinstance(num, int):
            self.sim_quantity = num
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')

