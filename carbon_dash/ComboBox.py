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


class ComboBox(Component):
    """A ComboBox component.
ComboBox is a dropdown with autocomplete functionality.
Wraps the Carbon ComboBox component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Children elements (typically Text components for options, or
    custom renderers).

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- allowCustomValue (boolean; default False):
    Whether to allow custom values not in the items list.

- className (string; optional):
    Specify a custom className to be applied to the component.

- direction (a value equal to: 'top', 'bottom'; default 'bottom'):
    Direction of the dropdown menu.

- disabled (boolean; default False):
    Whether the combobox is disabled.

- helperText (a list of or a singular dash component, string or number; optional):
    Helper text displayed below the combobox.

- invalid (boolean; default False):
    Whether the combobox is in an invalid state.

- invalidText (a list of or a singular dash component, string or number; optional):
    Error message to display when invalid.

- items (list; optional):
    Array of items to display in the combobox. Each item should have
    an id, text, and optionally disabled/icon properties.

- labelText (a list of or a singular dash component, string or number; optional):
    Label text displayed above the combobox.

- light (boolean; default False):
    Light variant.

- loading_state (dict; optional):
    Dash loading state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- persisted_props (list of strings; optional):
    Properties whose user interactions will persist.

- persistence (boolean | string | number; optional):
    Used to allow user interactions in this component to be persisted.

- persistence_type (a value equal to: 'local', 'session', 'memory'; optional):
    Where persisted user changes will be stored.

- placeholder (string; optional):
    Placeholder text when no value is selected.

- selectedItem (boolean | number | string | dict | list; optional):
    The currently selected item.

- size (a value equal to: 'sm', 'md', 'lg'; default 'md'):
    Size of the combobox.

- titleText (a list of or a singular dash component, string or number; optional):
    Title text for the combobox (shown as help text/tooltip).

- warn (boolean; default False):
    Whether the combobox is in a warning state.

- warnText (a list of or a singular dash component, string or number; optional):
    Warning message to display."""
    _children_props: typing.List[str] = ['labelText', 'titleText', 'helperText', 'invalidText', 'warnText']
    _base_nodes = ['labelText', 'titleText', 'helperText', 'invalidText', 'warnText', 'children']
    _namespace = 'carbon_dash'
    _type = 'ComboBox'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        items: typing.Optional[typing.Sequence] = None,
        selectedItem: typing.Optional[typing.Any] = None,
        labelText: typing.Optional[ComponentType] = None,
        titleText: typing.Optional[ComponentType] = None,
        helperText: typing.Optional[ComponentType] = None,
        placeholder: typing.Optional[str] = None,
        disabled: typing.Optional[bool] = None,
        invalid: typing.Optional[bool] = None,
        invalidText: typing.Optional[ComponentType] = None,
        warn: typing.Optional[bool] = None,
        warnText: typing.Optional[ComponentType] = None,
        allowCustomValue: typing.Optional[bool] = None,
        size: typing.Optional[typing.Optional[str]] = None,
        light: typing.Optional[bool] = None,
        direction: typing.Optional[Literal["top", "bottom"]] = None,
        persistence: typing.Optional[typing.Union[bool, str, NumberType]] = None,
        persisted_props: typing.Optional[typing.Sequence[str]] = None,
        persistence_type: typing.Optional[Literal["local", "session", "memory"]] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'allowCustomValue', 'className', 'direction', 'disabled', 'helperText', 'invalid', 'invalidText', 'items', 'labelText', 'light', 'loading_state', 'persisted_props', 'persistence', 'persistence_type', 'placeholder', 'selectedItem', 'size', 'style', 'titleText', 'warn', 'warnText']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'allowCustomValue', 'className', 'direction', 'disabled', 'helperText', 'invalid', 'invalidText', 'items', 'labelText', 'light', 'loading_state', 'persisted_props', 'persistence', 'persistence_type', 'placeholder', 'selectedItem', 'size', 'style', 'titleText', 'warn', 'warnText']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(ComboBox, self).__init__(children=children, **args)

setattr(ComboBox, "__init__", _explicitize_args(ComboBox.__init__))
