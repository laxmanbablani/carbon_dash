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


class OverflowMenuItem(Component):
    """An OverflowMenuItem component.
OverflowMenuItem is a wrapper for the Carbon OverflowMenuItem component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- className (string; default ''):
    className.

- closeMenu (boolean | number | string | dict | list; optional):
    closeMenu.

- dangerDescription (boolean | number | string | dict | list; optional):
    dangerDescription.

- disabled (boolean | number | string | dict | list; optional):
    disabled.

- handleOverflowMenuItemFocus (boolean | number | string | dict | list; optional):
    handleOverflowMenuItemFocus.

- hasDivider (boolean | number | string | dict | list; optional):
    hasDivider.

- href (boolean | number | string | dict | list; optional):
    href.

- index (boolean | number | string | dict | list; optional):
    index.

- isDelete (boolean | number | string | dict | list; optional):
    isDelete.

- itemText (boolean | number | string | dict | list; optional):
    itemText.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- onBlur (boolean | number | string | dict | list; optional):
    onBlur.

- onClick (boolean | number | string | dict | list; optional):
    onClick.

- onFocus (boolean | number | string | dict | list; optional):
    onFocus.

- onKeyDown (boolean | number | string | dict | list; optional):
    onKeyDown.

- onKeyUp (boolean | number | string | dict | list; optional):
    onKeyUp.

- onMouseDown (boolean | number | string | dict | list; optional):
    onMouseDown.

- onMouseEnter (boolean | number | string | dict | list; optional):
    onMouseEnter.

- onMouseLeave (boolean | number | string | dict | list; optional):
    onMouseLeave.

- onMouseUp (boolean | number | string | dict | list; optional):
    onMouseUp.

- requireTitle (boolean | number | string | dict | list; optional):
    requireTitle.

- title (boolean | number | string | dict | list; optional):
    title.

- wrapperClassName (boolean | number | string | dict | list; optional):
    wrapperClassName."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'OverflowMenuItem'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        closeMenu: typing.Optional[typing.Any] = None,
        dangerDescription: typing.Optional[typing.Any] = None,
        disabled: typing.Optional[typing.Any] = None,
        handleOverflowMenuItemFocus: typing.Optional[typing.Any] = None,
        hasDivider: typing.Optional[typing.Any] = None,
        href: typing.Optional[typing.Any] = None,
        index: typing.Optional[typing.Any] = None,
        isDelete: typing.Optional[typing.Any] = None,
        itemText: typing.Optional[typing.Any] = None,
        onBlur: typing.Optional[typing.Any] = None,
        onClick: typing.Optional[typing.Any] = None,
        onFocus: typing.Optional[typing.Any] = None,
        onKeyDown: typing.Optional[typing.Any] = None,
        onKeyUp: typing.Optional[typing.Any] = None,
        onMouseDown: typing.Optional[typing.Any] = None,
        onMouseEnter: typing.Optional[typing.Any] = None,
        onMouseLeave: typing.Optional[typing.Any] = None,
        onMouseUp: typing.Optional[typing.Any] = None,
        requireTitle: typing.Optional[typing.Any] = None,
        title: typing.Optional[typing.Any] = None,
        wrapperClassName: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'closeMenu', 'dangerDescription', 'disabled', 'handleOverflowMenuItemFocus', 'hasDivider', 'href', 'index', 'isDelete', 'itemText', 'loading_state', 'onBlur', 'onClick', 'onFocus', 'onKeyDown', 'onKeyUp', 'onMouseDown', 'onMouseEnter', 'onMouseLeave', 'onMouseUp', 'requireTitle', 'style', 'title', 'wrapperClassName']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'closeMenu', 'dangerDescription', 'disabled', 'handleOverflowMenuItemFocus', 'hasDivider', 'href', 'index', 'isDelete', 'itemText', 'loading_state', 'onBlur', 'onClick', 'onFocus', 'onKeyDown', 'onKeyUp', 'onMouseDown', 'onMouseEnter', 'onMouseLeave', 'onMouseUp', 'requireTitle', 'style', 'title', 'wrapperClassName']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(OverflowMenuItem, self).__init__(children=children, **args)

setattr(OverflowMenuItem, "__init__", _explicitize_args(OverflowMenuItem.__init__))
