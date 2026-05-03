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


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional)

- className (string; optional)

- disabled (boolean; default False):
    Whether disabled.

- helperText (a list of or a singular dash component, string or number; optional):
    Helper text.

- invalid (boolean; optional):
    Whether invalid.

- invalidText (a list of or a singular dash component, string or number; optional):
    Invalid text.

- labelText (a list of or a singular dash component, string or number; optional):
    Label text.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- pattern (string; optional):
    Format pattern.

- placeholder (string; optional):
    Placeholder text.

- size (a value equal to: 'sm', 'md', 'lg'; default 'md'):
    Input size.

- type (string; optional):
    DatePickerInput type."""
    _children_props: typing.List[str] = ['labelText', 'helperText', 'invalidText']
    _base_nodes = ['labelText', 'helperText', 'invalidText', 'children']
    _namespace = 'carbon_dash'
    _type = 'DatePickerInput'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        labelText: typing.Optional[ComponentType] = None,
        placeholder: typing.Optional[str] = None,
        helperText: typing.Optional[ComponentType] = None,
        disabled: typing.Optional[bool] = None,
        invalid: typing.Optional[bool] = None,
        invalidText: typing.Optional[ComponentType] = None,
        size: typing.Optional[typing.Optional[str]] = None,
        pattern: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'disabled', 'helperText', 'invalid', 'invalidText', 'labelText', 'loading_state', 'pattern', 'placeholder', 'size', 'style', 'type']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'disabled', 'helperText', 'invalid', 'invalidText', 'labelText', 'loading_state', 'pattern', 'placeholder', 'size', 'style', 'type']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(DatePickerInput, self).__init__(children=children, **args)

setattr(DatePickerInput, "__init__", _explicitize_args(DatePickerInput.__init__))
