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


class NumberInput(Component):
    """A NumberInput component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional)

- allowEmpty (boolean; default False):
    Allow empty value.

- className (string; optional)

- disabled (boolean; default False):
    Whether disabled.

- helperText (a list of or a singular dash component, string or number; optional):
    Helper text.

- hideLabel (boolean; default False):
    Whether to hide label.

- hideSteppers (boolean; default False):
    Whether to hide steppers with mouse event.

- invalid (boolean; default False):
    Whether invalid.

- invalidText (a list of or a singular dash component, string or number; optional):
    Invalid text.

- label (a list of or a singular dash component, string or number; optional):
    Label text.

- light (boolean; optional):
    Whether lightweight.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- max (number; default 100):
    Maximum value.

- min (number; default 0):
    Minimum value.

- persisted_props (list of strings; optional)

- persistence (boolean | string | number; optional)

- persistence_type (a value equal to: 'local', 'session', 'memory'; optional)

- readOnly (boolean; optional):
    Whether readonly.

- size (a value equal to: 'sm', 'md', 'lg'; default 'md'):
    Size.

- step (number; default 1):
    Step value.

- value (number | string; optional):
    The value.

- warn (boolean; default False):
    Whether warn.

- warnText (a list of or a singular dash component, string or number; optional):
    Warn text."""
    _children_props: typing.List[str] = ['label', 'helperText', 'invalidText', 'warnText']
    _base_nodes = ['label', 'helperText', 'invalidText', 'warnText', 'children']
    _namespace = 'carbon_dash'
    _type = 'NumberInput'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        value: typing.Optional[typing.Union[NumberType, str]] = None,
        label: typing.Optional[ComponentType] = None,
        helperText: typing.Optional[ComponentType] = None,
        min: typing.Optional[NumberType] = None,
        max: typing.Optional[NumberType] = None,
        step: typing.Optional[NumberType] = None,
        disabled: typing.Optional[bool] = None,
        readOnly: typing.Optional[bool] = None,
        invalid: typing.Optional[bool] = None,
        invalidText: typing.Optional[ComponentType] = None,
        warn: typing.Optional[bool] = None,
        warnText: typing.Optional[ComponentType] = None,
        size: typing.Optional[typing.Optional[str]] = None,
        hideSteppers: typing.Optional[bool] = None,
        hideLabel: typing.Optional[bool] = None,
        light: typing.Optional[bool] = None,
        allowEmpty: typing.Optional[bool] = None,
        persistence: typing.Optional[typing.Union[bool, str, NumberType]] = None,
        persisted_props: typing.Optional[typing.Sequence[str]] = None,
        persistence_type: typing.Optional[Literal["local", "session", "memory"]] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'allowEmpty', 'className', 'disabled', 'helperText', 'hideLabel', 'hideSteppers', 'invalid', 'invalidText', 'label', 'light', 'loading_state', 'max', 'min', 'persisted_props', 'persistence', 'persistence_type', 'readOnly', 'size', 'step', 'style', 'value', 'warn', 'warnText']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'allowEmpty', 'className', 'disabled', 'helperText', 'hideLabel', 'hideSteppers', 'invalid', 'invalidText', 'label', 'light', 'loading_state', 'max', 'min', 'persisted_props', 'persistence', 'persistence_type', 'readOnly', 'size', 'step', 'style', 'value', 'warn', 'warnText']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(NumberInput, self).__init__(children=children, **args)

setattr(NumberInput, "__init__", _explicitize_args(NumberInput.__init__))
