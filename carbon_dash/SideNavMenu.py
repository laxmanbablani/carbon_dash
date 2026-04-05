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
SideNavMenu is a wrapper for the Carbon SideNavMenu component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- className (string; default ''):
    className.

- defaultExpanded (boolean | number | string | dict | list; optional):
    defaultExpanded.

- isActive (boolean | number | string | dict | list; optional):
    isActive.

- isSideNavExpanded (boolean | number | string | dict | list; optional):
    isSideNavExpanded.

- large (boolean | number | string | dict | list; optional):
    large.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- renderIcon (boolean | number | string | dict | list; optional):
    renderIcon.

- tabIndex (boolean | number | string | dict | list; optional):
    tabIndex.

- title (boolean | number | string | dict | list; optional):
    title."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'SideNavMenu'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        defaultExpanded: typing.Optional[typing.Any] = None,
        isActive: typing.Optional[typing.Any] = None,
        isSideNavExpanded: typing.Optional[typing.Any] = None,
        large: typing.Optional[typing.Any] = None,
        renderIcon: typing.Optional[typing.Any] = None,
        tabIndex: typing.Optional[typing.Any] = None,
        title: typing.Optional[typing.Any] = None,
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
