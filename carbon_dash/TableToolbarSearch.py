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


class TableToolbarSearch(Component):
    """A TableToolbarSearch component.
TableToolbarSearch is a wrapper for the Carbon TableToolbarSearch component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- className (string; default ''):
    className.

- defaultExpanded (boolean | number | string | dict | list; optional):
    defaultExpanded.

- defaultValue (boolean | number | string | dict | list; optional):
    defaultValue.

- disabled (boolean | number | string | dict | list; optional):
    disabled.

- expanded (boolean; default False):
    expanded.

- labelText (boolean | number | string | dict | list; optional):
    labelText.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- onBlur (boolean | number | string | dict | list; optional):
    onBlur.

- onChange (boolean | number | string | dict | list; optional):
    onChange.

- onClear (boolean | number | string | dict | list; optional):
    onClear.

- onExpand (boolean | number | string | dict | list; optional):
    onExpand.

- onFocus (boolean | number | string | dict | list; optional):
    onFocus.

- persistent (boolean | number | string | dict | list; optional):
    persistent.

- placeholder (boolean | number | string | dict | list; optional):
    placeholder.

- searchContainerClass (boolean | number | string | dict | list; optional):
    searchContainerClass.

- size (boolean | number | string | dict | list; optional):
    size.

- tabIndex (boolean | number | string | dict | list; optional):
    tabIndex.

- translateWithId (boolean | number | string | dict | list; optional):
    translateWithId."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'TableToolbarSearch'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        defaultExpanded: typing.Optional[typing.Any] = None,
        defaultValue: typing.Optional[typing.Any] = None,
        disabled: typing.Optional[typing.Any] = None,
        expanded: typing.Optional[bool] = None,
        labelText: typing.Optional[typing.Any] = None,
        onBlur: typing.Optional[typing.Any] = None,
        onChange: typing.Optional[typing.Any] = None,
        onClear: typing.Optional[typing.Any] = None,
        onExpand: typing.Optional[typing.Any] = None,
        onFocus: typing.Optional[typing.Any] = None,
        persistent: typing.Optional[typing.Any] = None,
        placeholder: typing.Optional[typing.Any] = None,
        searchContainerClass: typing.Optional[typing.Any] = None,
        size: typing.Optional[typing.Optional[str]] = None,
        tabIndex: typing.Optional[typing.Any] = None,
        translateWithId: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'defaultExpanded', 'defaultValue', 'disabled', 'expanded', 'labelText', 'loading_state', 'onBlur', 'onChange', 'onClear', 'onExpand', 'onFocus', 'persistent', 'placeholder', 'searchContainerClass', 'size', 'style', 'tabIndex', 'translateWithId']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'defaultExpanded', 'defaultValue', 'disabled', 'expanded', 'labelText', 'loading_state', 'onBlur', 'onChange', 'onClear', 'onExpand', 'onFocus', 'persistent', 'placeholder', 'searchContainerClass', 'size', 'style', 'tabIndex', 'translateWithId']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(TableToolbarSearch, self).__init__(children=children, **args)

setattr(TableToolbarSearch, "__init__", _explicitize_args(TableToolbarSearch.__init__))
