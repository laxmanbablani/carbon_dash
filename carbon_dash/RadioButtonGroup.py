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


class RadioButtonGroup(Component):
    """A RadioButtonGroup component.
RadioButtonGroup is a wrapper for the Carbon RadioButtonGroup component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- className (string; default ''):
    className.

- decorator (boolean | number | string | dict | list; optional):
    decorator.

- defaultSelected (boolean | number | string | dict | list; optional):
    defaultSelected.

- disabled (boolean | number | string | dict | list; optional):
    disabled.

- helperText (boolean | number | string | dict | list; optional):
    helperText.

- invalid (boolean | number | string | dict | list; optional):
    invalid.

- invalidText (boolean | number | string | dict | list; optional):
    invalidText.

- label (string; default 'Radio Button Group'):
    label.

- labelPosition (boolean | number | string | dict | list; optional):
    labelPosition.

- legendText (boolean | number | string | dict | list; optional):
    legendText.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- name (boolean | number | string | dict | list; optional):
    name.

- onChange (boolean | number | string | dict | list; optional):
    onChange.

- orientation (boolean | number | string | dict | list; optional):
    orientation.

- persisted_props (list of strings; optional):
    persisted_props.

- persistence (boolean | string | number; optional):
    persistence.

- persistence_type (a value equal to: 'local', 'session', 'memory'; optional):
    persistence_type.

- readOnly (boolean | number | string | dict | list; optional):
    readOnly.

- required (boolean | number | string | dict | list; optional):
    required.

- slug (boolean | number | string | dict | list; optional):
    slug.

- valueSelected (boolean | number | string | dict | list; optional):
    valueSelected.

- warn (boolean | number | string | dict | list; optional):
    warn.

- warnText (boolean | number | string | dict | list; optional):
    warnText."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'RadioButtonGroup'


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
        defaultSelected: typing.Optional[typing.Any] = None,
        disabled: typing.Optional[typing.Any] = None,
        helperText: typing.Optional[typing.Any] = None,
        invalid: typing.Optional[typing.Any] = None,
        invalidText: typing.Optional[typing.Any] = None,
        labelPosition: typing.Optional[typing.Any] = None,
        legendText: typing.Optional[typing.Any] = None,
        name: typing.Optional[typing.Any] = None,
        onChange: typing.Optional[typing.Any] = None,
        orientation: typing.Optional[typing.Any] = None,
        readOnly: typing.Optional[typing.Any] = None,
        required: typing.Optional[typing.Any] = None,
        slug: typing.Optional[typing.Any] = None,
        valueSelected: typing.Optional[typing.Any] = None,
        warn: typing.Optional[typing.Any] = None,
        warnText: typing.Optional[typing.Any] = None,
        label: typing.Optional[str] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'decorator', 'defaultSelected', 'disabled', 'helperText', 'invalid', 'invalidText', 'label', 'labelPosition', 'legendText', 'loading_state', 'name', 'onChange', 'orientation', 'persisted_props', 'persistence', 'persistence_type', 'readOnly', 'required', 'slug', 'style', 'valueSelected', 'warn', 'warnText']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'decorator', 'defaultSelected', 'disabled', 'helperText', 'invalid', 'invalidText', 'label', 'labelPosition', 'legendText', 'loading_state', 'name', 'onChange', 'orientation', 'persisted_props', 'persistence', 'persistence_type', 'readOnly', 'required', 'slug', 'style', 'valueSelected', 'warn', 'warnText']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(RadioButtonGroup, self).__init__(children=children, **args)

setattr(RadioButtonGroup, "__init__", _explicitize_args(RadioButtonGroup.__init__))
