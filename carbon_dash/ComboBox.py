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


class ComboBox(Component):
    """A ComboBox component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional)

- allowCustomValue (boolean; default False)

- className (string; optional)

- direction (a value equal to: 'top', 'bottom'; default 'bottom')

- disabled (boolean; default False)

- helperText (a list of or a singular dash component, string or number; optional)

- invalid (boolean; default False)

- invalidText (a list of or a singular dash component, string or number; optional)

- items (list; optional)

- labelText (a list of or a singular dash component, string or number; optional)

- light (boolean; optional)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- persisted_props (list of strings; optional)

- persistence (boolean | string | number; optional)

- persistence_type (a value equal to: 'local', 'session', 'memory'; optional)

- placeholder (string; optional)

- selectedItem (boolean | number | string | dict | list; optional)

- size (a value equal to: 'sm', 'md', 'lg'; default 'md')

- titleText (a list of or a singular dash component, string or number; optional)

- warn (boolean; default False)

- warnText (a list of or a singular dash component, string or number; optional)"""
    _children_props: typing.List[str] = ['labelText', 'titleText', 'helperText', 'invalidText', 'warnText']
    _base_nodes = ['labelText', 'titleText', 'helperText', 'invalidText', 'warnText', 'children']
    _namespace = 'carbon_dash'
    _type = 'ComboBox'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        items: typing.Optional[typing.Sequence] = None,
        selectedItem: typing.Optional[typing.Any] = None,
        labelText: typing.Optional[ComponentType] = None,
        titleText: typing.Optional[ComponentType] = None,
        helperText: typing.Optional[ComponentType] = None,
        placeholder: typing.Optional[str] = None,
        disabled: typing.Optional[bool] = None,
        invalid: typing.Optional[bool] = None,
        invalidText: typing.Optional[ComponentType] = None,
        warn: typing.Optional[bool] = None,
        warnText: typing.Optional[ComponentType] = None,
        allowCustomValue: typing.Optional[bool] = None,
        size: typing.Optional[typing.Optional[str]] = None,
        light: typing.Optional[bool] = None,
        direction: typing.Optional[Literal["top", "bottom"]] = None,
        persistence: typing.Optional[typing.Union[bool, str, NumberType]] = None,
        persisted_props: typing.Optional[typing.Sequence[str]] = None,
        persistence_type: typing.Optional[Literal["local", "session", "memory"]] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'allowCustomValue', 'className', 'direction', 'disabled', 'helperText', 'invalid', 'invalidText', 'items', 'labelText', 'light', 'loading_state', 'persisted_props', 'persistence', 'persistence_type', 'placeholder', 'selectedItem', 'size', 'style', 'titleText', 'warn', 'warnText']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'allowCustomValue', 'className', 'direction', 'disabled', 'helperText', 'invalid', 'invalidText', 'items', 'labelText', 'light', 'loading_state', 'persisted_props', 'persistence', 'persistence_type', 'placeholder', 'selectedItem', 'size', 'style', 'titleText', 'warn', 'warnText']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(ComboBox, self).__init__(children=children, **args)

setattr(ComboBox, "__init__", _explicitize_args(ComboBox.__init__))
