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


class Slider(Component):
    """A Slider component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional)

- className (string; optional)

- disabled (boolean; default False):
    Whether disabled.

- hideTextInput (boolean; default False):
    Whether to hide text inputs.

- labelText (a list of or a singular dash component, string or number; optional):
    Label text.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- max (number; default 100):
    Maximum value.

- maxLabel (string; optional):
    Maximum label.

- min (number; default 0):
    Minimum value.

- minLabel (string; optional):
    Minimum label.

- persisted_props (list of strings; optional)

- persistence (boolean | string | number; optional)

- persistence_type (a value equal to: 'local', 'session', 'memory'; optional)

- step (number; default 1):
    Step interval.

- stepMultiplier (number; optional):
    Step multipliers array.

- value (number; optional):
    Current value.

- valueLabel (string; optional):
    Label for current value."""
    _children_props: typing.List[str] = ['labelText']
    _base_nodes = ['labelText', 'children']
    _namespace = 'carbon_dash'
    _type = 'Slider'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        value: typing.Optional[NumberType] = None,
        labelText: typing.Optional[ComponentType] = None,
        min: typing.Optional[NumberType] = None,
        max: typing.Optional[NumberType] = None,
        step: typing.Optional[NumberType] = None,
        stepMultiplier: typing.Optional[NumberType] = None,
        disabled: typing.Optional[bool] = None,
        hideTextInput: typing.Optional[bool] = None,
        minLabel: typing.Optional[str] = None,
        maxLabel: typing.Optional[str] = None,
        valueLabel: typing.Optional[str] = None,
        formatLabel: typing.Optional[typing.Any] = None,
        persistence: typing.Optional[typing.Union[bool, str, NumberType]] = None,
        persisted_props: typing.Optional[typing.Sequence[str]] = None,
        persistence_type: typing.Optional[Literal["local", "session", "memory"]] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'disabled', 'hideTextInput', 'labelText', 'loading_state', 'max', 'maxLabel', 'min', 'minLabel', 'persisted_props', 'persistence', 'persistence_type', 'step', 'stepMultiplier', 'style', 'value', 'valueLabel']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'disabled', 'hideTextInput', 'labelText', 'loading_state', 'max', 'maxLabel', 'min', 'minLabel', 'persisted_props', 'persistence', 'persistence_type', 'step', 'stepMultiplier', 'style', 'value', 'valueLabel']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Slider, self).__init__(children=children, **args)

setattr(Slider, "__init__", _explicitize_args(Slider.__init__))
