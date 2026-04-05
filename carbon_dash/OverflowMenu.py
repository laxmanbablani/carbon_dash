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


class OverflowMenu(Component):
    """An OverflowMenu component.
OverflowMenu is a wrapper for the Carbon OverflowMenu component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- align (boolean | number | string | dict | list; optional):
    align.

- ariaLabel (boolean | number | string | dict | list; optional):
    ariaLabel.

- className (string; default ''):
    className.

- direction (boolean | number | string | dict | list; optional):
    direction.

- flipped (boolean | number | string | dict | list; optional):
    flipped.

- focusTrap (boolean | number | string | dict | list; optional):
    focusTrap.

- iconClass (boolean | number | string | dict | list; optional):
    iconClass.

- iconDescription (boolean | number | string | dict | list; optional):
    iconDescription.

- left (boolean | number | string | dict | list; optional):
    left.

- light (boolean | number | string | dict | list; optional):
    light.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- menuOffset (boolean | number | string | dict | list; optional):
    menuOffset.

- menuOffsetFlip (boolean | number | string | dict | list; optional):
    menuOffsetFlip.

- menuOptionsClass (boolean | number | string | dict | list; optional):
    menuOptionsClass.

- onClick (boolean | number | string | dict | list; optional):
    onClick.

- onClose (boolean | number | string | dict | list; optional):
    onClose.

- onFocus (boolean | number | string | dict | list; optional):
    onFocus.

- onKeyDown (boolean | number | string | dict | list; optional):
    onKeyDown.

- onOpen (boolean | number | string | dict | list; optional):
    onOpen.

- open (boolean | number | string | dict | list; optional):
    open.

- renderIcon (boolean | number | string | dict | list; optional):
    renderIcon.

- selectorPrimaryFocus (boolean | number | string | dict | list; optional):
    selectorPrimaryFocus.

- size (boolean | number | string | dict | list; optional):
    size.

- top (boolean | number | string | dict | list; optional):
    top."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'OverflowMenu'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        align: typing.Optional[typing.Any] = None,
        ariaLabel: typing.Optional[typing.Any] = None,
        direction: typing.Optional[typing.Any] = None,
        flipped: typing.Optional[typing.Any] = None,
        focusTrap: typing.Optional[typing.Any] = None,
        iconClass: typing.Optional[typing.Any] = None,
        iconDescription: typing.Optional[typing.Any] = None,
        light: typing.Optional[typing.Any] = None,
        menuOffset: typing.Optional[typing.Any] = None,
        top: typing.Optional[typing.Any] = None,
        left: typing.Optional[typing.Any] = None,
        menuOffsetFlip: typing.Optional[typing.Any] = None,
        menuOptionsClass: typing.Optional[typing.Any] = None,
        onClick: typing.Optional[typing.Any] = None,
        onClose: typing.Optional[typing.Any] = None,
        onFocus: typing.Optional[typing.Any] = None,
        onKeyDown: typing.Optional[typing.Any] = None,
        onOpen: typing.Optional[typing.Any] = None,
        open: typing.Optional[typing.Any] = None,
        renderIcon: typing.Optional[typing.Any] = None,
        selectorPrimaryFocus: typing.Optional[typing.Any] = None,
        size: typing.Optional[typing.Optional[str]] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'align', 'ariaLabel', 'className', 'direction', 'flipped', 'focusTrap', 'iconClass', 'iconDescription', 'left', 'light', 'loading_state', 'menuOffset', 'menuOffsetFlip', 'menuOptionsClass', 'onClick', 'onClose', 'onFocus', 'onKeyDown', 'onOpen', 'open', 'renderIcon', 'selectorPrimaryFocus', 'size', 'style', 'top']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'align', 'ariaLabel', 'className', 'direction', 'flipped', 'focusTrap', 'iconClass', 'iconDescription', 'left', 'light', 'loading_state', 'menuOffset', 'menuOffsetFlip', 'menuOptionsClass', 'onClick', 'onClose', 'onFocus', 'onKeyDown', 'onOpen', 'open', 'renderIcon', 'selectorPrimaryFocus', 'size', 'style', 'top']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(OverflowMenu, self).__init__(children=children, **args)

setattr(OverflowMenu, "__init__", _explicitize_args(OverflowMenu.__init__))
