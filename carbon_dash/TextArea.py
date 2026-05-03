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


class TextArea(Component):
    """A TextArea component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional)

- className (string; optional)

- cols (number; default 50)

- disabled (boolean; default False)

- enableCounter (boolean; optional)

- helperText (a list of or a singular dash component, string or number; optional)

- hideLabel (boolean; optional)

- invalid (boolean; optional)

- invalidText (a list of or a singular dash component, string or number; optional)

- labelText (a list of or a singular dash component, string or number; optional)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- maxCount (number; optional)

- persisted_props (list of strings; optional)

- persistence (boolean | string | number; optional)

- persistence_type (a value equal to: 'local', 'session', 'memory'; optional)

- placeholder (string; optional)

- readOnly (boolean; optional)

- rows (number; default 4)

- size (a value equal to: 'sm', 'md', 'lg'; default 'md')

- value (string; optional)

- warn (boolean; optional)

- warnText (a list of or a singular dash component, string or number; optional)"""
    _children_props: typing.List[str] = ['labelText', 'helperText', 'invalidText', 'warnText']
    _base_nodes = ['labelText', 'helperText', 'invalidText', 'warnText', 'children']
    _namespace = 'carbon_dash'
    _type = 'TextArea'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        value: typing.Optional[str] = None,
        labelText: typing.Optional[ComponentType] = None,
        helperText: typing.Optional[ComponentType] = None,
        placeholder: typing.Optional[str] = None,
        rows: typing.Optional[NumberType] = None,
        cols: typing.Optional[NumberType] = None,
        disabled: typing.Optional[bool] = None,
        readOnly: typing.Optional[bool] = None,
        invalid: typing.Optional[bool] = None,
        invalidText: typing.Optional[ComponentType] = None,
        warn: typing.Optional[bool] = None,
        warnText: typing.Optional[ComponentType] = None,
        enableCounter: typing.Optional[bool] = None,
        maxCount: typing.Optional[NumberType] = None,
        hideLabel: typing.Optional[bool] = None,
        size: typing.Optional[typing.Optional[str]] = None,
        persistence: typing.Optional[typing.Union[bool, str, NumberType]] = None,
        persisted_props: typing.Optional[typing.Sequence[str]] = None,
        persistence_type: typing.Optional[Literal["local", "session", "memory"]] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'cols', 'disabled', 'enableCounter', 'helperText', 'hideLabel', 'invalid', 'invalidText', 'labelText', 'loading_state', 'maxCount', 'persisted_props', 'persistence', 'persistence_type', 'placeholder', 'readOnly', 'rows', 'size', 'style', 'value', 'warn', 'warnText']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'cols', 'disabled', 'enableCounter', 'helperText', 'hideLabel', 'invalid', 'invalidText', 'labelText', 'loading_state', 'maxCount', 'persisted_props', 'persistence', 'persistence_type', 'placeholder', 'readOnly', 'rows', 'size', 'style', 'value', 'warn', 'warnText']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(TextArea, self).__init__(children=children, **args)

setattr(TextArea, "__init__", _explicitize_args(TextArea.__init__))
