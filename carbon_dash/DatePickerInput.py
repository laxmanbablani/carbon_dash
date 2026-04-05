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


class DatePickerInput(Component):
    """A DatePickerInput component.
DatePickerInput is a wrapper for the Carbon DatePickerInput component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- className (string; default ''):
    className.

- datePickerType (boolean | number | string | dict | list; optional):
    datePickerType.

- decorator (boolean | number | string | dict | list; optional):
    decorator.

- disabled (boolean | number | string | dict | list; optional):
    disabled.

- helperText (boolean | number | string | dict | list; optional):
    helperText.

- hideLabel (boolean | number | string | dict | list; optional):
    hideLabel.

- invalid (boolean | number | string | dict | list; optional):
    invalid.

- invalidText (boolean | number | string | dict | list; optional):
    invalidText.

- labelText (boolean | number | string | dict | list; optional):
    labelText.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- onChange (boolean | number | string | dict | list; optional):
    onChange.

- onClick (boolean | number | string | dict | list; optional):
    onClick.

- pattern (boolean | number | string | dict | list; optional):
    pattern.

- placeholder (boolean | number | string | dict | list; optional):
    placeholder.

- readOnly (boolean | number | string | dict | list; optional):
    readOnly.

- size (boolean | number | string | dict | list; optional):
    size.

- slug (boolean | number | string | dict | list; optional):
    slug.

- type (boolean | number | string | dict | list; optional):
    type.

- warn (boolean | number | string | dict | list; optional):
    warn.

- warnText (boolean | number | string | dict | list; optional):
    warnText."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'DatePickerInput'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        datePickerType: typing.Optional[typing.Any] = None,
        decorator: typing.Optional[typing.Any] = None,
        disabled: typing.Optional[typing.Any] = None,
        helperText: typing.Optional[typing.Any] = None,
        hideLabel: typing.Optional[typing.Any] = None,
        invalid: typing.Optional[typing.Any] = None,
        invalidText: typing.Optional[typing.Any] = None,
        labelText: typing.Optional[typing.Any] = None,
        onChange: typing.Optional[typing.Any] = None,
        onClick: typing.Optional[typing.Any] = None,
        pattern: typing.Optional[typing.Any] = None,
        placeholder: typing.Optional[typing.Any] = None,
        readOnly: typing.Optional[typing.Any] = None,
        size: typing.Optional[typing.Optional[str]] = None,
        slug: typing.Optional[typing.Any] = None,
        type: typing.Optional[typing.Any] = None,
        warn: typing.Optional[typing.Any] = None,
        warnText: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'datePickerType', 'decorator', 'disabled', 'helperText', 'hideLabel', 'invalid', 'invalidText', 'labelText', 'loading_state', 'onChange', 'onClick', 'pattern', 'placeholder', 'readOnly', 'size', 'slug', 'style', 'type', 'warn', 'warnText']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'datePickerType', 'decorator', 'disabled', 'helperText', 'hideLabel', 'invalid', 'invalidText', 'labelText', 'loading_state', 'onChange', 'onClick', 'pattern', 'placeholder', 'readOnly', 'size', 'slug', 'style', 'type', 'warn', 'warnText']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(DatePickerInput, self).__init__(children=children, **args)

setattr(DatePickerInput, "__init__", _explicitize_args(DatePickerInput.__init__))
