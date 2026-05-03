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


class HeaderMenu(Component):
    """A HeaderMenu component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional)

- ariaLabel (string; optional):
    Menu link name for accessibility.

- className (string; optional)

- isActive (boolean; optional):
    Whether the menu is active.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- menuLinkName (string; optional):
    The label for the menu."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'HeaderMenu'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        ariaLabel: typing.Optional[str] = None,
        menuLinkName: typing.Optional[str] = None,
        isActive: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'ariaLabel', 'className', 'isActive', 'loading_state', 'menuLinkName', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'ariaLabel', 'className', 'isActive', 'loading_state', 'menuLinkName', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(HeaderMenu, self).__init__(children=children, **args)

setattr(HeaderMenu, "__init__", _explicitize_args(HeaderMenu.__init__))
