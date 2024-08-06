from typing import Type, Tuple, Dict, Any

from .decorators import dao_error_handler


class DAOMeta(type):
    """ MetaClass uses for adding '@dao_error_handler' decorator to all static methods of DAO classes. """

    def __new__(mcs: Type['DAOMeta'], name: str, bases: Tuple[type, ...], dct: Dict[str, Any]) -> Any:
        for k, v in dct.items():
            if isinstance(v, staticmethod):
                dct[k] = staticmethod(dao_error_handler(v.__func__))
        return super().__new__(mcs, name, bases, dct)
