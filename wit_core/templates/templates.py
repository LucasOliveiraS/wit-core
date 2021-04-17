from typing import Any

from ..core.utils import load_module


def execute_template_function(func, arg=None) -> Any:
    action_module = load_module("templates", "templates.py")

    if getattr(action_module, func, None) is None:
        raise AttributeError("Not found template to execute")

    try:
        if not arg:
            return getattr(action_module, func)()
        else:
            return getattr(action_module, func)(arg)
    except Exception as error:
        return error
