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
SideNav is a wrapper for the Carbon SideNav component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- addFocusListeners (boolean | number | string | dict | list; optional):
    addFocusListeners.

- addMouseListeners (boolean | number | string | dict | list; optional):
    addMouseListeners.

- className (string; default ''):
    className.

- defaultExpanded (boolean | number | string | dict | list; optional):
    defaultExpanded.

- enterDelayMs (boolean | number | string | dict | list; optional):
    enterDelayMs.

- expanded (boolean | number | string | dict | list; optional):
    expanded.

- href (boolean | number | string | dict | list; optional):
    href.

- isChildOfHeader (boolean | number | string | dict | list; optional):
    isChildOfHeader.

- isFixedNav (boolean | number | string | dict | list; optional):
    isFixedNav.

- isPersistent (boolean | number | string | dict | list; optional):
    isPersistent.

- isRail (boolean | number | string | dict | list; optional):
    isRail.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- onOverlayClick (boolean | number | string | dict | list; optional):
    onOverlayClick.

- onSideNavBlur (boolean | number | string | dict | list; optional):
    onSideNavBlur.

- onToggle (boolean | number | string | dict | list; optional):
    onToggle."""
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
        addFocusListeners: typing.Optional[typing.Any] = None,
        addMouseListeners: typing.Optional[typing.Any] = None,
        defaultExpanded: typing.Optional[typing.Any] = None,
        enterDelayMs: typing.Optional[typing.Any] = None,
        expanded: typing.Optional[typing.Any] = None,
        href: typing.Optional[typing.Any] = None,
        isChildOfHeader: typing.Optional[typing.Any] = None,
        isFixedNav: typing.Optional[typing.Any] = None,
        isPersistent: typing.Optional[typing.Any] = None,
        isRail: typing.Optional[typing.Any] = None,
        onOverlayClick: typing.Optional[typing.Any] = None,
        onSideNavBlur: typing.Optional[typing.Any] = None,
        onToggle: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'addFocusListeners', 'addMouseListeners', 'className', 'defaultExpanded', 'enterDelayMs', 'expanded', 'href', 'isChildOfHeader', 'isFixedNav', 'isPersistent', 'isRail', 'loading_state', 'onOverlayClick', 'onSideNavBlur', 'onToggle', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'addFocusListeners', 'addMouseListeners', 'className', 'defaultExpanded', 'enterDelayMs', 'expanded', 'href', 'isChildOfHeader', 'isFixedNav', 'isPersistent', 'isRail', 'loading_state', 'onOverlayClick', 'onSideNavBlur', 'onToggle', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(SideNav, self).__init__(children=children, **args)

setattr(SideNav, "__init__", _explicitize_args(SideNav.__init__))
