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


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Alternative content.

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- className (string; optional):
    Custom CSS class.

- description (string; optional):
    Table description.

- headers (list of dicts; optional):
    Array of header configs: {key: string, header: string}.

    `headers` is a list of dicts with keys:

    - key (string; required)

    - header (a list of or a singular dash component, string or number; required)

    - isSortable (boolean; optional)

- isSortable (boolean; default False):
    Allow sorting by clicking column headers.

- loading_state (dict; optional):
    Dash loading state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- rows (list of dicts; optional):
    Array of row objects. Each row MUST have a unique `id` string.

- selectedRows (list of strings; optional):
    Array of selected row IDs (read via Dash callback).

- size (a value equal to: 'xs', 'sm', 'md', 'lg', 'xl', '2xl'; optional):
    Table size.

- stickyHeader (boolean; optional):
    Make header sticky.

- title (string; optional):
    Table title.

- useZebraStyles (boolean; default False):
    Add zebra striping.

- withSelection (boolean; default False):
    Show row selection checkboxes.

- withToolbar (boolean; default False):
    Show toolbar with search/filter."""
    _children_props: typing.List[str] = ['headers[].header']
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'DataTable'
    Headers = TypedDict(
        "Headers",
            {
            "key": str,
            "header": ComponentType,
            "isSortable": NotRequired[bool]
        }
    )


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        rows: typing.Optional[typing.Sequence[dict]] = None,
        headers: typing.Optional[typing.Sequence["Headers"]] = None,
        isSortable: typing.Optional[bool] = None,
        withSelection: typing.Optional[bool] = None,
        withToolbar: typing.Optional[bool] = None,
        selectedRows: typing.Optional[typing.Sequence[str]] = None,
        useZebraStyles: typing.Optional[bool] = None,
        title: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        stickyHeader: typing.Optional[bool] = None,
        size: typing.Optional[typing.Optional[str]] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'description', 'headers', 'isSortable', 'loading_state', 'rows', 'selectedRows', 'size', 'stickyHeader', 'style', 'title', 'useZebraStyles', 'withSelection', 'withToolbar']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'description', 'headers', 'isSortable', 'loading_state', 'rows', 'selectedRows', 'size', 'stickyHeader', 'style', 'title', 'useZebraStyles', 'withSelection', 'withToolbar']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(DataTable, self).__init__(children=children, **args)

setattr(DataTable, "__init__", _explicitize_args(DataTable.__init__))
