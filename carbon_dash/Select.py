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
Select is a wrapper for the Carbon Select component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- className (string; default ''):
    className.

- decorator (boolean | number | string | dict | list; optional):
    decorator.

- defaultValue (boolean | number | string | dict | list; optional):
    defaultValue.

- disabled (boolean | number | string | dict | list; optional):
    disabled.

- helperText (boolean | number | string | dict | list; optional):
    helperText.

- hideLabel (boolean | number | string | dict | list; optional):
    hideLabel.

- inline (boolean | number | string | dict | list; optional):
    inline.

- invalid (boolean | number | string | dict | list; optional):
    invalid.

- invalidText (boolean | number | string | dict | list; optional):
    invalidText.

- label (string; default 'Select'):
    label.

- labelText (boolean | number | string | dict | list; optional):
    labelText.

- light (boolean | number | string | dict | list; optional):
    light.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- noLabel (boolean | number | string | dict | list; optional):
    noLabel.

- onChange (boolean | number | string | dict | list; optional):
    onChange.

- persisted_props (list of strings; optional):
    persisted_props.

- persistence (boolean | string | number; optional):
    persistence.

- persistence_type (a value equal to: 'local', 'session', 'memory'; optional):
    persistence_type.

- readOnly (boolean | number | string | dict | list; optional):
    readOnly.

- size (boolean | number | string | dict | list; optional):
    size.

- slug (boolean | number | string | dict | list; optional):
    slug.

- value (boolean | number | string | dict | list; default ''):
    value.

- warn (boolean | number | string | dict | list; optional):
    warn.

- warnText (boolean | number | string | dict | list; optional):
    warnText."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'Select'


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
        decorator: typing.Optional[typing.Any] = None,
        defaultValue: typing.Optional[typing.Any] = None,
        disabled: typing.Optional[typing.Any] = None,
        helperText: typing.Optional[typing.Any] = None,
        hideLabel: typing.Optional[typing.Any] = None,
        inline: typing.Optional[typing.Any] = None,
        invalid: typing.Optional[typing.Any] = None,
        invalidText: typing.Optional[typing.Any] = None,
        labelText: typing.Optional[typing.Any] = None,
        light: typing.Optional[typing.Any] = None,
        noLabel: typing.Optional[typing.Any] = None,
        onChange: typing.Optional[typing.Any] = None,
        readOnly: typing.Optional[typing.Any] = None,
        size: typing.Optional[typing.Optional[str]] = None,
        slug: typing.Optional[typing.Any] = None,
        warn: typing.Optional[typing.Any] = None,
        warnText: typing.Optional[typing.Any] = None,
        value: typing.Optional[typing.Any] = None,
        label: typing.Optional[str] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'decorator', 'defaultValue', 'disabled', 'helperText', 'hideLabel', 'inline', 'invalid', 'invalidText', 'label', 'labelText', 'light', 'loading_state', 'noLabel', 'onChange', 'persisted_props', 'persistence', 'persistence_type', 'readOnly', 'size', 'slug', 'style', 'value', 'warn', 'warnText']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'decorator', 'defaultValue', 'disabled', 'helperText', 'hideLabel', 'inline', 'invalid', 'invalidText', 'label', 'labelText', 'light', 'loading_state', 'noLabel', 'onChange', 'persisted_props', 'persistence', 'persistence_type', 'readOnly', 'size', 'slug', 'style', 'value', 'warn', 'warnText']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Select, self).__init__(children=children, **args)

setattr(Select, "__init__", _explicitize_args(Select.__init__))
