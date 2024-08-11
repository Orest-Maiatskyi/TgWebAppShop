from decimal import Decimal, getcontext
from flask import Flask

from app.config import current_config
from app.extensions import *

from app.database.models import GoodsModel

getcontext().prec = 2

app = Flask(__name__)
app.config.from_object(current_config)

init_extensions(app)


from app.database.models import *
from app.database.dao import *


with app.app_context():
    try:
        import random
        db.drop_all()
        db.create_all()
        for i in range(105):
            GoodsDAO.create_goods(GoodsModel(
                title=f'Test-Title-{i}-egjnogmweoefrsdhrh', 
                banner=f'{random.randint(1, 12)}.png', 
                price=1.99, 
                description="""A method that shows a native popup requesting permission for the bot to send messages to the user. If an optional callback parameter was passed, the callback function will be called when the popup is closed and the first argument will be a boolean indicating whether the user granted this access.A method that shows a native popup requesting permission for the bot to send messages to the user. If an optional callback parameter was passed, the callback function will be called when the popup is closed and the first argument will be a boolean indicating whether the user granted this access.""",
                in_stock=1))
    except Exception as ignore: 
        pass


from app.routes import *
