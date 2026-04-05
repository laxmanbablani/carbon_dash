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
ProgressBar is a wrapper for the Carbon ProgressBar component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- className (string; default ''):
    className.

- debounce (boolean | number; optional):
    debounce.

- helperText (boolean | number | string | dict | list; optional):
    helperText.

- hideLabel (boolean | number | string | dict | list; optional):
    hideLabel.

- label (boolean | number | string | dict | list; optional):
    label.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- max (boolean | number | string | dict | list; optional):
    max.

- n_blur (number; optional):
    n_blur.

- n_submit (number; optional):
    n_submit.

- persisted_props (list of strings; optional):
    persisted_props.

- persistence (boolean | string | number; optional):
    persistence.

- persistence_type (a value equal to: 'local', 'session', 'memory'; optional):
    persistence_type.

- size (boolean | number | string | dict | list; optional):
    size.

- status (boolean | number | string | dict | list; optional):
    status.

- type (boolean | number | string | dict | list; optional):
    type.

- value (boolean | number | string | dict | list; optional):
    value."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'ProgressBar'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        persistence: typing.Optional[typing.Union[bool, str, NumberType]] = None,
        persisted_props: typing.Optional[typing.Sequence[str]] = None,
        persistence_type: typing.Optional[Literal["local", "session", "memory"]] = None,
        n_blur: typing.Optional[NumberType] = None,
        n_submit: typing.Optional[NumberType] = None,
        debounce: typing.Optional[typing.Union[bool, NumberType]] = None,
        helperText: typing.Optional[typing.Any] = None,
        hideLabel: typing.Optional[typing.Any] = None,
        label: typing.Optional[typing.Any] = None,
        max: typing.Optional[typing.Any] = None,
        size: typing.Optional[typing.Optional[str]] = None,
        status: typing.Optional[typing.Any] = None,
        type: typing.Optional[typing.Any] = None,
        value: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'debounce', 'helperText', 'hideLabel', 'label', 'loading_state', 'max', 'n_blur', 'n_submit', 'persisted_props', 'persistence', 'persistence_type', 'size', 'status', 'style', 'type', 'value']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'debounce', 'helperText', 'hideLabel', 'label', 'loading_state', 'max', 'n_blur', 'n_submit', 'persisted_props', 'persistence', 'persistence_type', 'size', 'status', 'style', 'type', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(ProgressBar, self).__init__(children=children, **args)

setattr(ProgressBar, "__init__", _explicitize_args(ProgressBar.__init__))
