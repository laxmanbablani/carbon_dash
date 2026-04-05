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
HeaderMenu is a wrapper for the Carbon HeaderMenu component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- className (string; default ''):
    className.

- focusRef (boolean | number | string | dict | list; optional):
    focusRef.

- isActive (boolean | number | string | dict | list; optional):
    isActive.

- isCurrentPage (boolean | number | string | dict | list; optional):
    isCurrentPage.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- menuLinkName (boolean | number | string | dict | list; optional):
    menuLinkName.

- onBlur (boolean | number | string | dict | list; optional):
    onBlur.

- onClick (boolean | number | string | dict | list; optional):
    onClick.

- onKeyDown (boolean | number | string | dict | list; optional):
    onKeyDown.

- renderMenuContent (boolean | number | string | dict | list; optional):
    renderMenuContent.

- tabIndex (boolean | number | string | dict | list; optional):
    tabIndex."""
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
        focusRef: typing.Optional[typing.Any] = None,
        isActive: typing.Optional[typing.Any] = None,
        isCurrentPage: typing.Optional[typing.Any] = None,
        menuLinkName: typing.Optional[typing.Any] = None,
        onBlur: typing.Optional[typing.Any] = None,
        onClick: typing.Optional[typing.Any] = None,
        onKeyDown: typing.Optional[typing.Any] = None,
        renderMenuContent: typing.Optional[typing.Any] = None,
        tabIndex: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'focusRef', 'isActive', 'isCurrentPage', 'loading_state', 'menuLinkName', 'onBlur', 'onClick', 'onKeyDown', 'renderMenuContent', 'style', 'tabIndex']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'focusRef', 'isActive', 'isCurrentPage', 'loading_state', 'menuLinkName', 'onBlur', 'onClick', 'onKeyDown', 'renderMenuContent', 'style', 'tabIndex']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(HeaderMenu, self).__init__(children=children, **args)

setattr(HeaderMenu, "__init__", _explicitize_args(HeaderMenu.__init__))
