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


class TableExpandRow(Component):
    """A TableExpandRow component.
TableExpandRow is a wrapper for the Carbon TableExpandRow component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- ariaLabel (boolean | number | string | dict | list; optional):
    ariaLabel.

- className (string; default ''):
    className.

- expandHeader (boolean | number | string | dict | list; optional):
    expandHeader.

- expandIconDescription (boolean | number | string | dict | list; optional):
    expandIconDescription.

- isExpanded (boolean | number | string | dict | list; optional):
    isExpanded.

- isSelected (boolean | number | string | dict | list; optional):
    isSelected.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- onExpand (boolean | number | string | dict | list; optional):
    onExpand."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'TableExpandRow'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        ariaLabel: typing.Optional[typing.Any] = None,
        expandHeader: typing.Optional[typing.Any] = None,
        expandIconDescription: typing.Optional[typing.Any] = None,
        isExpanded: typing.Optional[typing.Any] = None,
        isSelected: typing.Optional[typing.Any] = None,
        onExpand: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'ariaLabel', 'className', 'expandHeader', 'expandIconDescription', 'isExpanded', 'isSelected', 'loading_state', 'onExpand', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'ariaLabel', 'className', 'expandHeader', 'expandIconDescription', 'isExpanded', 'isSelected', 'loading_state', 'onExpand', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(TableExpandRow, self).__init__(children=children, **args)

setattr(TableExpandRow, "__init__", _explicitize_args(TableExpandRow.__init__))
