from typing import Union, Optional, List

from flask_sqlalchemy.pagination import QueryPagination

from app import db
from ..models import GoodsModel
from ..utils import DAOMeta


class GoodsDAO(metaclass=DAOMeta):

    @staticmethod
    def create_goods(goods: GoodsModel) -> None:
        db.session.add(goods)
        db.session.commit()

    @staticmethod
    def get_all_goods() -> List[GoodsModel]:
        return db.session.query(GoodsModel).all()

    @staticmethod
    def get_goods_by_id(_id: Union[int, str]) -> Optional[GoodsModel]:
        return db.session.query(GoodsModel).where(GoodsModel.id == str(_id)).first()

    @staticmethod
    def get_goods_by_title(title: str) -> Optional[GoodsModel]:
        return db.session.query(GoodsModel).where(GoodsModel.title == title).first()

    @staticmethod
    def get_goods_with_limit(page: Union[int, str], per_page: Union[int, str]) -> QueryPagination:
        return GoodsModel.query.where(GoodsModel.in_stock > 0).paginate(page=page, per_page=per_page)

    @staticmethod
    def update_goods_by_id(_id: Union[int, str], up_dict: dict) -> None:
        db.session.query(GoodsModel).where(GoodsModel.id == str(_id)).update(up_dict)
        db.session.commit()

    @staticmethod
    def delete_goods_by_id(_id: Union[int, str]) -> None:
        db.session.query(GoodsModel).where(GoodsModel.id == str(_id)).delete()
