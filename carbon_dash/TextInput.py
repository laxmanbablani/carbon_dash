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


class TextInput(Component):
    """A TextInput component.
TextInput is a wrapper for the Carbon TextInput component.
Supports label, placeholder, helper text, invalid/warn states, and AI label decorator.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The content of the text input (used as label fallback if labelText
    not provided).

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- aiLabel (boolean; default False):
    Whether to render the AI label decorator.

- className (string; optional):
    Custom CSS class.

- defaultValue (string | number; optional):
    Default value (for uncontrolled mode).

- disabled (boolean; default False):
    Whether the input is disabled.

- enableCounter (boolean; optional):
    Whether to display the character counter.

- helperText (a list of or a singular dash component, string or number; optional):
    Input helper text.

- hideLabel (boolean; default False):
    Whether to hide the label.

- invalid (boolean; default False):
    Whether the input is in an invalid state.

- invalidText (a list of or a singular dash component, string or number; optional):
    Invalid state error message.

- labelText (a list of or a singular dash component, string or number; optional):
    Specify the label text.

- light (boolean; optional):
    Whether the label should be lightweight.

- loading_state (dict; optional):
    Dash loading state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- maxCount (number; optional):
    Maximum count (used with enableCounter).

- persisted_props (list of strings; optional)

- persistence (boolean | string | number; optional):
    Persistence.

- persistence_type (a value equal to: 'local', 'session', 'memory'; optional)

- placeholder (string; optional):
    Placeholder text.

- readOnly (boolean; default False):
    Whether the input is read only.

- renderIcon (a list of or a singular dash component, string or number; optional):
    An icon component to render inside the input.

- size (a value equal to: 'sm', 'md', 'lg'; default 'md'):
    Size of the input.

- type (string; optional):
    What the input type is (e.g. 'text', 'email', 'password').

- value (string | number; optional):
    The value of the input.

- warn (boolean; default False):
    Whether the input is in a warning state.

- warnText (a list of or a singular dash component, string or number; optional):
    Warning state message."""
    _children_props: typing.List[str] = ['labelText', 'helperText', 'invalidText', 'warnText', 'renderIcon']
    _base_nodes = ['labelText', 'helperText', 'invalidText', 'warnText', 'renderIcon', 'children']
    _namespace = 'carbon_dash'
    _type = 'TextInput'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        value: typing.Optional[typing.Union[str, NumberType]] = None,
        labelText: typing.Optional[ComponentType] = None,
        placeholder: typing.Optional[str] = None,
        helperText: typing.Optional[ComponentType] = None,
        disabled: typing.Optional[bool] = None,
        readOnly: typing.Optional[bool] = None,
        invalid: typing.Optional[bool] = None,
        invalidText: typing.Optional[ComponentType] = None,
        warn: typing.Optional[bool] = None,
        warnText: typing.Optional[ComponentType] = None,
        size: typing.Optional[typing.Optional[str]] = None,
        hideLabel: typing.Optional[bool] = None,
        enableCounter: typing.Optional[bool] = None,
        maxCount: typing.Optional[NumberType] = None,
        type: typing.Optional[str] = None,
        defaultValue: typing.Optional[typing.Union[str, NumberType]] = None,
        light: typing.Optional[bool] = None,
        renderIcon: typing.Optional[ComponentType] = None,
        aiLabel: typing.Optional[bool] = None,
        onChange: typing.Optional[typing.Any] = None,
        onBlur: typing.Optional[typing.Any] = None,
        persistence: typing.Optional[typing.Union[bool, str, NumberType]] = None,
        persisted_props: typing.Optional[typing.Sequence[str]] = None,
        persistence_type: typing.Optional[Literal["local", "session", "memory"]] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'aiLabel', 'className', 'defaultValue', 'disabled', 'enableCounter', 'helperText', 'hideLabel', 'invalid', 'invalidText', 'labelText', 'light', 'loading_state', 'maxCount', 'persisted_props', 'persistence', 'persistence_type', 'placeholder', 'readOnly', 'renderIcon', 'size', 'style', 'type', 'value', 'warn', 'warnText']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'aiLabel', 'className', 'defaultValue', 'disabled', 'enableCounter', 'helperText', 'hideLabel', 'invalid', 'invalidText', 'labelText', 'light', 'loading_state', 'maxCount', 'persisted_props', 'persistence', 'persistence_type', 'placeholder', 'readOnly', 'renderIcon', 'size', 'style', 'type', 'value', 'warn', 'warnText']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(TextInput, self).__init__(children=children, **args)

setattr(TextInput, "__init__", _explicitize_args(TextInput.__init__))
