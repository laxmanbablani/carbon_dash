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


class PaginationNav(Component):
    """A PaginationNav component.
PaginationNav is a wrapper for the Carbon PaginationNav component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- className (string; default ''):
    className.

- disableOverflow (boolean | number | string | dict | list; optional):
    disableOverflow.

- itemsShown (boolean | number | string | dict | list; optional):
    itemsShown.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- loop (boolean | number | string | dict | list; optional):
    loop.

- onChange (boolean | number | string | dict | list; optional):
    onChange.

- page (boolean | number | string | dict | list; optional):
    page.

- size (boolean | number | string | dict | list; optional):
    size.

- tooltipAlignment (boolean | number | string | dict | list; optional):
    tooltipAlignment.

- tooltipPosition (boolean | number | string | dict | list; optional):
    tooltipPosition.

- totalItems (boolean | number | string | dict | list; optional):
    totalItems.

- translateWithId (boolean | number | string | dict | list; optional):
    translateWithId."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'PaginationNav'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        disableOverflow: typing.Optional[typing.Any] = None,
        itemsShown: typing.Optional[typing.Any] = None,
        loop: typing.Optional[typing.Any] = None,
        onChange: typing.Optional[typing.Any] = None,
        page: typing.Optional[typing.Any] = None,
        size: typing.Optional[typing.Optional[str]] = None,
        tooltipAlignment: typing.Optional[typing.Any] = None,
        tooltipPosition: typing.Optional[typing.Any] = None,
        totalItems: typing.Optional[typing.Any] = None,
        translateWithId: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'disableOverflow', 'itemsShown', 'loading_state', 'loop', 'onChange', 'page', 'size', 'style', 'tooltipAlignment', 'tooltipPosition', 'totalItems', 'translateWithId']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'disableOverflow', 'itemsShown', 'loading_state', 'loop', 'onChange', 'page', 'size', 'style', 'tooltipAlignment', 'tooltipPosition', 'totalItems', 'translateWithId']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(PaginationNav, self).__init__(children=children, **args)

setattr(PaginationNav, "__init__", _explicitize_args(PaginationNav.__init__))
