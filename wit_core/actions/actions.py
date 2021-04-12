import sys
from typing import Any


def execute_action_function(func, arg=None) -> Any:
    if getattr(sys.modules[__name__], func, None) is None:
        raise AttributeError("Not found action to execute")

    try:
        return getattr(sys.modules[__name__], func)(arg)
    except Exception as error:
        return error
