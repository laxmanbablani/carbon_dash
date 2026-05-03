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


class TabList(Component):
    """A TabList component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Tab components rendered inside this list.

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- activation (a value equal to: 'automatic', 'manual'; default 'automatic'):
    Specify the activation mode. 'automatic' or 'manual'.

- ariaLabel (string; optional):
    Specify the label used for the tab list aria-label.

- className (string; optional):
    Custom CSS class.

- contained (boolean; default False):
    Specify whether the tab list should be contained.

- fullWidth (boolean; default False):
    Specify whether the tab list should be full width.

- loading_state (dict; optional):
    Dash loading state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)"""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'TabList'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        contained: typing.Optional[bool] = None,
        fullWidth: typing.Optional[bool] = None,
        activation: typing.Optional[Literal["automatic", "manual"]] = None,
        ariaLabel: typing.Optional[str] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'activation', 'ariaLabel', 'className', 'contained', 'fullWidth', 'loading_state', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'activation', 'ariaLabel', 'className', 'contained', 'fullWidth', 'loading_state', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(TabList, self).__init__(children=children, **args)

setattr(TabList, "__init__", _explicitize_args(TabList.__init__))
