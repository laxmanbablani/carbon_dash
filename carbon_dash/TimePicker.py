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


class TimePicker(Component):
    """A TimePicker component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional)

- className (string; optional)

- disabled (boolean; default False):
    Whether disabled.

- hideLabel (boolean; optional):
    Hide label.

- invalid (boolean; optional):
    Whether invalid.

- invalidText (a list of or a singular dash component, string or number; optional):
    Invalid text.

- labelText (a list of or a singular dash component, string or number; optional):
    Label text.

- light (boolean; optional):
    Light variant.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- pattern (string; optional):
    Format pattern.

- persisted_props (list of strings; optional)

- persistence (boolean | string | number; optional)

- persistence_type (a value equal to: 'local', 'session', 'memory'; optional)

- placeholder (string; optional):
    Placeholder.

- readOnly (boolean; optional):
    Whether readonly.

- size (a value equal to: 'sm', 'md', 'lg'; default 'md'):
    Size.

- timeFormat (a value equal to: '12', '24'; default '12'):
    Time format: '12' or '24'.

- type (string; optional):
    Type.

- value (string; optional):
    Current time value."""
    _children_props: typing.List[str] = ['labelText', 'invalidText']
    _base_nodes = ['labelText', 'invalidText', 'children']
    _namespace = 'carbon_dash'
    _type = 'TimePicker'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        value: typing.Optional[str] = None,
        labelText: typing.Optional[ComponentType] = None,
        placeholder: typing.Optional[str] = None,
        disabled: typing.Optional[bool] = None,
        invalid: typing.Optional[bool] = None,
        invalidText: typing.Optional[ComponentType] = None,
        size: typing.Optional[typing.Optional[str]] = None,
        light: typing.Optional[bool] = None,
        hideLabel: typing.Optional[bool] = None,
        readOnly: typing.Optional[bool] = None,
        pattern: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        timeFormat: typing.Optional[Literal["12", "24"]] = None,
        persistence: typing.Optional[typing.Union[bool, str, NumberType]] = None,
        persisted_props: typing.Optional[typing.Sequence[str]] = None,
        persistence_type: typing.Optional[Literal["local", "session", "memory"]] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'disabled', 'hideLabel', 'invalid', 'invalidText', 'labelText', 'light', 'loading_state', 'pattern', 'persisted_props', 'persistence', 'persistence_type', 'placeholder', 'readOnly', 'size', 'style', 'timeFormat', 'type', 'value']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'disabled', 'hideLabel', 'invalid', 'invalidText', 'labelText', 'light', 'loading_state', 'pattern', 'persisted_props', 'persistence', 'persistence_type', 'placeholder', 'readOnly', 'size', 'style', 'timeFormat', 'type', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(TimePicker, self).__init__(children=children, **args)

setattr(TimePicker, "__init__", _explicitize_args(TimePicker.__init__))
