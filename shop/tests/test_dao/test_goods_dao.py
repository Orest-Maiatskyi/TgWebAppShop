from unittest import TestCase, main

from app import *
from app.database.dao import *


class GoodsDAOTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        if current_config.__name__ != 'TestConfig':
            raise Exception('CURRENT CONFIG IS NOT FOR TESTING, EDIT config.py FIRST!')

    def setUp(self):
        with app.app_context():
            db.drop_all()
            db.create_all()

    def test_create_goods(self):
        with app.app_context():
            self.assertEqual(GoodsDAO.get_goods_by_id(1), None)
            GoodsDAO.create_goods(GoodsModel(title='test-title', price=999.99))
            self.assertEqual(GoodsDAO.get_goods_by_id(1),
                             GoodsModel(id=1, title='test-title', price=999.99))

    def test_get_all_goods(self):
        with app.app_context():
            for i in range(10):
                GoodsDAO.create_goods(GoodsModel(title=f'test-title-{i}', price=999.99))
            self.assertEqual(GoodsDAO.get_all_goods(),
                             [GoodsModel(id=i+1, title=f'test-title-{i}', price=999.99) for i in range(10)])

    def test_get_goods_by_id(self):
        with app.app_context():
            GoodsDAO.create_goods(GoodsModel(title='test-title', price=999.99))
            self.assertEqual(GoodsDAO.get_goods_by_id(1),
                             GoodsModel(id=1, title='test-title', price=999.99))

    def test_get_goods_by_title(self):
        with app.app_context():
            GoodsDAO.create_goods(GoodsModel(title='test-title', price=999.99))
            self.assertEqual(GoodsDAO.get_goods_by_title('test-title'),
                             GoodsModel(id=1, title='test-title', price=999.99))

    def test_update_goods_by_id(self):
        with app.app_context():
            GoodsDAO.create_goods(GoodsModel(title='test-title', price=999.99))
            self.assertEqual(GoodsDAO.get_goods_by_id(1),
                             GoodsModel(id=1, title='test-title', price=999.99))
            GoodsDAO.update_goods_by_id(1, {'title': 'updated-test-title'})
            self.assertEqual(GoodsDAO.get_goods_by_id(1),
                             GoodsModel(id=1, title='updated-test-title', price=999.99))

    def test_delete_goods_by_id(self):
        with app.app_context():
            GoodsDAO.create_goods(GoodsModel(title='test-title', price=999.99))
            self.assertEqual(GoodsDAO.get_goods_by_id(1),
                             GoodsModel(id=1, title='test-title', price=999.99))
            GoodsDAO.delete_goods_by_id(1)
            self.assertEqual(GoodsDAO.get_goods_by_id(1), None)

    def tearDown(self):
        with app.app_context():
            db.drop_all()


if __name__ == "__main__":
    main()
