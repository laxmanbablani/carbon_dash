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


class SwitcherItem(Component):
    """A SwitcherItem component.
SwitcherItem is a wrapper for the Carbon SwitcherItem component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- className (string; default ''):
    className.

- handleSwitcherItemFocus (boolean | number | string | dict | list; optional):
    handleSwitcherItemFocus.

- href (boolean | number | string | dict | list; optional):
    href.

- index (boolean | number | string | dict | list; optional):
    index.

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

- tabIndex (boolean | number | string | dict | list; optional):
    tabIndex.

- target (boolean | number | string | dict | list; optional):
    target."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'SwitcherItem'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        handleSwitcherItemFocus: typing.Optional[typing.Any] = None,
        href: typing.Optional[typing.Any] = None,
        index: typing.Optional[typing.Any] = None,
        onClick: typing.Optional[typing.Any] = None,
        onKeyDown: typing.Optional[typing.Any] = None,
        tabIndex: typing.Optional[typing.Any] = None,
        target: typing.Optional[typing.Any] = None,
        rel: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'handleSwitcherItemFocus', 'href', 'index', 'loading_state', 'onClick', 'onKeyDown', 'rel', 'style', 'tabIndex', 'target']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'handleSwitcherItemFocus', 'href', 'index', 'loading_state', 'onClick', 'onKeyDown', 'rel', 'style', 'tabIndex', 'target']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(SwitcherItem, self).__init__(children=children, **args)

setattr(SwitcherItem, "__init__", _explicitize_args(SwitcherItem.__init__))
