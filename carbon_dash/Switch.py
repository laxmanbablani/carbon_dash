# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args

ComponentSingleType = typing.Union[str, int, float, Component, None]
ComponentType = typing.Union[
    ComponentSingleType,
    typing.Sequence[ComponentSingleType],
]

NumberType = typing.Union[
    typing.SupportsFloat, typing.SupportsInt, typing.SupportsComplex
]


class Switch(Component):
    """A Switch component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional)

- className (string; optional)

- disabled (boolean; default False)

- index (number; optional)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- name (string | number; optional)

- selected (boolean; default False)

- text (string; optional)"""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'Switch'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        text: typing.Optional[str] = None,
        name: typing.Optional[typing.Union[str, NumberType]] = None,
        selected: typing.Optional[bool] = None,
        disabled: typing.Optional[bool] = None,
        index: typing.Optional[NumberType] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'disabled', 'index', 'loading_state', 'name', 'selected', 'style', 'text']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'disabled', 'index', 'loading_state', 'name', 'selected', 'style', 'text']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Switch, self).__init__(children=children, **args)

setattr(Switch, "__init__", _explicitize_args(Switch.__init__))
