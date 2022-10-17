from cls.storage import Storage


class Request:
    def __init__(self, qw: str, storages: dict[str, Storage]):
        rez = qw.lower()
        if len(rez) == 0:
            raise BaseException
        rez = rez.split(' ')
        self.from_sl = rez[4]
        self.to = rez[6]
        self.amount = int(rez[1])
        self.product = rez[2]

        if self.to not in storages or self.from_sl not in storages:
            raise BaseException
