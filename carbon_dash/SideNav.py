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


class SideNav(Component):
    """A SideNav component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The content of the side navigation.

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- addFocusListeners (boolean; default True):
    Specify whether focus and blur listeners are added. They are by
    default.

- addMouseListeners (boolean; default True):
    Specify whether mouse entry/exit listeners are added. They are by
    default.

- ariaLabel (string; optional):
    Required props for accessibility label on the underlying menu.
    Provide an aria-label.

- ariaLabelledBy (string; optional):
    Required props for accessibility label on the underlying menu.
    Provide an aria-labelledby.

- className (string; optional):
    Custom CSS class.

- defaultExpanded (boolean; optional):
    If `True`, the SideNav will be open on initial render.

- enterDelayMs (number; optional):
    Specify the duration in milliseconds to delay before displaying
    the side navigation.

- expanded (boolean; default True):
    If `True`, the SideNav will be expanded, otherwise it will be
    collapsed. Using this prop causes SideNav to become a controlled
    component.

- href (string; optional):
    Provide the `href` to the id of the element on your package that
    is the main content.

- isChildOfHeader (boolean; default True):
    Specify if sideNav is a child of the header.

- isFixedNav (boolean; default False):
    Specify if sideNav is standalone.

- isPersistent (boolean; default True):
    Specify if the sideNav will be persistent above the lg breakpoint.

- isRail (boolean; default False):
    Optional prop to display the side nav rail.

- loading_state (dict; optional):
    Dash loading state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)"""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'SideNav'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        ariaLabel: typing.Optional[str] = None,
        ariaLabelledBy: typing.Optional[str] = None,
        addFocusListeners: typing.Optional[bool] = None,
        addMouseListeners: typing.Optional[bool] = None,
        defaultExpanded: typing.Optional[bool] = None,
        enterDelayMs: typing.Optional[NumberType] = None,
        expanded: typing.Optional[bool] = None,
        href: typing.Optional[str] = None,
        isChildOfHeader: typing.Optional[bool] = None,
        isFixedNav: typing.Optional[bool] = None,
        isPersistent: typing.Optional[bool] = None,
        isRail: typing.Optional[bool] = None,
        onOverlayClick: typing.Optional[typing.Any] = None,
        onSideNavBlur: typing.Optional[typing.Any] = None,
        onToggle: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'addFocusListeners', 'addMouseListeners', 'ariaLabel', 'ariaLabelledBy', 'className', 'defaultExpanded', 'enterDelayMs', 'expanded', 'href', 'isChildOfHeader', 'isFixedNav', 'isPersistent', 'isRail', 'loading_state', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'addFocusListeners', 'addMouseListeners', 'ariaLabel', 'ariaLabelledBy', 'className', 'defaultExpanded', 'enterDelayMs', 'expanded', 'href', 'isChildOfHeader', 'isFixedNav', 'isPersistent', 'isRail', 'loading_state', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(SideNav, self).__init__(children=children, **args)

setattr(SideNav, "__init__", _explicitize_args(SideNav.__init__))
