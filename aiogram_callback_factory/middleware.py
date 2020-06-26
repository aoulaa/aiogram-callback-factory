from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import CallbackQuery

from . import factory


class CallbackFactoryMiddleware(BaseMiddleware):

    @staticmethod
    async def on_process_callback_query(update: CallbackQuery, _):

        _, callback_value = factory.parse_callback_data(update.data)
        update.data = callback_value
