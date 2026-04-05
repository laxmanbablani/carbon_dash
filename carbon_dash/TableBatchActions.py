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


class TableBatchActions(Component):
    """A TableBatchActions component.
TableBatchActions is a wrapper for the Carbon TableBatchActions component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- className (string; default ''):
    className.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- onCancel (boolean | number | string | dict | list; optional):
    onCancel.

- onSelectAll (boolean | number | string | dict | list; optional):
    onSelectAll.

- shouldShowBatchActions (boolean | number | string | dict | list; optional):
    shouldShowBatchActions.

- totalCount (boolean | number | string | dict | list; optional):
    totalCount.

- totalSelected (boolean | number | string | dict | list; optional):
    totalSelected.

- translateWithId (boolean | number | string | dict | list; optional):
    translateWithId."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'TableBatchActions'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        onCancel: typing.Optional[typing.Any] = None,
        onSelectAll: typing.Optional[typing.Any] = None,
        shouldShowBatchActions: typing.Optional[typing.Any] = None,
        totalCount: typing.Optional[typing.Any] = None,
        totalSelected: typing.Optional[typing.Any] = None,
        translateWithId: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'loading_state', 'onCancel', 'onSelectAll', 'shouldShowBatchActions', 'style', 'totalCount', 'totalSelected', 'translateWithId']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'loading_state', 'onCancel', 'onSelectAll', 'shouldShowBatchActions', 'style', 'totalCount', 'totalSelected', 'translateWithId']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(TableBatchActions, self).__init__(children=children, **args)

setattr(TableBatchActions, "__init__", _explicitize_args(TableBatchActions.__init__))
