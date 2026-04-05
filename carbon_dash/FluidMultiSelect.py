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
FluidMultiSelect is a wrapper for the Carbon FluidMultiSelect component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- className (string; default ''):
    className.

- clearSelectionDescription (boolean | number | string | dict | list; optional):
    clearSelectionDescription.

- clearSelectionText (boolean | number | string | dict | list; optional):
    clearSelectionText.

- compareItems (boolean | number | string | dict | list; optional):
    compareItems.

- direction (boolean | number | string | dict | list; optional):
    direction.

- disabled (boolean | number | string | dict | list; optional):
    disabled.

- downshiftProps (boolean | number | string | dict | list; optional):
    downshiftProps.

- initialSelectedItems (boolean | number | string | dict | list; optional):
    initialSelectedItems.

- invalid (boolean | number | string | dict | list; optional):
    invalid.

- invalidText (boolean | number | string | dict | list; optional):
    invalidText.

- isCondensed (boolean | number | string | dict | list; optional):
    isCondensed.

- isFilterable (boolean | number | string | dict | list; optional):
    isFilterable.

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

- locale (boolean | number | string | dict | list; optional):
    locale.

- onChange (boolean | number | string | dict | list; optional):
    onChange.

- onInputValueChange (boolean | number | string | dict | list; optional):
    onInputValueChange.

- onMenuChange (boolean | number | string | dict | list; optional):
    onMenuChange.

- readOnly (boolean | number | string | dict | list; optional):
    readOnly.

- selectedItems (boolean | number | string | dict | list; optional):
    selectedItems.

- selectionFeedback (boolean | number | string | dict | list; optional):
    selectionFeedback.

- sortItems (boolean | number | string | dict | list; optional):
    sortItems.

- titleText (boolean | number | string | dict | list; optional):
    titleText.

- translateWithId (boolean | number | string | dict | list; optional):
    translateWithId.

- useTitleInItem (boolean | number | string | dict | list; optional):
    useTitleInItem.

- warn (boolean | number | string | dict | list; optional):
    warn.

- warnText (boolean | number | string | dict | list; optional):
    warnText."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'FluidMultiSelect'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        clearSelectionDescription: typing.Optional[typing.Any] = None,
        clearSelectionText: typing.Optional[typing.Any] = None,
        compareItems: typing.Optional[typing.Any] = None,
        direction: typing.Optional[typing.Any] = None,
        disabled: typing.Optional[typing.Any] = None,
        downshiftProps: typing.Optional[typing.Any] = None,
        initialSelectedItems: typing.Optional[typing.Any] = None,
        invalid: typing.Optional[typing.Any] = None,
        invalidText: typing.Optional[typing.Any] = None,
        isCondensed: typing.Optional[typing.Any] = None,
        isFilterable: typing.Optional[typing.Any] = None,
        itemToElement: typing.Optional[typing.Any] = None,
        itemToString: typing.Optional[typing.Any] = None,
        items: typing.Optional[typing.Any] = None,
        label: typing.Optional[typing.Any] = None,
        locale: typing.Optional[typing.Any] = None,
        onChange: typing.Optional[typing.Any] = None,
        onInputValueChange: typing.Optional[typing.Any] = None,
        onMenuChange: typing.Optional[typing.Any] = None,
        readOnly: typing.Optional[typing.Any] = None,
        selectedItems: typing.Optional[typing.Any] = None,
        selectionFeedback: typing.Optional[typing.Any] = None,
        sortItems: typing.Optional[typing.Any] = None,
        titleText: typing.Optional[typing.Any] = None,
        translateWithId: typing.Optional[typing.Any] = None,
        useTitleInItem: typing.Optional[typing.Any] = None,
        warn: typing.Optional[typing.Any] = None,
        warnText: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'clearSelectionDescription', 'clearSelectionText', 'compareItems', 'direction', 'disabled', 'downshiftProps', 'initialSelectedItems', 'invalid', 'invalidText', 'isCondensed', 'isFilterable', 'itemToElement', 'itemToString', 'items', 'label', 'loading_state', 'locale', 'onChange', 'onInputValueChange', 'onMenuChange', 'readOnly', 'selectedItems', 'selectionFeedback', 'sortItems', 'style', 'titleText', 'translateWithId', 'useTitleInItem', 'warn', 'warnText']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'clearSelectionDescription', 'clearSelectionText', 'compareItems', 'direction', 'disabled', 'downshiftProps', 'initialSelectedItems', 'invalid', 'invalidText', 'isCondensed', 'isFilterable', 'itemToElement', 'itemToString', 'items', 'label', 'loading_state', 'locale', 'onChange', 'onInputValueChange', 'onMenuChange', 'readOnly', 'selectedItems', 'selectionFeedback', 'sortItems', 'style', 'titleText', 'translateWithId', 'useTitleInItem', 'warn', 'warnText']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FluidMultiSelect, self).__init__(children=children, **args)

setattr(FluidMultiSelect, "__init__", _explicitize_args(FluidMultiSelect.__init__))
