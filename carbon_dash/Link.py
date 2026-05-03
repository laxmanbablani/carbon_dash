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


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional)

- className (string; optional)

- disabled (boolean; default False):
    Whether the link is disabled.

- href (string; optional):
    Provide the href for the link.

- inline (boolean; default True):
    Whether the link is inline (default) or standalone.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- size (a value equal to: 'sm', 'md', 'lg'; optional):
    Size of the link.

- target (string; optional):
    Specify the target attribute.

- visited (boolean; optional):
    Whether to render the visited state."""
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
        href: typing.Optional[str] = None,
        inline: typing.Optional[bool] = None,
        size: typing.Optional[typing.Optional[str]] = None,
        visited: typing.Optional[bool] = None,
        disabled: typing.Optional[bool] = None,
        target: typing.Optional[str] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'disabled', 'href', 'inline', 'loading_state', 'size', 'style', 'target', 'visited']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'disabled', 'href', 'inline', 'loading_state', 'size', 'style', 'target', 'visited']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Link, self).__init__(children=children, **args)

setattr(Link, "__init__", _explicitize_args(Link.__init__))
