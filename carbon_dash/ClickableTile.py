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


class ClickableTile(Component):
    """A ClickableTile component.
ClickableTile is a wrapper for the Carbon ClickableTile component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- className (string; default ''):
    className.

- clicked (boolean | number | string | dict | list; optional):
    clicked.

- decorator (boolean | number | string | dict | list; optional):
    decorator.

- disabled (boolean | number | string | dict | list; optional):
    disabled.

- hasRoundedCorners (boolean | number | string | dict | list; optional):
    hasRoundedCorners.

- href (boolean | number | string | dict | list; optional):
    href.

- light (boolean | number | string | dict | list; optional):
    light.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- onClick (boolean | number | string | dict | list; optional):
    onClick.

- onKeyDown (boolean | number | string | dict | list; optional):
    onKeyDown.

- rel (boolean | number | string | dict | list; optional):
    rel.

- renderIcon (a list of or a singular dash component, string or number; optional):
    renderIcon."""
    _children_props: typing.List[str] = ['renderIcon']
    _base_nodes = ['renderIcon', 'children']
    _namespace = 'carbon_dash'
    _type = 'ClickableTile'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        clicked: typing.Optional[typing.Any] = None,
        decorator: typing.Optional[typing.Any] = None,
        disabled: typing.Optional[typing.Any] = None,
        hasRoundedCorners: typing.Optional[typing.Any] = None,
        href: typing.Optional[typing.Any] = None,
        light: typing.Optional[typing.Any] = None,
        onClick: typing.Optional[typing.Any] = None,
        onKeyDown: typing.Optional[typing.Any] = None,
        rel: typing.Optional[typing.Any] = None,
        renderIcon: typing.Optional[ComponentType] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'clicked', 'decorator', 'disabled', 'hasRoundedCorners', 'href', 'light', 'loading_state', 'onClick', 'onKeyDown', 'rel', 'renderIcon', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'clicked', 'decorator', 'disabled', 'hasRoundedCorners', 'href', 'light', 'loading_state', 'onClick', 'onKeyDown', 'rel', 'renderIcon', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(ClickableTile, self).__init__(children=children, **args)

setattr(ClickableTile, "__init__", _explicitize_args(ClickableTile.__init__))
