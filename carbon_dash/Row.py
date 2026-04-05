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


class Row(Component):
    """A Row component.
Row is a wrapper for the Carbon Row component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- as_ (boolean | number | string | dict | list; optional):
    as.

- className (string; default ''):
    className.

- condensed (boolean; default False):
    condensed.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- narrow (boolean; default False):
    narrow."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'Row'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        as_: typing.Optional[typing.Any] = None,
        condensed: typing.Optional[bool] = None,
        narrow: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'as_', 'className', 'condensed', 'loading_state', 'narrow', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'as_', 'className', 'condensed', 'loading_state', 'narrow', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Row, self).__init__(children=children, **args)

setattr(Row, "__init__", _explicitize_args(Row.__init__))
