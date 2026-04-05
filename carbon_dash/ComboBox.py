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
ComboBox is a wrapper for the Carbon ComboBox component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- allowCustomValue (boolean | number | string | dict | list; optional):
    allowCustomValue.

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

- downshiftActions (boolean | number | string | dict | list; optional):
    downshiftActions.

- downshiftProps (boolean | number | string | dict | list; optional):
    downshiftProps.

- helperText (boolean | number | string | dict | list; optional):
    helperText.

- initialSelectedItem (boolean | number | string | dict | list; optional):
    initialSelectedItem.

- inputProps (boolean | number | string | dict | list; optional):
    inputProps.

- invalid (boolean | number | string | dict | list; optional):
    invalid.

- invalidText (boolean | number | string | dict | list; optional):
    invalidText.

- itemToElement (boolean | number | string | dict | list; optional):
    itemToElement.

- itemToString (boolean | number | string | dict | list; optional):
    itemToString.

- items (boolean | number | string | dict | list; optional):
    items.

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

- onInputChange (boolean | number | string | dict | list; optional):
    onInputChange.

- onToggleClick (boolean | number | string | dict | list; optional):
    onToggleClick.

- placeholder (boolean | number | string | dict | list; optional):
    placeholder.

- readOnly (boolean | number | string | dict | list; optional):
    readOnly.

- selectedItem (boolean | number | string | dict | list; optional):
    selectedItem.

- shouldFilterItem (boolean | number | string | dict | list; optional):
    shouldFilterItem.

- size (boolean | number | string | dict | list; optional):
    size.

- slug (boolean | number | string | dict | list; optional):
    slug.

- titleText (boolean | number | string | dict | list; optional):
    titleText.

- translateWithId (boolean | number | string | dict | list; optional):
    translateWithId.

- typeahead (boolean | number | string | dict | list; optional):
    typeahead.

- warn (boolean | number | string | dict | list; optional):
    warn.

- warnText (boolean | number | string | dict | list; optional):
    warnText."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'ComboBox'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        allowCustomValue: typing.Optional[typing.Any] = None,
        ariaLabel: typing.Optional[typing.Any] = None,
        autoAlign: typing.Optional[typing.Any] = None,
        decorator: typing.Optional[typing.Any] = None,
        direction: typing.Optional[typing.Any] = None,
        disabled: typing.Optional[typing.Any] = None,
        downshiftProps: typing.Optional[typing.Any] = None,
        downshiftActions: typing.Optional[typing.Any] = None,
        helperText: typing.Optional[typing.Any] = None,
        initialSelectedItem: typing.Optional[typing.Any] = None,
        invalid: typing.Optional[typing.Any] = None,
        invalidText: typing.Optional[typing.Any] = None,
        itemToElement: typing.Optional[typing.Any] = None,
        itemToString: typing.Optional[typing.Any] = None,
        items: typing.Optional[typing.Any] = None,
        light: typing.Optional[typing.Any] = None,
        onChange: typing.Optional[typing.Any] = None,
        onInputChange: typing.Optional[typing.Any] = None,
        onToggleClick: typing.Optional[typing.Any] = None,
        placeholder: typing.Optional[typing.Any] = None,
        readOnly: typing.Optional[typing.Any] = None,
        selectedItem: typing.Optional[typing.Any] = None,
        shouldFilterItem: typing.Optional[typing.Any] = None,
        size: typing.Optional[typing.Optional[str]] = None,
        slug: typing.Optional[typing.Any] = None,
        titleText: typing.Optional[typing.Any] = None,
        translateWithId: typing.Optional[typing.Any] = None,
        typeahead: typing.Optional[typing.Any] = None,
        warn: typing.Optional[typing.Any] = None,
        warnText: typing.Optional[typing.Any] = None,
        inputProps: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'allowCustomValue', 'ariaLabel', 'autoAlign', 'className', 'decorator', 'direction', 'disabled', 'downshiftActions', 'downshiftProps', 'helperText', 'initialSelectedItem', 'inputProps', 'invalid', 'invalidText', 'itemToElement', 'itemToString', 'items', 'light', 'loading_state', 'onChange', 'onInputChange', 'onToggleClick', 'placeholder', 'readOnly', 'selectedItem', 'shouldFilterItem', 'size', 'slug', 'style', 'titleText', 'translateWithId', 'typeahead', 'warn', 'warnText']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'allowCustomValue', 'ariaLabel', 'autoAlign', 'className', 'decorator', 'direction', 'disabled', 'downshiftActions', 'downshiftProps', 'helperText', 'initialSelectedItem', 'inputProps', 'invalid', 'invalidText', 'itemToElement', 'itemToString', 'items', 'light', 'loading_state', 'onChange', 'onInputChange', 'onToggleClick', 'placeholder', 'readOnly', 'selectedItem', 'shouldFilterItem', 'size', 'slug', 'style', 'titleText', 'translateWithId', 'typeahead', 'warn', 'warnText']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(ComboBox, self).__init__(children=children, **args)

setattr(ComboBox, "__init__", _explicitize_args(ComboBox.__init__))
