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


class FilterableMultiSelect(Component):
    """A FilterableMultiSelect component.
FilterableMultiSelect is a wrapper for the Carbon FilterableMultiSelect component.

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

- clearSelectionDescription (boolean | number | string | dict | list; optional):
    clearSelectionDescription.

- clearSelectionText (boolean | number | string | dict | list; optional):
    clearSelectionText.

- compareItems (boolean | number | string | dict | list; optional):
    compareItems.

- decorator (boolean | number | string | dict | list; optional):
    decorator.

- direction (boolean | number | string | dict | list; optional):
    direction.

- disabled (boolean | number | string | dict | list; optional):
    disabled.

- downshiftProps (boolean | number | string | dict | list; optional):
    downshiftProps.

- filterItems (boolean | number | string | dict | list; optional):
    filterItems.

- hideLabel (boolean | number | string | dict | list; optional):
    hideLabel.

- initialSelectedItems (boolean | number | string | dict | list; optional):
    initialSelectedItems.

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

- locale (boolean | number | string | dict | list; optional):
    locale.

- onChange (boolean | number | string | dict | list; optional):
    onChange.

- onInputValueChange (boolean | number | string | dict | list; optional):
    onInputValueChange.

- onMenuChange (boolean | number | string | dict | list; optional):
    onMenuChange.

- open (boolean | number | string | dict | list; optional):
    open.

- placeholder (boolean | number | string | dict | list; optional):
    placeholder.

- selectionFeedback (boolean | number | string | dict | list; optional):
    selectionFeedback.

- size (boolean | number | string | dict | list; optional):
    size.

- slug (boolean | number | string | dict | list; optional):
    slug.

- sortItems (boolean | number | string | dict | list; optional):
    sortItems.

- titleText (boolean | number | string | dict | list; optional):
    titleText.

- translateWithId (boolean | number | string | dict | list; optional):
    translateWithId.

- type (boolean | number | string | dict | list; optional):
    type.

- useTitleInItem (boolean | number | string | dict | list; optional):
    useTitleInItem.

- warn (boolean | number | string | dict | list; optional):
    warn.

- warnText (boolean | number | string | dict | list; optional):
    warnText."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'FilterableMultiSelect'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        ariaLabel: typing.Optional[typing.Any] = None,
        autoAlign: typing.Optional[typing.Any] = None,
        clearSelectionDescription: typing.Optional[typing.Any] = None,
        clearSelectionText: typing.Optional[typing.Any] = None,
        decorator: typing.Optional[typing.Any] = None,
        filterItems: typing.Optional[typing.Any] = None,
        direction: typing.Optional[typing.Any] = None,
        disabled: typing.Optional[typing.Any] = None,
        downshiftProps: typing.Optional[typing.Any] = None,
        hideLabel: typing.Optional[typing.Any] = None,
        initialSelectedItems: typing.Optional[typing.Any] = None,
        invalid: typing.Optional[typing.Any] = None,
        invalidText: typing.Optional[typing.Any] = None,
        itemToElement: typing.Optional[typing.Any] = None,
        itemToString: typing.Optional[typing.Any] = None,
        items: typing.Optional[typing.Any] = None,
        light: typing.Optional[typing.Any] = None,
        locale: typing.Optional[typing.Any] = None,
        onChange: typing.Optional[typing.Any] = None,
        onInputValueChange: typing.Optional[typing.Any] = None,
        onMenuChange: typing.Optional[typing.Any] = None,
        open: typing.Optional[typing.Any] = None,
        placeholder: typing.Optional[typing.Any] = None,
        selectionFeedback: typing.Optional[typing.Any] = None,
        size: typing.Optional[typing.Optional[str]] = None,
        slug: typing.Optional[typing.Any] = None,
        compareItems: typing.Optional[typing.Any] = None,
        sortItems: typing.Optional[typing.Any] = None,
        titleText: typing.Optional[typing.Any] = None,
        translateWithId: typing.Optional[typing.Any] = None,
        type: typing.Optional[typing.Any] = None,
        useTitleInItem: typing.Optional[typing.Any] = None,
        warn: typing.Optional[typing.Any] = None,
        warnText: typing.Optional[typing.Any] = None,
        inputProps: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'ariaLabel', 'autoAlign', 'className', 'clearSelectionDescription', 'clearSelectionText', 'compareItems', 'decorator', 'direction', 'disabled', 'downshiftProps', 'filterItems', 'hideLabel', 'initialSelectedItems', 'inputProps', 'invalid', 'invalidText', 'itemToElement', 'itemToString', 'items', 'light', 'loading_state', 'locale', 'onChange', 'onInputValueChange', 'onMenuChange', 'open', 'placeholder', 'selectionFeedback', 'size', 'slug', 'sortItems', 'style', 'titleText', 'translateWithId', 'type', 'useTitleInItem', 'warn', 'warnText']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'ariaLabel', 'autoAlign', 'className', 'clearSelectionDescription', 'clearSelectionText', 'compareItems', 'decorator', 'direction', 'disabled', 'downshiftProps', 'filterItems', 'hideLabel', 'initialSelectedItems', 'inputProps', 'invalid', 'invalidText', 'itemToElement', 'itemToString', 'items', 'light', 'loading_state', 'locale', 'onChange', 'onInputValueChange', 'onMenuChange', 'open', 'placeholder', 'selectionFeedback', 'size', 'slug', 'sortItems', 'style', 'titleText', 'translateWithId', 'type', 'useTitleInItem', 'warn', 'warnText']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FilterableMultiSelect, self).__init__(children=children, **args)

setattr(FilterableMultiSelect, "__init__", _explicitize_args(FilterableMultiSelect.__init__))
