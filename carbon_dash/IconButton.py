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


class IconButton(Component):
    """An IconButton component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional)

- className (string; optional)

- disabled (boolean; default False)

- hasIconOnly (boolean; optional)

- kind (a value equal to: 'primary', 'secondary', 'tertiary', 'ghost', 'danger'; default 'primary')

- label (string; optional)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- n_clicks (number; default 0)

- persisted_props (list of strings; optional)

- persistence (boolean | string | number; optional)

- persistence_type (a value equal to: 'local', 'session', 'memory'; optional)

- renderIcon (a list of or a singular dash component, string or number; optional)

- size (a value equal to: 'sm', 'md', 'lg'; default 'lg')

- tooltipAlignment (string; optional)

- tooltipPosition (string; optional)"""
    _children_props: typing.List[str] = ['renderIcon']
    _base_nodes = ['renderIcon', 'children']
    _namespace = 'carbon_dash'
    _type = 'IconButton'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        renderIcon: typing.Optional[ComponentType] = None,
        n_clicks: typing.Optional[NumberType] = None,
        disabled: typing.Optional[bool] = None,
        kind: typing.Optional[typing.Optional[str]] = None,
        size: typing.Optional[typing.Optional[str]] = None,
        label: typing.Optional[str] = None,
        hasIconOnly: typing.Optional[bool] = None,
        tooltipAlignment: typing.Optional[str] = None,
        tooltipPosition: typing.Optional[str] = None,
        persistence: typing.Optional[typing.Union[bool, str, NumberType]] = None,
        persisted_props: typing.Optional[typing.Sequence[str]] = None,
        persistence_type: typing.Optional[Literal["local", "session", "memory"]] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'disabled', 'hasIconOnly', 'kind', 'label', 'loading_state', 'n_clicks', 'persisted_props', 'persistence', 'persistence_type', 'renderIcon', 'size', 'style', 'tooltipAlignment', 'tooltipPosition']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'disabled', 'hasIconOnly', 'kind', 'label', 'loading_state', 'n_clicks', 'persisted_props', 'persistence', 'persistence_type', 'renderIcon', 'size', 'style', 'tooltipAlignment', 'tooltipPosition']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(IconButton, self).__init__(children=children, **args)

setattr(IconButton, "__init__", _explicitize_args(IconButton.__init__))
