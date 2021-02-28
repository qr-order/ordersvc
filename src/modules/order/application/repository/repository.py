import abc

from sqlalchemy.orm import Session

from modules.order.infrastructure.model import Order


class AbstractRepository(abc.ABC):
    pass


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session: Session):
        self.session = session
        self.item_ids = []

    def add(self, batch):
        self.session.add(batch)
        self.item_ids.append(batch.id)

    def rollback_committed_data(self, model: Order):
        self.session.query(model).filter(model.id.in_(self.item_ids)).delete()
