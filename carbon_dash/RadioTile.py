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


class RadioTile(Component):
    """A RadioTile component.
RadioTile is a wrapper for the Carbon RadioTile component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- checked (boolean; default False):
    checked.

- className (string; default ''):
    className.

- debounce (boolean | number; optional):
    debounce.

- decorator (boolean | number | string | dict | list; optional):
    decorator.

- disabled (boolean | number | string | dict | list; optional):
    disabled.

- hasRoundedCorners (boolean | number | string | dict | list; optional):
    hasRoundedCorners.

- light (boolean | number | string | dict | list; optional):
    light.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- n_blur (number; optional):
    n_blur.

- n_submit (number; optional):
    n_submit.

- name (boolean | number | string | dict | list; optional):
    name.

- onChange (boolean | number | string | dict | list; optional):
    onChange.

- persisted_props (list of strings; optional):
    persisted_props.

- persistence (boolean | string | number; optional):
    persistence.

- persistence_type (a value equal to: 'local', 'session', 'memory'; optional):
    persistence_type.

- required (boolean | number | string | dict | list; optional):
    required.

- slug (boolean | number | string | dict | list; optional):
    slug.

- tabIndex (boolean | number | string | dict | list; optional):
    tabIndex.

- value (boolean | number | string | dict | list; default ''):
    value."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'RadioTile'


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
        checked: typing.Optional[bool] = None,
        decorator: typing.Optional[typing.Any] = None,
        disabled: typing.Optional[typing.Any] = None,
        hasRoundedCorners: typing.Optional[typing.Any] = None,
        light: typing.Optional[typing.Any] = None,
        name: typing.Optional[typing.Any] = None,
        onChange: typing.Optional[typing.Any] = None,
        value: typing.Optional[typing.Any] = None,
        slug: typing.Optional[typing.Any] = None,
        tabIndex: typing.Optional[typing.Any] = None,
        required: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'checked', 'className', 'debounce', 'decorator', 'disabled', 'hasRoundedCorners', 'light', 'loading_state', 'n_blur', 'n_submit', 'name', 'onChange', 'persisted_props', 'persistence', 'persistence_type', 'required', 'slug', 'style', 'tabIndex', 'value']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'checked', 'className', 'debounce', 'decorator', 'disabled', 'hasRoundedCorners', 'light', 'loading_state', 'n_blur', 'n_submit', 'name', 'onChange', 'persisted_props', 'persistence', 'persistence_type', 'required', 'slug', 'style', 'tabIndex', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(RadioTile, self).__init__(children=children, **args)

setattr(RadioTile, "__init__", _explicitize_args(RadioTile.__init__))
