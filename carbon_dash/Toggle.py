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


class Toggle(Component):
    """A Toggle component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional)

- className (string; optional)

- disabled (boolean; default False):
    Whether the toggle is disabled.

- hideLabel (boolean; optional):
    Whether to hide the label.

- labelA (a list of or a singular dash component, string or number; optional):
    Label for A (off) position.

- labelB (a list of or a singular dash component, string or number; optional):
    Label for B (on) position.

- labelText (a list of or a singular dash component, string or number; optional):
    Toggle label text.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- persisted_props (list of strings; optional)

- persistence (boolean | string | number; optional)

- persistence_type (a value equal to: 'local', 'session', 'memory'; optional)

- size (a value equal to: 'sm', 'md'; default 'md'):
    Size of the toggle.

- toggled (boolean; default False):
    Whether the toggle is on."""
    _children_props: typing.List[str] = ['labelText', 'labelA', 'labelB']
    _base_nodes = ['labelText', 'labelA', 'labelB', 'children']
    _namespace = 'carbon_dash'
    _type = 'Toggle'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        labelText: typing.Optional[ComponentType] = None,
        labelA: typing.Optional[ComponentType] = None,
        labelB: typing.Optional[ComponentType] = None,
        toggled: typing.Optional[bool] = None,
        disabled: typing.Optional[bool] = None,
        size: typing.Optional[typing.Optional[str]] = None,
        hideLabel: typing.Optional[bool] = None,
        persistence: typing.Optional[typing.Union[bool, str, NumberType]] = None,
        persisted_props: typing.Optional[typing.Sequence[str]] = None,
        persistence_type: typing.Optional[Literal["local", "session", "memory"]] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'disabled', 'hideLabel', 'labelA', 'labelB', 'labelText', 'loading_state', 'persisted_props', 'persistence', 'persistence_type', 'size', 'style', 'toggled']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'disabled', 'hideLabel', 'labelA', 'labelB', 'labelText', 'loading_state', 'persisted_props', 'persistence', 'persistence_type', 'size', 'style', 'toggled']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Toggle, self).__init__(children=children, **args)

setattr(Toggle, "__init__", _explicitize_args(Toggle.__init__))
