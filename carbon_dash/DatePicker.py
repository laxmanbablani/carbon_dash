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
DatePicker is a wrapper for the Carbon DatePicker component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- allowInput (boolean | number | string | dict | list; optional):
    allowInput.

- appendTo (boolean | number | string | dict | list; optional):
    appendTo.

- className (string; default ''):
    className.

- closeOnSelect (boolean | number | string | dict | list; optional):
    closeOnSelect.

- dateFormat (boolean | number | string | dict | list; optional):
    dateFormat.

- datePickerType (string; default 'single'):
    datePickerType.

- debounce (boolean | number; optional):
    debounce.

- disable (boolean | number | string | dict | list; optional):
    disable.

- enable (boolean | number | string | dict | list; optional):
    enable.

- inline (boolean | number | string | dict | list; optional):
    inline.

- invalid (boolean | number | string | dict | list; optional):
    invalid.

- invalidText (boolean | number | string | dict | list; optional):
    invalidText.

- light (boolean | number | string | dict | list; optional):
    light.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- locale (boolean | number | string | dict | list; optional):
    locale.

- maxDate (boolean | number | string | dict | list; optional):
    maxDate.

- minDate (boolean | number | string | dict | list; optional):
    minDate.

- n_blur (number; optional):
    n_blur.

- n_submit (number; optional):
    n_submit.

- nextMonthAriaLabel (boolean | number | string | dict | list; optional):
    nextMonthAriaLabel.

- onChange (boolean | number | string | dict | list; optional):
    onChange.

- onClose (boolean | number | string | dict | list; optional):
    onClose.

- onOpen (boolean | number | string | dict | list; optional):
    onOpen.

- parseDate (boolean | number | string | dict | list; optional):
    parseDate.

- persisted_props (list of strings; optional):
    persisted_props.

- persistence (boolean | string | number; optional):
    persistence.

- persistence_type (a value equal to: 'local', 'session', 'memory'; optional):
    persistence_type.

- prevMonthAriaLabel (boolean | number | string | dict | list; optional):
    prevMonthAriaLabel.

- readOnly (boolean | number | string | dict | list; optional):
    readOnly.

- short (boolean | number | string | dict | list; optional):
    short.

- value (boolean | number | string | dict | list; optional):
    value.

- warn (boolean | number | string | dict | list; optional):
    warn.

- warnText (boolean | number | string | dict | list; optional):
    warnText."""
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
        persistence: typing.Optional[typing.Union[bool, str, NumberType]] = None,
        persisted_props: typing.Optional[typing.Sequence[str]] = None,
        persistence_type: typing.Optional[Literal["local", "session", "memory"]] = None,
        n_blur: typing.Optional[NumberType] = None,
        n_submit: typing.Optional[NumberType] = None,
        debounce: typing.Optional[typing.Union[bool, NumberType]] = None,
        allowInput: typing.Optional[typing.Any] = None,
        appendTo: typing.Optional[typing.Any] = None,
        closeOnSelect: typing.Optional[typing.Any] = None,
        dateFormat: typing.Optional[typing.Any] = None,
        datePickerType: typing.Optional[str] = None,
        disable: typing.Optional[typing.Any] = None,
        enable: typing.Optional[typing.Any] = None,
        inline: typing.Optional[typing.Any] = None,
        invalid: typing.Optional[typing.Any] = None,
        light: typing.Optional[typing.Any] = None,
        locale: typing.Optional[typing.Any] = None,
        maxDate: typing.Optional[typing.Any] = None,
        minDate: typing.Optional[typing.Any] = None,
        onChange: typing.Optional[typing.Any] = None,
        onClose: typing.Optional[typing.Any] = None,
        onOpen: typing.Optional[typing.Any] = None,
        parseDate: typing.Optional[typing.Any] = None,
        readOnly: typing.Optional[typing.Any] = None,
        short: typing.Optional[typing.Any] = None,
        value: typing.Optional[typing.Any] = None,
        warn: typing.Optional[typing.Any] = None,
        nextMonthAriaLabel: typing.Optional[typing.Any] = None,
        prevMonthAriaLabel: typing.Optional[typing.Any] = None,
        invalidText: typing.Optional[typing.Any] = None,
        warnText: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'allowInput', 'appendTo', 'className', 'closeOnSelect', 'dateFormat', 'datePickerType', 'debounce', 'disable', 'enable', 'inline', 'invalid', 'invalidText', 'light', 'loading_state', 'locale', 'maxDate', 'minDate', 'n_blur', 'n_submit', 'nextMonthAriaLabel', 'onChange', 'onClose', 'onOpen', 'parseDate', 'persisted_props', 'persistence', 'persistence_type', 'prevMonthAriaLabel', 'readOnly', 'short', 'style', 'value', 'warn', 'warnText']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'allowInput', 'appendTo', 'className', 'closeOnSelect', 'dateFormat', 'datePickerType', 'debounce', 'disable', 'enable', 'inline', 'invalid', 'invalidText', 'light', 'loading_state', 'locale', 'maxDate', 'minDate', 'n_blur', 'n_submit', 'nextMonthAriaLabel', 'onChange', 'onClose', 'onOpen', 'parseDate', 'persisted_props', 'persistence', 'persistence_type', 'prevMonthAriaLabel', 'readOnly', 'short', 'style', 'value', 'warn', 'warnText']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(DatePicker, self).__init__(children=children, **args)

setattr(DatePicker, "__init__", _explicitize_args(DatePicker.__init__))
