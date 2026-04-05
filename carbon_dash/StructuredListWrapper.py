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


class StructuredListWrapper(Component):
    """A StructuredListWrapper component.
StructuredListWrapper is a wrapper for the Carbon StructuredListWrapper component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- ariaLabel (boolean | number | string | dict | list; optional):
    ariaLabel.

- className (string; default ''):
    className.

- isCondensed (boolean | number | string | dict | list; optional):
    isCondensed.

- isFlush (boolean | number | string | dict | list; optional):
    isFlush.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- selectedInitialRow (boolean | number | string | dict | list; optional):
    selectedInitialRow.

- selection (boolean | number | string | dict | list; optional):
    selection."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'StructuredListWrapper'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        ariaLabel: typing.Optional[typing.Any] = None,
        isCondensed: typing.Optional[typing.Any] = None,
        isFlush: typing.Optional[typing.Any] = None,
        selection: typing.Optional[typing.Any] = None,
        selectedInitialRow: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'ariaLabel', 'className', 'isCondensed', 'isFlush', 'loading_state', 'selectedInitialRow', 'selection', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'ariaLabel', 'className', 'isCondensed', 'isFlush', 'loading_state', 'selectedInitialRow', 'selection', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(StructuredListWrapper, self).__init__(children=children, **args)

setattr(StructuredListWrapper, "__init__", _explicitize_args(StructuredListWrapper.__init__))
