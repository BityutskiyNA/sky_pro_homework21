from cls.storage import Storage


class Request:
    def __init__(self, qw: str, storages: dict[str, Storage]):
        result = qw.lower()
        if len(result) == 0:
            raise BaseException
        result = result.split(' ')
        self.from_sl = result[4]
        self.to = result[6]
        self.amount = int(result[1])
        self.product = result[2]

        if self.to not in storages or self.from_sl not in storages:
            raise BaseException
