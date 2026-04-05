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


class Link(Component):
    """A Link component.
Link is a wrapper for the Carbon Link component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- as_ (boolean | number | string | dict | list; optional):
    as.

- className (string; default ''):
    className.

- disabled (boolean | number | string | dict | list; optional):
    disabled.

- href (boolean | number | string | dict | list; optional):
    href.

- inline (boolean | number | string | dict | list; optional):
    inline.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- renderIcon (boolean | number | string | dict | list; optional):
    renderIcon.

- size (boolean | number | string | dict | list; optional):
    size.

- visited (boolean | number | string | dict | list; optional):
    visited."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'Link'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        as_: typing.Optional[typing.Any] = None,
        disabled: typing.Optional[typing.Any] = None,
        href: typing.Optional[typing.Any] = None,
        inline: typing.Optional[typing.Any] = None,
        renderIcon: typing.Optional[typing.Any] = None,
        size: typing.Optional[typing.Optional[str]] = None,
        visited: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'as_', 'className', 'disabled', 'href', 'inline', 'loading_state', 'renderIcon', 'size', 'style', 'visited']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'as_', 'className', 'disabled', 'href', 'inline', 'loading_state', 'renderIcon', 'size', 'style', 'visited']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Link, self).__init__(children=children, **args)

setattr(Link, "__init__", _explicitize_args(Link.__init__))
