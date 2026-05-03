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


class SideNavMenu(Component):
    """A SideNavMenu component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Provide SideNavMenuItem's inside of the SideNavMenu.

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- className (string; optional):
    Custom CSS class.

- defaultExpanded (boolean; optional):
    Specify whether the menu should default to expanded. By default,
    it will be closed.

- isActive (boolean; optional):
    Specify whether the SideNavMenu is \"active\". SideNavMenu should
    be considered active if one of its menu items are a link for the
    current page.

- isSideNavExpanded (boolean; optional):
    Property to indicate if the side nav container is open (or not).
    Use to keep local state and styling in step with the SideNav
    expansion state.

- large (boolean; optional):
    Specify if this is a large variation of the SideNavMenu.

- loading_state (dict; optional):
    Dash loading state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- renderIcon (a list of or a singular dash component, string or number; optional):
    An icon component to render in the menu. Accepts DashIconify,
    html.Div, Carbon icon name string, or any React node.

- tabIndex (number; optional):
    Optional prop to specify the tabIndex of the button.

- title (string; optional):
    Provide the text for the overall menu name."""
    _children_props: typing.List[str] = ['renderIcon']
    _base_nodes = ['renderIcon', 'children']
    _namespace = 'carbon_dash'
    _type = 'SideNavMenu'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        defaultExpanded: typing.Optional[bool] = None,
        isActive: typing.Optional[bool] = None,
        isSideNavExpanded: typing.Optional[bool] = None,
        large: typing.Optional[bool] = None,
        renderIcon: typing.Optional[ComponentType] = None,
        tabIndex: typing.Optional[NumberType] = None,
        title: typing.Optional[str] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'defaultExpanded', 'isActive', 'isSideNavExpanded', 'large', 'loading_state', 'renderIcon', 'style', 'tabIndex', 'title']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'defaultExpanded', 'isActive', 'isSideNavExpanded', 'large', 'loading_state', 'renderIcon', 'style', 'tabIndex', 'title']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(SideNavMenu, self).__init__(children=children, **args)

setattr(SideNavMenu, "__init__", _explicitize_args(SideNavMenu.__init__))
