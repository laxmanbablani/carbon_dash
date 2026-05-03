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


class DatePicker(Component):
    """A DatePicker component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional)

- className (string; optional)

- dateFormat (string; optional):
    Format pattern for dates.

- datePickerType (a value equal to: 'single', 'range'; default 'single'):
    Date picker type: 'single' or 'range'.

- defaultValue (string | list of strings; optional):
    Default value.

- disabled (boolean; default False):
    Whether disabled.

- light (boolean; default False):
    Light variant.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- locale (string; optional):
    Locale for formatting.

- maxDate (string; optional):
    Maximum date.

- minDate (string; optional):
    Minimum date.

- persisted_props (list of strings; optional)

- persistence (boolean | string | number; optional)

- persistence_type (a value equal to: 'local', 'session', 'memory'; optional)

- readOnly (boolean; default False):
    Whether readonly.

- short (boolean; default False):
    Short style without calendar.

- value (string | list of strings; optional):
    The current date value(s). For single: string. For range: [start,
    end]."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'DatePicker'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        datePickerType: typing.Optional[Literal["single", "range"]] = None,
        value: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        dateFormat: typing.Optional[str] = None,
        defaultValue: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        disabled: typing.Optional[bool] = None,
        readOnly: typing.Optional[bool] = None,
        light: typing.Optional[bool] = None,
        short: typing.Optional[bool] = None,
        minDate: typing.Optional[str] = None,
        maxDate: typing.Optional[str] = None,
        locale: typing.Optional[str] = None,
        persistence: typing.Optional[typing.Union[bool, str, NumberType]] = None,
        persisted_props: typing.Optional[typing.Sequence[str]] = None,
        persistence_type: typing.Optional[Literal["local", "session", "memory"]] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'dateFormat', 'datePickerType', 'defaultValue', 'disabled', 'light', 'loading_state', 'locale', 'maxDate', 'minDate', 'persisted_props', 'persistence', 'persistence_type', 'readOnly', 'short', 'style', 'value']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'dateFormat', 'datePickerType', 'defaultValue', 'disabled', 'light', 'loading_state', 'locale', 'maxDate', 'minDate', 'persisted_props', 'persistence', 'persistence_type', 'readOnly', 'short', 'style', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(DatePicker, self).__init__(children=children, **args)

setattr(DatePicker, "__init__", _explicitize_args(DatePicker.__init__))
