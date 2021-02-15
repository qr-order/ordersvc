import abc


class AbstractRepository(abc.ABC):
    pass


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, batch):
        self.session.add(batch)

    def update(self, batch):
        self.session.update(batch)
