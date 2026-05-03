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


class ProgressBar(Component):
    """A ProgressBar component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional)

- className (string; optional)

- helperText (a list of or a singular dash component, string or number; optional)

- hideLabel (boolean; optional)

- label (a list of or a singular dash component, string or number; optional)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- max (number; default 100)

- persisted_props (list of strings; optional)

- persistence (boolean | string | number; optional)

- persistence_type (a value equal to: 'local', 'session', 'memory'; optional)

- size (a value equal to: 'big', 'small'; default 'big')

- value (number; default 0)"""
    _children_props: typing.List[str] = ['label', 'helperText']
    _base_nodes = ['label', 'helperText', 'children']
    _namespace = 'carbon_dash'
    _type = 'ProgressBar'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        value: typing.Optional[NumberType] = None,
        max: typing.Optional[NumberType] = None,
        label: typing.Optional[ComponentType] = None,
        helperText: typing.Optional[ComponentType] = None,
        hideLabel: typing.Optional[bool] = None,
        size: typing.Optional[typing.Optional[str]] = None,
        persistence: typing.Optional[typing.Union[bool, str, NumberType]] = None,
        persisted_props: typing.Optional[typing.Sequence[str]] = None,
        persistence_type: typing.Optional[Literal["local", "session", "memory"]] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'helperText', 'hideLabel', 'label', 'loading_state', 'max', 'persisted_props', 'persistence', 'persistence_type', 'size', 'style', 'value']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'helperText', 'hideLabel', 'label', 'loading_state', 'max', 'persisted_props', 'persistence', 'persistence_type', 'size', 'style', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(ProgressBar, self).__init__(children=children, **args)

setattr(ProgressBar, "__init__", _explicitize_args(ProgressBar.__init__))
