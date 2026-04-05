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


class FluidDropdown(Component):
    """A FluidDropdown component.
FluidDropdown is a wrapper for the Carbon FluidDropdown component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- className (string; default ''):
    className.

- direction (boolean | number | string | dict | list; optional):
    direction.

- disabled (boolean | number | string | dict | list; optional):
    disabled.

- initialSelectedItem (boolean | number | string | dict | list; optional):
    initialSelectedItem.

- invalid (boolean | number | string | dict | list; optional):
    invalid.

- invalidText (boolean | number | string | dict | list; optional):
    invalidText.

- isCondensed (boolean | number | string | dict | list; optional):
    isCondensed.

- itemToElement (boolean | number | string | dict | list; optional):
    itemToElement.

- itemToString (boolean | number | string | dict | list; optional):
    itemToString.

- items (boolean | number | string | dict | list; optional):
    items.

- label (boolean | number | string | dict | list; optional):
    label.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- onChange (boolean | number | string | dict | list; optional):
    onChange.

- renderSelectedItem (boolean | number | string | dict | list; optional):
    renderSelectedItem.

- selectedItem (boolean | number | string | dict | list; optional):
    selectedItem.

- titleText (boolean | number | string | dict | list; optional):
    titleText.

- translateWithId (boolean | number | string | dict | list; optional):
    translateWithId.

- warn (boolean | number | string | dict | list; optional):
    warn.

- warnText (boolean | number | string | dict | list; optional):
    warnText."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'FluidDropdown'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        direction: typing.Optional[typing.Any] = None,
        disabled: typing.Optional[typing.Any] = None,
        initialSelectedItem: typing.Optional[typing.Any] = None,
        invalid: typing.Optional[typing.Any] = None,
        invalidText: typing.Optional[typing.Any] = None,
        isCondensed: typing.Optional[typing.Any] = None,
        itemToElement: typing.Optional[typing.Any] = None,
        itemToString: typing.Optional[typing.Any] = None,
        items: typing.Optional[typing.Any] = None,
        label: typing.Optional[typing.Any] = None,
        onChange: typing.Optional[typing.Any] = None,
        renderSelectedItem: typing.Optional[typing.Any] = None,
        selectedItem: typing.Optional[typing.Any] = None,
        titleText: typing.Optional[typing.Any] = None,
        translateWithId: typing.Optional[typing.Any] = None,
        warn: typing.Optional[typing.Any] = None,
        warnText: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'direction', 'disabled', 'initialSelectedItem', 'invalid', 'invalidText', 'isCondensed', 'itemToElement', 'itemToString', 'items', 'label', 'loading_state', 'onChange', 'renderSelectedItem', 'selectedItem', 'style', 'titleText', 'translateWithId', 'warn', 'warnText']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'direction', 'disabled', 'initialSelectedItem', 'invalid', 'invalidText', 'isCondensed', 'itemToElement', 'itemToString', 'items', 'label', 'loading_state', 'onChange', 'renderSelectedItem', 'selectedItem', 'style', 'titleText', 'translateWithId', 'warn', 'warnText']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FluidDropdown, self).__init__(children=children, **args)

setattr(FluidDropdown, "__init__", _explicitize_args(FluidDropdown.__init__))
