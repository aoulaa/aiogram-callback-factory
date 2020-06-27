# aiogram-callback-factory
Factory for servicing CallbackQuery in Telegram bots.

## Installation
Install with [pip](https://pip.pypa.io/en/stable/):
``` bash
$ pip install git+https://github.com/Abstract-X/aiogram-callback-factory.git
```
**I recommend using a [virtual environment](https://docs.python.org/3.7/library/venv.html).**

## Usage
**The library provides:**
- `make_callback_data`/`parse_callback_data` 
- `CallbackDataFilter` to select a specific CallbackQuery.
- `CallbackFactoryMiddleware` to get a clean callback_data value (no filter prefix).
---
`make_callback_data`  
**Note:** _callback_value supports strings, numbers, and lists._
``` python3
>>> from aiogram_callback_factory import make_callback_data
>>>
>>> callback_data = make_callback_data(filter_key="test_key", callback_value="test_value")
>>> callback_data
'{"k":"test_key","v":"test_value"}'
>>>
>>> callback_data = make_callback_data(filter_key="test_key", callback_value=[111, 222, 333])
>>> callback_data
'{"k":"test_key","v":[111,222,333]}'
```
---
`parse_callback_data`
``` python3
>>> from aiogram_callback_factory import parse_callback_data
>>>
>>> filter_key, callback_value = parse_callback_data('{"k":"test_key","v":"test_value"}')
>>> filter_key
'test_key'
>>> callback_value
'test_value'
>>>
>>> # list
>>> _, callback_value = parse_callback_data('{"k":"test_key","v":[111,222,333]}')
>>> callback_value
[111, 222, 333]
```
---
`CallbackDataFilter` & `CallbackFactoryMiddleware`
``` python3
from aiogram_callback_factory import CallbackDataFilter, CallbackFactoryMiddleware

# setup filter and middleware
dispatcher.filters_factory.bind(CallbackDataFilter, event_handlers=[dispatcher.callback_query_handlers])
dispatcher.middleware.setup(CallbackFactoryMiddleware())

@dispatcher.callback_query_handler(callback_data="my_filter_key_for_testing")
async def handle_callback_query(query):
    print(query.data)  # it will output: 'my_value_for_testing'
```
**Note:** _CallbackFactoryFilter supports `enum.Enum`:_
``` python3
import enum
from aiogram_callback_factory import make_callback_data

class CallbackFilterKey(enum.IntEnum):
    TEST = enum.auto()

# make inline keyboard
keyboard = InlineKeyboardMarkup()
test_button = InlineKeyboardButton(
    text="🔎 Test it!",
    callback_data=make_callback_data(
        filter_key=CallbackFilterKey.TEST,  # enum key
        callback_value="my_value_for_testing"
    )
)
keyboard.row(test_button)

@dispatcher.message_handler()
async def handle_message(message):
    await bot.send_message(chat_id=message.from_user.id, text="Testing?", reply_markup=keyboard)

@dispatcher.callback_query_handler(callback_data=CallbackFilterKey.TEST)  # enum key
async def handle_callback_query(query):
    print(query.data)  # it will output: 'my_value_for_testing'

```

## Tips
1. For filters values, it is better to use short enums.
2. Use only ***latin*** characters (as well as numbers, signs, etc.) to create callback_data.
