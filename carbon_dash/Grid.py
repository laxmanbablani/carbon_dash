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


class Grid(Component):
    """A Grid component.
Grid is a wrapper for the Carbon Grid component.
Provides the top-level grid container for layout.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The content of the grid.

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- align (a value equal to: 'start', 'center', 'end'; optional):
    Specify grid alignment: 'start', 'center', or 'end'.

- className (string; optional):
    Custom CSS class.

- condensed (boolean; default False):
    Collapse the gutter to 1px. Useful for fluid layouts.

- fullWidth (boolean; default False):
    Remove the default max width the grid has set.

- loading_state (dict; optional):
    Dash loading state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- narrow (boolean; default False):
    Container hangs 16px into the gutter. Useful for typographic
    alignment."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'Grid'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        align: typing.Optional[Literal["start", "center", "end"]] = None,
        condensed: typing.Optional[bool] = None,
        fullWidth: typing.Optional[bool] = None,
        narrow: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'align', 'className', 'condensed', 'fullWidth', 'loading_state', 'narrow', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'align', 'className', 'condensed', 'fullWidth', 'loading_state', 'narrow', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Grid, self).__init__(children=children, **args)

setattr(Grid, "__init__", _explicitize_args(Grid.__init__))
