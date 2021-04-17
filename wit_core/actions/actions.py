from typing import Any

from ..core.utils import load_module


def execute_action_function(func, arg=None) -> Any:
    action_module = load_module("actions", "actions.py")

    if getattr(action_module, func, None) is None:
        raise AttributeError("Not found action to execute")

    try:
        if not arg:
            return getattr(action_module, func)()
        else:
            return getattr(action_module, func)(arg)
    except Exception as error:
        return error
