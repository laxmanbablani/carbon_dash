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


class Dropdown(Component):
    """A Dropdown component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional)

- className (string; optional)

- decorator (a list of or a singular dash component, string or number; optional):
    Whether to show AI label decorator.

- direction (a value equal to: 'top', 'bottom'; default 'bottom'):
    Direction: top or bottom.

- disabled (boolean; default False):
    Whether disabled.

- helperText (a list of or a singular dash component, string or number; optional):
    Helper text.

- inline (boolean; default False):
    Inline variant.

- invalid (boolean; default False):
    Whether invalid.

- invalidText (a list of or a singular dash component, string or number; optional):
    Invalid text.

- items (list; optional):
    List of items to show in the dropdown.

- label (a list of or a singular dash component, string or number; optional):
    Label text displayed above.

- light (boolean; optional):
    Light variant.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- persisted_props (list of strings; optional)

- persistence (boolean | string | number; optional)

- persistence_type (a value equal to: 'local', 'session', 'memory'; optional)

- selectedItem (boolean | number | string | dict | list; optional):
    Currently selected item.

- size (a value equal to: 'sm', 'md', 'lg'; default 'md'):
    Size.

- titleText (a list of or a singular dash component, string or number; optional):
    Title text.

- type (a value equal to: 'default', 'inline'; default 'default'):
    Type: default or inline.

- warn (boolean; default False):
    Whether warn.

- warnText (a list of or a singular dash component, string or number; optional):
    Warn text."""
    _children_props: typing.List[str] = ['label', 'titleText', 'helperText', 'invalidText', 'warnText', 'decorator']
    _base_nodes = ['label', 'titleText', 'helperText', 'invalidText', 'warnText', 'decorator', 'children']
    _namespace = 'carbon_dash'
    _type = 'Dropdown'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        items: typing.Optional[typing.Sequence] = None,
        selectedItem: typing.Optional[typing.Any] = None,
        label: typing.Optional[ComponentType] = None,
        titleText: typing.Optional[ComponentType] = None,
        helperText: typing.Optional[ComponentType] = None,
        disabled: typing.Optional[bool] = None,
        direction: typing.Optional[Literal["top", "bottom"]] = None,
        size: typing.Optional[typing.Optional[str]] = None,
        inline: typing.Optional[bool] = None,
        invalid: typing.Optional[bool] = None,
        invalidText: typing.Optional[ComponentType] = None,
        warn: typing.Optional[bool] = None,
        warnText: typing.Optional[ComponentType] = None,
        light: typing.Optional[bool] = None,
        type: typing.Optional[Literal["default", "inline"]] = None,
        decorator: typing.Optional[ComponentType] = None,
        persistence: typing.Optional[typing.Union[bool, str, NumberType]] = None,
        persisted_props: typing.Optional[typing.Sequence[str]] = None,
        persistence_type: typing.Optional[Literal["local", "session", "memory"]] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'decorator', 'direction', 'disabled', 'helperText', 'inline', 'invalid', 'invalidText', 'items', 'label', 'light', 'loading_state', 'persisted_props', 'persistence', 'persistence_type', 'selectedItem', 'size', 'style', 'titleText', 'type', 'warn', 'warnText']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'decorator', 'direction', 'disabled', 'helperText', 'inline', 'invalid', 'invalidText', 'items', 'label', 'light', 'loading_state', 'persisted_props', 'persistence', 'persistence_type', 'selectedItem', 'size', 'style', 'titleText', 'type', 'warn', 'warnText']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Dropdown, self).__init__(children=children, **args)

setattr(Dropdown, "__init__", _explicitize_args(Dropdown.__init__))
