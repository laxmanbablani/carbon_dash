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


class FluidNumberInput(Component):
    """A FluidNumberInput component.
FluidNumberInput is a wrapper for the Carbon FluidNumberInput component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- allowEmpty (boolean | number | string | dict | list; optional):
    allowEmpty.

- className (string; default ''):
    className.

- debounce (boolean | number; optional):
    debounce.

- defaultValue (boolean | number | string | dict | list; optional):
    defaultValue.

- disableWheel (boolean | number | string | dict | list; optional):
    disableWheel.

- disabled (boolean | number | string | dict | list; optional):
    disabled.

- formatOptions (boolean | number | string | dict | list; optional):
    formatOptions.

- iconDescription (boolean | number | string | dict | list; optional):
    iconDescription.

- inputMode (boolean | number | string | dict | list; optional):
    inputMode.

- invalid (boolean | number | string | dict | list; optional):
    invalid.

- invalidText (boolean | number | string | dict | list; optional):
    invalidText.

- label (boolean | number | string | dict | list; optional):
    label.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- locale (boolean | number | string | dict | list; optional):
    locale.

- max (boolean | number | string | dict | list; optional):
    max.

- min (boolean | number | string | dict | list; optional):
    min.

- n_blur (number; optional):
    n_blur.

- n_submit (number; optional):
    n_submit.

- onChange (boolean | number | string | dict | list; optional):
    onChange.

- onClick (boolean | number | string | dict | list; optional):
    onClick.

- onKeyUp (boolean | number | string | dict | list; optional):
    onKeyUp.

- pattern (boolean | number | string | dict | list; optional):
    pattern.

- persisted_props (list of strings; optional):
    persisted_props.

- persistence (boolean | string | number; optional):
    persistence.

- persistence_type (a value equal to: 'local', 'session', 'memory'; optional):
    persistence_type.

- readOnly (boolean | number | string | dict | list; optional):
    readOnly.

- step (boolean | number | string | dict | list; optional):
    step.

- translateWithId (boolean | number | string | dict | list; optional):
    translateWithId.

- type (boolean | number | string | dict | list; optional):
    type.

- value (boolean | number | string | dict | list; default ''):
    value.

- warn (boolean | number | string | dict | list; optional):
    warn.

- warnText (boolean | number | string | dict | list; optional):
    warnText."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'FluidNumberInput'


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
        allowEmpty: typing.Optional[typing.Any] = None,
        defaultValue: typing.Optional[typing.Any] = None,
        disableWheel: typing.Optional[typing.Any] = None,
        disabled: typing.Optional[typing.Any] = None,
        formatOptions: typing.Optional[typing.Any] = None,
        iconDescription: typing.Optional[typing.Any] = None,
        inputMode: typing.Optional[typing.Any] = None,
        invalid: typing.Optional[typing.Any] = None,
        invalidText: typing.Optional[typing.Any] = None,
        label: typing.Optional[typing.Any] = None,
        locale: typing.Optional[typing.Any] = None,
        max: typing.Optional[typing.Any] = None,
        min: typing.Optional[typing.Any] = None,
        onChange: typing.Optional[typing.Any] = None,
        onClick: typing.Optional[typing.Any] = None,
        onKeyUp: typing.Optional[typing.Any] = None,
        pattern: typing.Optional[typing.Any] = None,
        step: typing.Optional[typing.Any] = None,
        translateWithId: typing.Optional[typing.Any] = None,
        type: typing.Optional[typing.Any] = None,
        value: typing.Optional[typing.Any] = None,
        warn: typing.Optional[typing.Any] = None,
        warnText: typing.Optional[typing.Any] = None,
        readOnly: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'allowEmpty', 'className', 'debounce', 'defaultValue', 'disableWheel', 'disabled', 'formatOptions', 'iconDescription', 'inputMode', 'invalid', 'invalidText', 'label', 'loading_state', 'locale', 'max', 'min', 'n_blur', 'n_submit', 'onChange', 'onClick', 'onKeyUp', 'pattern', 'persisted_props', 'persistence', 'persistence_type', 'readOnly', 'step', 'style', 'translateWithId', 'type', 'value', 'warn', 'warnText']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'allowEmpty', 'className', 'debounce', 'defaultValue', 'disableWheel', 'disabled', 'formatOptions', 'iconDescription', 'inputMode', 'invalid', 'invalidText', 'label', 'loading_state', 'locale', 'max', 'min', 'n_blur', 'n_submit', 'onChange', 'onClick', 'onKeyUp', 'pattern', 'persisted_props', 'persistence', 'persistence_type', 'readOnly', 'step', 'style', 'translateWithId', 'type', 'value', 'warn', 'warnText']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FluidNumberInput, self).__init__(children=children, **args)

setattr(FluidNumberInput, "__init__", _explicitize_args(FluidNumberInput.__init__))
