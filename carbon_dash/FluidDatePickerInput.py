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


class FluidDatePickerInput(Component):
    """A FluidDatePickerInput component.
FluidDatePickerInput is a full-width date picker input component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The content of the date picker input.

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- className (string; optional):
    Custom CSS class.

- dateFormat (string; default 'm/d/Y'):
    Specify the date format.

- disabled (boolean; default False):
    Specify whether the control is disabled.

- labelText (a list of or a singular dash component, string or number; optional):
    Provide the label text for the date picker input.

- loading_state (dict; optional):
    Dash loading state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- pattern (string; default '\\d{1,2}/\\d{1,2}/\\d{4}'):
    Specify the pattern for the date input.

- persisted_props (list of strings; optional)

- persistence (boolean | string | number; optional):
    Persistence settings.

- persistence_type (a value equal to: 'local', 'session', 'memory'; optional)

- placeholder (string; default 'mm/dd/yyyy'):
    Provide the placeholder text for the date picker input."""
    _children_props: typing.List[str] = ['labelText']
    _base_nodes = ['labelText', 'children']
    _namespace = 'carbon_dash'
    _type = 'FluidDatePickerInput'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        placeholder: typing.Optional[str] = None,
        labelText: typing.Optional[ComponentType] = None,
        dateFormat: typing.Optional[str] = None,
        pattern: typing.Optional[str] = None,
        disabled: typing.Optional[bool] = None,
        persistence: typing.Optional[typing.Union[bool, str, NumberType]] = None,
        persisted_props: typing.Optional[typing.Sequence[str]] = None,
        persistence_type: typing.Optional[Literal["local", "session", "memory"]] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'dateFormat', 'disabled', 'labelText', 'loading_state', 'pattern', 'persisted_props', 'persistence', 'persistence_type', 'placeholder', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'dateFormat', 'disabled', 'labelText', 'loading_state', 'pattern', 'persisted_props', 'persistence', 'persistence_type', 'placeholder', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FluidDatePickerInput, self).__init__(children=children, **args)

setattr(FluidDatePickerInput, "__init__", _explicitize_args(FluidDatePickerInput.__init__))
