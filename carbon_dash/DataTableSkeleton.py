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


class DataTableSkeleton(Component):
    """A DataTableSkeleton component.
DataTableSkeleton is a wrapper for the Carbon DataTableSkeleton component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- className (string; default ''):
    className.

- columnCount (boolean | number | string | dict | list; optional):
    columnCount.

- headers (boolean | number | string | dict | list; optional):
    headers.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- rowCount (boolean | number | string | dict | list; optional):
    rowCount.

- showHeader (boolean | number | string | dict | list; optional):
    showHeader.

- showToolbar (boolean | number | string | dict | list; optional):
    showToolbar.

- size (boolean | number | string | dict | list; optional):
    size.

- zebra (boolean | number | string | dict | list; optional):
    zebra."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'DataTableSkeleton'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        columnCount: typing.Optional[typing.Any] = None,
        headers: typing.Optional[typing.Any] = None,
        rowCount: typing.Optional[typing.Any] = None,
        showHeader: typing.Optional[typing.Any] = None,
        showToolbar: typing.Optional[typing.Any] = None,
        size: typing.Optional[typing.Optional[str]] = None,
        zebra: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'columnCount', 'headers', 'loading_state', 'rowCount', 'showHeader', 'showToolbar', 'size', 'style', 'zebra']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'columnCount', 'headers', 'loading_state', 'rowCount', 'showHeader', 'showToolbar', 'size', 'style', 'zebra']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(DataTableSkeleton, self).__init__(children=children, **args)

setattr(DataTableSkeleton, "__init__", _explicitize_args(DataTableSkeleton.__init__))
