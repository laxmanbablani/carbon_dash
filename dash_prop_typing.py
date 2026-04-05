"""
This file is automatically loaded at build time to generate custom Python types for Dash 3.0+.
"""

def str_num_prop(*_):
    return "typing.Union[str, NumberType]"

def str_prop(*_):
    return "typing.Optional[str]"

def bool_prop(*_):
    return "typing.Optional[bool]"

def dict_prop(*_):
    return "typing.Optional[typing.Dict[str, typing.Any]]"

def list_prop(*_):
    return "typing.Optional[typing.Sequence[typing.Any]]"

def list_of_strings_prop(*_):
    return "typing.Optional[typing.Sequence[str]]"

def list_dict_prop(*_):
    return "typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]"

default_types = {
    "className": str_prop,
    "id": str_prop,
    "style": dict_prop,
    "size": str_prop,
    "kind": str_prop,
    "color": str_prop,
    "loading_state": dict_prop,
}

custom_props = {
    "*": default_types,
}
