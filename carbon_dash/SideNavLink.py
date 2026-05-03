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


class SideNavLink(Component):
    """A SideNavLink component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional)

- ariaLabel (string; optional)

- ariaLabelledBy (string; optional)

- as (optional)

- className (string; optional)

- element (optional)

- href (string; optional)

- isActive (boolean; optional)

- isSideNavExpanded (boolean; optional)

- large (boolean; default False)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- n_clicks (number; default 0)

- renderIcon (a list of or a singular dash component, string or number; optional)

- tabIndex (number; optional)"""
    _children_props: typing.List[str] = ['renderIcon']
    _base_nodes = ['renderIcon', 'children']
    _namespace = 'carbon_dash'
    _type = 'SideNavLink'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        renderIcon: typing.Optional[ComponentType] = None,
        n_clicks: typing.Optional[NumberType] = None,
        href: typing.Optional[str] = None,
        isActive: typing.Optional[bool] = None,
        isSideNavExpanded: typing.Optional[bool] = None,
        large: typing.Optional[bool] = None,
        tabIndex: typing.Optional[NumberType] = None,
        ariaLabel: typing.Optional[str] = None,
        ariaLabelledBy: typing.Optional[str] = None,
        element: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'ariaLabel', 'ariaLabelledBy', 'as', 'className', 'element', 'href', 'isActive', 'isSideNavExpanded', 'large', 'loading_state', 'n_clicks', 'renderIcon', 'style', 'tabIndex']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'ariaLabel', 'ariaLabelledBy', 'as', 'className', 'element', 'href', 'isActive', 'isSideNavExpanded', 'large', 'loading_state', 'n_clicks', 'renderIcon', 'style', 'tabIndex']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(SideNavLink, self).__init__(children=children, **args)

setattr(SideNavLink, "__init__", _explicitize_args(SideNavLink.__init__))
