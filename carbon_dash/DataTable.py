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


class DataTable(Component):
    """A DataTable component.
DataTable is a wrapper for the Carbon DataTable component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- className (string; default ''):
    className.

- description (string; default ''):
    description.

- experimentalAutoAlign (boolean | number | string | dict | list; optional):
    experimentalAutoAlign.

- filterRows (boolean | number | string | dict | list; optional):
    filterRows.

- header (boolean | number | string | dict | list; optional):
    header.

- headers (list; optional):
    headers.

- isSortable (boolean; default False):
    isSortable.

- key (boolean | number | string | dict | list; optional):
    key.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- locale (boolean | number | string | dict | list; optional):
    locale.

- overflowMenuOnHover (boolean | number | string | dict | list; optional):
    overflowMenuOnHover.

- radio (boolean | number | string | dict | list; optional):
    radio.

- render (boolean | number | string | dict | list; optional):
    render.

- rows (list; optional):
    rows.

- size (string; default 'lg'):
    size.

- sortRow (boolean | number | string | dict | list; optional):
    sortRow.

- stickyHeader (boolean | number | string | dict | list; optional):
    stickyHeader.

- title (string; default ''):
    title.

- translateWithId (boolean | number | string | dict | list; optional):
    translateWithId.

- useStaticWidth (boolean | number | string | dict | list; optional):
    useStaticWidth.

- useZebraStyles (boolean; default False):
    useZebraStyles.

- withExpansion (boolean; default False):
    withExpansion.

- withSelection (boolean; default False):
    withSelection."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'DataTable'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        experimentalAutoAlign: typing.Optional[typing.Any] = None,
        filterRows: typing.Optional[typing.Any] = None,
        headers: typing.Optional[typing.Sequence] = None,
        key: typing.Optional[typing.Any] = None,
        header: typing.Optional[typing.Any] = None,
        isSortable: typing.Optional[bool] = None,
        locale: typing.Optional[typing.Any] = None,
        overflowMenuOnHover: typing.Optional[typing.Any] = None,
        radio: typing.Optional[typing.Any] = None,
        render: typing.Optional[typing.Any] = None,
        rows: typing.Optional[typing.Sequence] = None,
        size: typing.Optional[typing.Optional[str]] = None,
        sortRow: typing.Optional[typing.Any] = None,
        stickyHeader: typing.Optional[typing.Any] = None,
        translateWithId: typing.Optional[typing.Any] = None,
        useStaticWidth: typing.Optional[typing.Any] = None,
        useZebraStyles: typing.Optional[bool] = None,
        title: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        withSelection: typing.Optional[bool] = None,
        withExpansion: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'description', 'experimentalAutoAlign', 'filterRows', 'header', 'headers', 'isSortable', 'key', 'loading_state', 'locale', 'overflowMenuOnHover', 'radio', 'render', 'rows', 'size', 'sortRow', 'stickyHeader', 'style', 'title', 'translateWithId', 'useStaticWidth', 'useZebraStyles', 'withExpansion', 'withSelection']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'description', 'experimentalAutoAlign', 'filterRows', 'header', 'headers', 'isSortable', 'key', 'loading_state', 'locale', 'overflowMenuOnHover', 'radio', 'render', 'rows', 'size', 'sortRow', 'stickyHeader', 'style', 'title', 'translateWithId', 'useStaticWidth', 'useZebraStyles', 'withExpansion', 'withSelection']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(DataTable, self).__init__(children=children, **args)

setattr(DataTable, "__init__", _explicitize_args(DataTable.__init__))
