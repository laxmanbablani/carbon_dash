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


class Tag(Component):
    """A Tag component.
Tag is a wrapper for the Carbon Tag component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- as_ (boolean | number | string | dict | list; optional):
    as.

- className (string; default ''):
    className.

- decorator (boolean | number | string | dict | list; optional):
    decorator.

- disabled (boolean; default False):
    disabled.

- filter (boolean | number | string | dict | list; optional):
    filter.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- onClose (boolean | number | string | dict | list; optional):
    onClose.

- renderIcon (a list of or a singular dash component, string or number; optional):
    renderIcon.

- size (string; default 'md'):
    size.

- slug (boolean | number | string | dict | list; optional):
    slug.

- title (boolean | number | string | dict | list; optional):
    title.

- type (string; default 'gray'):
    type."""
    _children_props: typing.List[str] = ['renderIcon']
    _base_nodes = ['renderIcon', 'children']
    _namespace = 'carbon_dash'
    _type = 'Tag'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        as_: typing.Optional[typing.Any] = None,
        decorator: typing.Optional[typing.Any] = None,
        disabled: typing.Optional[bool] = None,
        filter: typing.Optional[typing.Any] = None,
        onClose: typing.Optional[typing.Any] = None,
        renderIcon: typing.Optional[ComponentType] = None,
        size: typing.Optional[typing.Optional[str]] = None,
        slug: typing.Optional[typing.Any] = None,
        title: typing.Optional[typing.Any] = None,
        type: typing.Optional[str] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'as_', 'className', 'decorator', 'disabled', 'filter', 'loading_state', 'onClose', 'renderIcon', 'size', 'slug', 'style', 'title', 'type']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'as_', 'className', 'decorator', 'disabled', 'filter', 'loading_state', 'onClose', 'renderIcon', 'size', 'slug', 'style', 'title', 'type']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Tag, self).__init__(children=children, **args)

setattr(Tag, "__init__", _explicitize_args(Tag.__init__))
