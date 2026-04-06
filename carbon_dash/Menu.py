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


class Menu(Component):
    """A Menu component.
Menu is a wrapper for the Carbon Menu component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- backgroundToken (boolean | number | string | dict | list; optional):
    backgroundToken.

- border (boolean | number | string | dict | list; optional):
    border.

- className (string; default ''):
    className.

- label (boolean | number | string | dict | list; optional):
    label.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- menuAlignment (boolean | number | string | dict | list; optional):
    menuAlignment.

- mode (boolean | number | string | dict | list; optional):
    mode.

- onClose (boolean | number | string | dict | list; optional):
    onClose.

- onOpen (boolean | number | string | dict | list; optional):
    onOpen.

- open (boolean; default False):
    open.

- size (boolean | number | string | dict | list; optional):
    size.

- target (boolean | number | string | dict | list; optional):
    target.

- x (boolean | number | string | dict | list; optional):
    x.

- y (boolean | number | string | dict | list; optional):
    y."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'Menu'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        backgroundToken: typing.Optional[typing.Any] = None,
        border: typing.Optional[typing.Any] = None,
        label: typing.Optional[typing.Any] = None,
        menuAlignment: typing.Optional[typing.Any] = None,
        mode: typing.Optional[typing.Any] = None,
        onClose: typing.Optional[typing.Any] = None,
        onOpen: typing.Optional[typing.Any] = None,
        open: typing.Optional[bool] = None,
        size: typing.Optional[typing.Optional[str]] = None,
        target: typing.Optional[typing.Any] = None,
        x: typing.Optional[typing.Any] = None,
        y: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'backgroundToken', 'border', 'className', 'label', 'loading_state', 'menuAlignment', 'mode', 'onClose', 'onOpen', 'open', 'size', 'style', 'target', 'x', 'y']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'backgroundToken', 'border', 'className', 'label', 'loading_state', 'menuAlignment', 'mode', 'onClose', 'onOpen', 'open', 'size', 'style', 'target', 'x', 'y']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Menu, self).__init__(children=children, **args)

setattr(Menu, "__init__", _explicitize_args(Menu.__init__))
