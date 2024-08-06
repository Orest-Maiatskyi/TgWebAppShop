from sqlalchemy import DECIMAL

from app import db


class GoodsModel(db.Model):
    __tablename__ = 'goods'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False, default='No description yet...')
    banner = db.Column(db.String(100), nullable=False, default='no-banner.png')
    price = db.Column(DECIMAL(10, 2), nullable=False)
    in_stock = db.Column(db.Integer, nullable=False, default=0)

    def __unicode__(self):
        return str(self.id)

    def __repr__(self):
        return f'Goods - {str(self.id)}'

    def __eq__(self, other: 'GoodsModel') -> bool:
        return self.id == other.id and self.title == other.title
