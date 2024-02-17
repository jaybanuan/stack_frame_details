import inspect
import json
import collections.abc

from typing import Any


exclude_preds = {
    'frame': lambda name, value: (not name.startswith('f_')) or (name in ['f_back', 'f_builtins', 'f_globals', 'f_locals']),
    'f_code': lambda name, value: (not name.startswith('co_')) or (name in ['co_varnames', 'co_cellvars', 'co_freevars', 'co_code', 'co_consts', 'co_names', 'co_lnotab', 'co_linetable'])
}


def default_exclude_pred(name: str, value: Any) -> bool:
    return name.startswith('_')


def __collect_stackframe_details(name: str | None, value: Any) -> None | bool | int | float | str | list | dict:
    if isinstance(value, None | bool | int | float | str):
        return value
    elif isinstance(value, list):
        return [__collect_stackframe_details(None, entry) for entry in value]
    else:
        result: dict[str, Any] = {}

        exclude_pred = exclude_preds[name] if name in exclude_preds else default_exclude_pred
        for n, v in (value.items() if isinstance(value, collections.abc.Mapping) else inspect.getmembers(value)):
            if exclude_pred(n, v):
                continue

            result[n] = __collect_stackframe_details(n, v)

        return result


def collect_stackframe_details() -> list:
    result = []

    for stack_frame in inspect.stack():
        result.append(__collect_stackframe_details(None, stack_frame))

    return result


print(json.dumps(collect_stackframe_details(), indent=4))        
