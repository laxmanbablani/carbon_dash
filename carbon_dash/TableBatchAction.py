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


class TableBatchAction(Component):
    """A TableBatchAction component.
TableBatchAction is a wrapper for the Carbon TableBatchAction component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- className (string; default ''):
    className.

- hasIconOnly (boolean | number | string | dict | list; optional):
    hasIconOnly.

- iconDescription (boolean | number | string | dict | list; optional):
    iconDescription.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- renderIcon (a list of or a singular dash component, string or number; optional):
    renderIcon."""
    _children_props: typing.List[str] = ['renderIcon']
    _base_nodes = ['renderIcon', 'children']
    _namespace = 'carbon_dash'
    _type = 'TableBatchAction'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        hasIconOnly: typing.Optional[typing.Any] = None,
        iconDescription: typing.Optional[typing.Any] = None,
        renderIcon: typing.Optional[ComponentType] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'hasIconOnly', 'iconDescription', 'loading_state', 'renderIcon', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'hasIconOnly', 'iconDescription', 'loading_state', 'renderIcon', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(TableBatchAction, self).__init__(children=children, **args)

setattr(TableBatchAction, "__init__", _explicitize_args(TableBatchAction.__init__))
