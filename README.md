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
``` python3
>>> from aiogram_callback_factory import make_callback_data
>>>
>>> callback_data = make_callback_data(filter_key="test_key", callback_value="test_value")  # callback_value supports strings, numbers, and lists
>>> callback_data
'{"k":"test_key","v":"test_value"}'
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
```
---
`CallbackDataFilter` & `CallbackFactoryMiddleware`
``` python3
from aiogram_callback_factory import CallbackDataFilter, CallbackFactoryMiddleware

@dispatcher.callback_query_handler(callback_data="my_filter_key_for_testing")
async def handle_callback_query(query):
    print(query.data)  # it will output: 'my_value_for_testing'

dispatcher.filters_factory.bind(CallbackDataFilter, event_handlers=[dispatcher.callback_query_handlers])
dispatcher.middleware.setup(CallbackFactoryMiddleware())
```

## Tips
1. For filters values, it is better to use short enums.  
For example:
``` python3
import enum

class CallbackKey(enum.Enum):
      SOME_TEST_KEY = enum.auto()  # CallbackKey.SOME_TEST_KEY.value == 1
      ANOTHER_TEST_KEY = enum.auto()  # CallbackKey.ANOTHER_TEST_KEY.value == 2

# this handler will catch '{"k":1,"v":"some value"}'
@dispatcher.callback_query_handler(callback_data=CallbackKey.SOME_TEST_KEY.value)
async def handle_callback_query(query):
    ...
```
2. Use only ***latin*** characters (as well as numbers, signs, etc.) to create callback_data.
