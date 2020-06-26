from typing import Union

from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import CallbackQuery

from . import factory


class CallbackDataFilter(BoundFilter):

    key = "callback_data"

    def __init__(self, callback_data: Union[str, int]):

        self.callback_data = callback_data

    async def check(self, update: CallbackQuery) -> bool:

        filter_key, _ = factory.parse_callback_data(update.data)
        return filter_key == self.callback_data
