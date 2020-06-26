from typing import Union, Tuple
import json as jsonlib

from .exceptions import CallbackDataIsTooLongError


def make_callback_data(filter_key: Union[str, int],
                       callback_value: Union[str, int, list, None] = None) -> str:

    data = {
        "k": filter_key,
        "v": callback_value
    }

    data = jsonlib.dumps(data, separators=(",", ":"), sort_keys=True)

    if isinstance(callback_value, list):
        compacted_value = f"[{','.join(str(i) for i in callback_value)}]"
        data = data.replace(str(callback_value), compacted_value, 1)

    length_data = len(data.encode())
    if length_data > 64:
        raise CallbackDataIsTooLongError(f"resulted callback data is too long: '{data}' ({length_data})")

    return data


def parse_callback_data(data: str) -> Tuple[Union[str, int], Union[str, int, list, None]]:

    dump = jsonlib.loads(data)
    filter_key = dump["k"]
    callback_value = dump["v"]

    return filter_key, callback_value
