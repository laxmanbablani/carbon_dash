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


class HeaderName(Component):
    """A HeaderName component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The content of the header name.

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- as (optional):
    Provide a custom element or component to render the top-level node
    for the component.

- className (string; optional):
    Custom CSS class.

- element (optional):
    The base element to use to build the link. Defaults to `a`.
    @deprecated Use `as` instead.

- href (string; optional):
    Provide an href for the name to link to.

- isSideNavExpanded (boolean; optional):
    Property to indicate if the side nav container is open (or not).

- loading_state (dict; optional):
    Dash loading state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- prefix (string; default 'IBM'):
    Optionally specify a prefix to your header name. Useful for
    companies, for example: IBM [Product Name] versus solely [Product
    Name]."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'HeaderName'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        href: typing.Optional[str] = None,
        prefix: typing.Optional[str] = None,
        element: typing.Optional[typing.Any] = None,
        isSideNavExpanded: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'as', 'className', 'element', 'href', 'isSideNavExpanded', 'loading_state', 'prefix', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'as', 'className', 'element', 'href', 'isSideNavExpanded', 'loading_state', 'prefix', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(HeaderName, self).__init__(children=children, **args)

setattr(HeaderName, "__init__", _explicitize_args(HeaderName.__init__))
