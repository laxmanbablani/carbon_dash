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


class Column(Component):
    """A Column component.
Column is a wrapper for the Carbon Column component.
Provides responsive column spans for each breakpoint.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The content of the column.

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- as (string; optional):
    Provide a custom element to render instead of the default div.

- className (string; optional):
    Custom CSS class.

- lg (optional):
    Specify column span for the lg breakpoint (up to 1312px, 16
    columns).

- loading_state (dict; optional):
    Dash loading state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- max (optional):
    Specify column span for the max breakpoint (16 columns).

- md (optional):
    Specify column span for the md breakpoint (up to 1056px, 8
    columns).

- sm (optional):
    Specify column span for the sm breakpoint (up to 672px, 4
    columns).

- xlg (optional):
    Specify column span for the xlg breakpoint (up to 1584px, 16
    columns)."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'Column'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        sm: typing.Optional[typing.Any] = None,
        md: typing.Optional[typing.Any] = None,
        lg: typing.Optional[typing.Any] = None,
        xlg: typing.Optional[typing.Any] = None,
        max: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'as', 'className', 'lg', 'loading_state', 'max', 'md', 'sm', 'style', 'xlg']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'as', 'className', 'lg', 'loading_state', 'max', 'md', 'sm', 'style', 'xlg']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Column, self).__init__(children=children, **args)

setattr(Column, "__init__", _explicitize_args(Column.__init__))
