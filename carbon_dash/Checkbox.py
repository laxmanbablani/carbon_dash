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


class Checkbox(Component):
    """A Checkbox component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional)

- checked (boolean; default False):
    Whether the checkbox is checked.

- className (string; optional)

- disabled (boolean; default False):
    Whether the checkbox is disabled.

- hideLabel (boolean; default False):
    Whether to hide the label.

- indeterminate (boolean; default False):
    Whether the checkbox is in an indeterminate state.

- labelText (a list of or a singular dash component, string or number; optional):
    Checkbox label text.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- persisted_props (list of strings; optional)

- persistence (boolean | string | number; optional)

- persistence_type (a value equal to: 'local', 'session', 'memory'; optional)

- title (string; optional):
    Title attribute.

- value (string; optional):
    The value submitted with the form."""
    _children_props: typing.List[str] = ['labelText']
    _base_nodes = ['labelText', 'children']
    _namespace = 'carbon_dash'
    _type = 'Checkbox'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        labelText: typing.Optional[ComponentType] = None,
        checked: typing.Optional[bool] = None,
        disabled: typing.Optional[bool] = None,
        indeterminate: typing.Optional[bool] = None,
        hideLabel: typing.Optional[bool] = None,
        value: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        persistence: typing.Optional[typing.Union[bool, str, NumberType]] = None,
        persisted_props: typing.Optional[typing.Sequence[str]] = None,
        persistence_type: typing.Optional[Literal["local", "session", "memory"]] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'checked', 'className', 'disabled', 'hideLabel', 'indeterminate', 'labelText', 'loading_state', 'persisted_props', 'persistence', 'persistence_type', 'style', 'title', 'value']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'checked', 'className', 'disabled', 'hideLabel', 'indeterminate', 'labelText', 'loading_state', 'persisted_props', 'persistence', 'persistence_type', 'style', 'title', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Checkbox, self).__init__(children=children, **args)

setattr(Checkbox, "__init__", _explicitize_args(Checkbox.__init__))
