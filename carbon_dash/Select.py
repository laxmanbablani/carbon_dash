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


class Select(Component):
    """A Select component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional)

- className (string; optional)

- defaultValue (boolean | number | string | dict | list; optional):
    Default value (uncontrolled).

- disabled (boolean; default False):
    Whether the select is disabled.

- helperText (a list of or a singular dash component, string or number; optional):
    Helper text.

- hideLabel (boolean; default False):
    Whether the label should be visually hidden.

- inline (boolean; default False):
    Inline variant.

- invalid (boolean; default False):
    Whether the select is in invalid state.

- invalidText (a list of or a singular dash component, string or number; optional):
    Invalid state text.

- labelText (a list of or a singular dash component, string or number; optional):
    Label text.

- light (boolean; optional):
    Whether the label should be lightweight.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- persisted_props (list of strings; optional)

- persistence (boolean | string | number; optional)

- persistence_type (a value equal to: 'local', 'session', 'memory'; optional)

- size (a value equal to: 'sm', 'md', 'lg'; default 'md'):
    Size.

- value (boolean | number | string | dict | list; optional):
    Current value of the select.

- warn (boolean; default False):
    Whether the select is in warning state.

- warnText (a list of or a singular dash component, string or number; optional):
    Warning state text."""
    _children_props: typing.List[str] = ['labelText', 'invalidText', 'warnText', 'helperText']
    _base_nodes = ['labelText', 'invalidText', 'warnText', 'helperText', 'children']
    _namespace = 'carbon_dash'
    _type = 'Select'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        value: typing.Optional[typing.Any] = None,
        defaultValue: typing.Optional[typing.Any] = None,
        labelText: typing.Optional[ComponentType] = None,
        disabled: typing.Optional[bool] = None,
        invalid: typing.Optional[bool] = None,
        invalidText: typing.Optional[ComponentType] = None,
        warn: typing.Optional[bool] = None,
        warnText: typing.Optional[ComponentType] = None,
        helperText: typing.Optional[ComponentType] = None,
        hideLabel: typing.Optional[bool] = None,
        light: typing.Optional[bool] = None,
        size: typing.Optional[typing.Optional[str]] = None,
        inline: typing.Optional[bool] = None,
        persistence: typing.Optional[typing.Union[bool, str, NumberType]] = None,
        persisted_props: typing.Optional[typing.Sequence[str]] = None,
        persistence_type: typing.Optional[Literal["local", "session", "memory"]] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'defaultValue', 'disabled', 'helperText', 'hideLabel', 'inline', 'invalid', 'invalidText', 'labelText', 'light', 'loading_state', 'persisted_props', 'persistence', 'persistence_type', 'size', 'style', 'value', 'warn', 'warnText']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'defaultValue', 'disabled', 'helperText', 'hideLabel', 'inline', 'invalid', 'invalidText', 'labelText', 'light', 'loading_state', 'persisted_props', 'persistence', 'persistence_type', 'size', 'style', 'value', 'warn', 'warnText']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Select, self).__init__(children=children, **args)

setattr(Select, "__init__", _explicitize_args(Select.__init__))
