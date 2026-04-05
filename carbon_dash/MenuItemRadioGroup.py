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


class MenuItemRadioGroup(Component):
    """A MenuItemRadioGroup component.
MenuItemRadioGroup is a wrapper for the Carbon MenuItemRadioGroup component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- className (string; default ''):
    className.

- defaultSelectedItem (boolean | number | string | dict | list; optional):
    defaultSelectedItem.

- itemToString (boolean | number | string | dict | list; optional):
    itemToString.

- items (boolean | number | string | dict | list; optional):
    items.

- label (boolean | number | string | dict | list; optional):
    label.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- onChange (boolean | number | string | dict | list; optional):
    onChange.

- selectedItem (boolean | number | string | dict | list; optional):
    selectedItem."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'MenuItemRadioGroup'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        defaultSelectedItem: typing.Optional[typing.Any] = None,
        itemToString: typing.Optional[typing.Any] = None,
        items: typing.Optional[typing.Any] = None,
        label: typing.Optional[typing.Any] = None,
        onChange: typing.Optional[typing.Any] = None,
        selectedItem: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'defaultSelectedItem', 'itemToString', 'items', 'label', 'loading_state', 'onChange', 'selectedItem', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'defaultSelectedItem', 'itemToString', 'items', 'label', 'loading_state', 'onChange', 'selectedItem', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(MenuItemRadioGroup, self).__init__(children=children, **args)

setattr(MenuItemRadioGroup, "__init__", _explicitize_args(MenuItemRadioGroup.__init__))
