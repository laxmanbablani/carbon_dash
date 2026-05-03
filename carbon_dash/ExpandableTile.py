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


class ExpandableTile(Component):
    """An ExpandableTile component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional)

- belowFold (boolean; optional):
    Whether this is the below-fold content.

- className (string; optional)

- expanded (boolean; default False):
    Whether the tile is expanded.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- persisted_props (list of strings; optional)

- persistence (boolean | string | number; optional)

- persistence_type (a value equal to: 'local', 'session', 'memory'; optional)

- tileCollapsedText (a list of or a singular dash component, string or number; optional):
    Whether to collapse on expand.

- tileMaxHeight (number; optional):
    Max height before expanding.

- tileText (a list of or a singular dash component, string or number; optional):
    The tile's title (above fold)."""
    _children_props: typing.List[str] = ['tileText', 'tileCollapsedText']
    _base_nodes = ['tileText', 'tileCollapsedText', 'children']
    _namespace = 'carbon_dash'
    _type = 'ExpandableTile'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        expanded: typing.Optional[bool] = None,
        tileText: typing.Optional[ComponentType] = None,
        tileMaxHeight: typing.Optional[NumberType] = None,
        tileCollapsedText: typing.Optional[ComponentType] = None,
        belowFold: typing.Optional[bool] = None,
        persistence: typing.Optional[typing.Union[bool, str, NumberType]] = None,
        persisted_props: typing.Optional[typing.Sequence[str]] = None,
        persistence_type: typing.Optional[Literal["local", "session", "memory"]] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'belowFold', 'className', 'expanded', 'loading_state', 'persisted_props', 'persistence', 'persistence_type', 'style', 'tileCollapsedText', 'tileMaxHeight', 'tileText']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'belowFold', 'className', 'expanded', 'loading_state', 'persisted_props', 'persistence', 'persistence_type', 'style', 'tileCollapsedText', 'tileMaxHeight', 'tileText']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(ExpandableTile, self).__init__(children=children, **args)

setattr(ExpandableTile, "__init__", _explicitize_args(ExpandableTile.__init__))
