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
SideNavLink is a wrapper for the Carbon SideNavLink component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- as_ (boolean | number | string | dict | list; optional):
    as.

- className (string; default ''):
    className.

- element (boolean | number | string | dict | list; optional):
    element.

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

- renderIcon (a list of or a singular dash component, string or number; optional):
    renderIcon.

- tabIndex (boolean | number | string | dict | list; optional):
    tabIndex."""
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
        as_: typing.Optional[typing.Any] = None,
        element: typing.Optional[typing.Any] = None,
        isSideNavExpanded: typing.Optional[typing.Any] = None,
        isActive: typing.Optional[typing.Any] = None,
        large: typing.Optional[typing.Any] = None,
        renderIcon: typing.Optional[ComponentType] = None,
        tabIndex: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'as_', 'className', 'element', 'isActive', 'isSideNavExpanded', 'large', 'loading_state', 'renderIcon', 'style', 'tabIndex']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'as_', 'className', 'element', 'isActive', 'isSideNavExpanded', 'large', 'loading_state', 'renderIcon', 'style', 'tabIndex']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(SideNavLink, self).__init__(children=children, **args)

setattr(SideNavLink, "__init__", _explicitize_args(SideNavLink.__init__))
