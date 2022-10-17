from cls.request import Request


class Courier:
    def __init__(self, request: Request, storages):
        self.request = request

        if request.from_sl in storages:
            self.from_sl = storages[request.from_sl]

        if request.to in storages:
            self.to = storages[self.request.to]


    def move(self):
        self.from_sl.remove(name=self.request.product, koll= self.request.amount)
        print(f'курьер забрал {self.request.amount} {self.request.product} из {self.request.from_sl}')

        self.to.add(name=self.request.product, koll= self.request.amount)
        print(f'курьер доставил {self.request.amount} {self.request.product} в {self.request.to}')