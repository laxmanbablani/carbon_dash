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


class Popover(Component):
    """A Popover component.
Popover is a wrapper for the Carbon Popover component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- align (boolean | number | string | dict | list; optional):
    align.

- alignmentAxisOffset (boolean | number | string | dict | list; optional):
    alignmentAxisOffset.

- as_ (boolean | number | string | dict | list; optional):
    as.

- autoAlign (boolean | number | string | dict | list; optional):
    autoAlign.

- autoAlignBoundary (boolean | number | string | dict | list; optional):
    autoAlignBoundary.

- backgroundToken (boolean | number | string | dict | list; optional):
    backgroundToken.

- border (boolean | number | string | dict | list; optional):
    border.

- caret (boolean | number | string | dict | list; optional):
    caret.

- className (string; default ''):
    className.

- dropShadow (boolean | number | string | dict | list; optional):
    dropShadow.

- height (boolean | number | string | dict | list; optional):
    height.

- highContrast (boolean | number | string | dict | list; optional):
    highContrast.

- isTabTip (boolean | number | string | dict | list; optional):
    isTabTip.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- onRequestClose (boolean | number | string | dict | list; optional):
    onRequestClose.

- open (boolean; default False):
    open.

- width (boolean | number | string | dict | list; optional):
    width.

- x (boolean | number | string | dict | list; optional):
    x.

- y (boolean | number | string | dict | list; optional):
    y."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'Popover'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        align: typing.Optional[typing.Any] = None,
        alignmentAxisOffset: typing.Optional[typing.Any] = None,
        as_: typing.Optional[typing.Any] = None,
        autoAlign: typing.Optional[typing.Any] = None,
        backgroundToken: typing.Optional[typing.Any] = None,
        autoAlignBoundary: typing.Optional[typing.Any] = None,
        x: typing.Optional[typing.Any] = None,
        y: typing.Optional[typing.Any] = None,
        width: typing.Optional[typing.Any] = None,
        height: typing.Optional[typing.Any] = None,
        caret: typing.Optional[typing.Any] = None,
        border: typing.Optional[typing.Any] = None,
        dropShadow: typing.Optional[typing.Any] = None,
        highContrast: typing.Optional[typing.Any] = None,
        isTabTip: typing.Optional[typing.Any] = None,
        onRequestClose: typing.Optional[typing.Any] = None,
        open: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'align', 'alignmentAxisOffset', 'as_', 'autoAlign', 'autoAlignBoundary', 'backgroundToken', 'border', 'caret', 'className', 'dropShadow', 'height', 'highContrast', 'isTabTip', 'loading_state', 'onRequestClose', 'open', 'style', 'width', 'x', 'y']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'align', 'alignmentAxisOffset', 'as_', 'autoAlign', 'autoAlignBoundary', 'backgroundToken', 'border', 'caret', 'className', 'dropShadow', 'height', 'highContrast', 'isTabTip', 'loading_state', 'onRequestClose', 'open', 'style', 'width', 'x', 'y']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Popover, self).__init__(children=children, **args)

setattr(Popover, "__init__", _explicitize_args(Popover.__init__))
