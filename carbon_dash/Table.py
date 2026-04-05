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


class Table(Component):
    """A Table component.
Table is a wrapper for the Carbon Table component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- className (string; default ''):
    className.

- experimentalAutoAlign (boolean | number | string | dict | list; optional):
    experimentalAutoAlign.

- isSortable (boolean | number | string | dict | list; optional):
    isSortable.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- overflowMenuOnHover (boolean | number | string | dict | list; optional):
    overflowMenuOnHover.

- size (boolean | number | string | dict | list; optional):
    size.

- stickyHeader (boolean | number | string | dict | list; optional):
    stickyHeader.

- tabIndex (boolean | number | string | dict | list; optional):
    tabIndex.

- useStaticWidth (boolean | number | string | dict | list; optional):
    useStaticWidth.

- useZebraStyles (boolean | number | string | dict | list; optional):
    useZebraStyles."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'Table'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        experimentalAutoAlign: typing.Optional[typing.Any] = None,
        isSortable: typing.Optional[typing.Any] = None,
        overflowMenuOnHover: typing.Optional[typing.Any] = None,
        size: typing.Optional[typing.Optional[str]] = None,
        stickyHeader: typing.Optional[typing.Any] = None,
        useStaticWidth: typing.Optional[typing.Any] = None,
        useZebraStyles: typing.Optional[typing.Any] = None,
        tabIndex: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'experimentalAutoAlign', 'isSortable', 'loading_state', 'overflowMenuOnHover', 'size', 'stickyHeader', 'style', 'tabIndex', 'useStaticWidth', 'useZebraStyles']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'experimentalAutoAlign', 'isSortable', 'loading_state', 'overflowMenuOnHover', 'size', 'stickyHeader', 'style', 'tabIndex', 'useStaticWidth', 'useZebraStyles']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Table, self).__init__(children=children, **args)

setattr(Table, "__init__", _explicitize_args(Table.__init__))
