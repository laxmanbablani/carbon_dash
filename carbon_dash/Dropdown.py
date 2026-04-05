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


class Dropdown(Component):
    """A Dropdown component.
Dropdown is a wrapper for the Carbon Dropdown component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- ariaLabel (boolean | number | string | dict | list; optional):
    ariaLabel.

- autoAlign (boolean | number | string | dict | list; optional):
    autoAlign.

- className (string; default ''):
    className.

- decorator (boolean | number | string | dict | list; optional):
    decorator.

- direction (boolean | number | string | dict | list; optional):
    direction.

- disabled (boolean | number | string | dict | list; optional):
    disabled.

- downshiftProps (boolean | number | string | dict | list; optional):
    downshiftProps.

- helperText (boolean | number | string | dict | list; optional):
    helperText.

- hideLabel (boolean | number | string | dict | list; optional):
    hideLabel.

- initialSelectedItem (boolean | number | string | dict | list; optional):
    initialSelectedItem.

- invalid (boolean | number | string | dict | list; optional):
    invalid.

- invalidText (boolean | number | string | dict | list; optional):
    invalidText.

- itemToElement (boolean | number | string | dict | list; optional):
    itemToElement.

- itemToString (boolean | number | string | dict | list; optional):
    itemToString.

- items (list; optional):
    items.

- label (string; default 'Dropdown'):
    label.

- light (boolean | number | string | dict | list; optional):
    light.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

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

- renderSelectedItem (boolean | number | string | dict | list; optional):
    renderSelectedItem.

- selectedItem (boolean | number | string | dict | list; optional):
    selectedItem.

- size (boolean | number | string | dict | list; optional):
    size.

- slug (boolean | number | string | dict | list; optional):
    slug.

- title (string; default 'Dropdown Title'):
    title.

- titleText (boolean | number | string | dict | list; optional):
    titleText.

- translateWithId (boolean | number | string | dict | list; optional):
    translateWithId.

- type (boolean | number | string | dict | list; optional):
    type.

- warn (boolean | number | string | dict | list; optional):
    warn.

- warnText (boolean | number | string | dict | list; optional):
    warnText."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'Dropdown'


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
        ariaLabel: typing.Optional[typing.Any] = None,
        autoAlign: typing.Optional[typing.Any] = None,
        decorator: typing.Optional[typing.Any] = None,
        direction: typing.Optional[typing.Any] = None,
        disabled: typing.Optional[typing.Any] = None,
        downshiftProps: typing.Optional[typing.Any] = None,
        helperText: typing.Optional[typing.Any] = None,
        hideLabel: typing.Optional[typing.Any] = None,
        initialSelectedItem: typing.Optional[typing.Any] = None,
        invalid: typing.Optional[typing.Any] = None,
        invalidText: typing.Optional[typing.Any] = None,
        itemToElement: typing.Optional[typing.Any] = None,
        itemToString: typing.Optional[typing.Any] = None,
        items: typing.Optional[typing.Sequence] = None,
        label: typing.Optional[str] = None,
        light: typing.Optional[typing.Any] = None,
        onChange: typing.Optional[typing.Any] = None,
        readOnly: typing.Optional[typing.Any] = None,
        renderSelectedItem: typing.Optional[typing.Any] = None,
        selectedItem: typing.Optional[typing.Any] = None,
        size: typing.Optional[typing.Optional[str]] = None,
        slug: typing.Optional[typing.Any] = None,
        titleText: typing.Optional[typing.Any] = None,
        translateWithId: typing.Optional[typing.Any] = None,
        type: typing.Optional[typing.Any] = None,
        warn: typing.Optional[typing.Any] = None,
        warnText: typing.Optional[typing.Any] = None,
        title: typing.Optional[str] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'ariaLabel', 'autoAlign', 'className', 'decorator', 'direction', 'disabled', 'downshiftProps', 'helperText', 'hideLabel', 'initialSelectedItem', 'invalid', 'invalidText', 'itemToElement', 'itemToString', 'items', 'label', 'light', 'loading_state', 'onChange', 'persisted_props', 'persistence', 'persistence_type', 'readOnly', 'renderSelectedItem', 'selectedItem', 'size', 'slug', 'style', 'title', 'titleText', 'translateWithId', 'type', 'warn', 'warnText']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'ariaLabel', 'autoAlign', 'className', 'decorator', 'direction', 'disabled', 'downshiftProps', 'helperText', 'hideLabel', 'initialSelectedItem', 'invalid', 'invalidText', 'itemToElement', 'itemToString', 'items', 'label', 'light', 'loading_state', 'onChange', 'persisted_props', 'persistence', 'persistence_type', 'readOnly', 'renderSelectedItem', 'selectedItem', 'size', 'slug', 'style', 'title', 'titleText', 'translateWithId', 'type', 'warn', 'warnText']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Dropdown, self).__init__(children=children, **args)

setattr(Dropdown, "__init__", _explicitize_args(Dropdown.__init__))
