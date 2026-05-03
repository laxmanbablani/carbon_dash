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


class Tabs(Component):
    """A Tabs component.
Tabs is a wrapper for the Carbon Tabs component.
Provides a tabbed interface for organizing content.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The content of the tabs (should contain TabList and TabPanels).

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- className (string; optional):
    Custom CSS class.

- defaultSelectedIndex (number; default 0):
    Specify which content tab should be initially selected when the
    component is first rendered.

- dismissable (boolean; optional):
    Whether the rendered Tab children should be dismissable.

- loading_state (dict; optional):
    Dash loading state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- selectedIndex (number; optional):
    Control which content panel is currently selected."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'Tabs'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        selectedIndex: typing.Optional[NumberType] = None,
        defaultSelectedIndex: typing.Optional[NumberType] = None,
        dismissable: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'defaultSelectedIndex', 'dismissable', 'loading_state', 'selectedIndex', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'defaultSelectedIndex', 'dismissable', 'loading_state', 'selectedIndex', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Tabs, self).__init__(children=children, **args)

setattr(Tabs, "__init__", _explicitize_args(Tabs.__init__))
