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


class FluidMultiSelect(Component):
    """A FluidMultiSelect component.
FluidMultiSelect is a full-width MultiSelect component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The content of the multi select.

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- className (string; optional):
    Custom CSS class.

- disabled (boolean; default False):
    Specify whether the control is disabled.

- helperText (a list of or a singular dash component, string or number; optional):
    Provide text that is used alongside the control label.

- invalid (boolean; default False):
    Specify whether the control is in an invalid state.

- invalidText (a list of or a singular dash component, string or number; optional):
    Provide the text that is displayed when the control is in an
    invalid state.

- items (list; optional):
    The items to display in the multi select.

- label (a list of or a singular dash component, string or number; optional):
    Provide text that is used alongside the control label.

- loading_state (dict; optional):
    Dash loading state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- persisted_props (list of strings; optional)

- persistence (boolean | string | number; optional):
    Persistence settings.

- persistence_type (a value equal to: 'local', 'session', 'memory'; optional)

- placeholder (string; optional):
    Provide the placeholder text.

- selectedItems (list; optional):
    The selected items.

- size (a value equal to: 'sm', 'md', 'lg'; default 'md'):
    Specify the size of the multi select.

- titleText (a list of or a singular dash component, string or number; optional):
    Provide the title text for the multi select.

- warn (boolean; default False):
    Specify whether the control is in a warning state.

- warnText (a list of or a singular dash component, string or number; optional):
    Provide the text that is displayed when the control is in a
    warning state."""
    _children_props: typing.List[str] = ['label', 'titleText', 'helperText', 'invalidText', 'warnText']
    _base_nodes = ['label', 'titleText', 'helperText', 'invalidText', 'warnText', 'children']
    _namespace = 'carbon_dash'
    _type = 'FluidMultiSelect'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        items: typing.Optional[typing.Sequence] = None,
        selectedItems: typing.Optional[typing.Sequence] = None,
        label: typing.Optional[ComponentType] = None,
        titleText: typing.Optional[ComponentType] = None,
        helperText: typing.Optional[ComponentType] = None,
        placeholder: typing.Optional[str] = None,
        disabled: typing.Optional[bool] = None,
        invalid: typing.Optional[bool] = None,
        invalidText: typing.Optional[ComponentType] = None,
        warn: typing.Optional[bool] = None,
        warnText: typing.Optional[ComponentType] = None,
        size: typing.Optional[typing.Optional[str]] = None,
        persistence: typing.Optional[typing.Union[bool, str, NumberType]] = None,
        persisted_props: typing.Optional[typing.Sequence[str]] = None,
        persistence_type: typing.Optional[Literal["local", "session", "memory"]] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'disabled', 'helperText', 'invalid', 'invalidText', 'items', 'label', 'loading_state', 'persisted_props', 'persistence', 'persistence_type', 'placeholder', 'selectedItems', 'size', 'style', 'titleText', 'warn', 'warnText']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'disabled', 'helperText', 'invalid', 'invalidText', 'items', 'label', 'loading_state', 'persisted_props', 'persistence', 'persistence_type', 'placeholder', 'selectedItems', 'size', 'style', 'titleText', 'warn', 'warnText']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FluidMultiSelect, self).__init__(children=children, **args)

setattr(FluidMultiSelect, "__init__", _explicitize_args(FluidMultiSelect.__init__))
