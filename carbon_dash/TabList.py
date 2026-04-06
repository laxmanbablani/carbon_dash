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


class TabList(Component):
    """A TabList component.
TabList is a wrapper for the Carbon TabList component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- activation (boolean | number | string | dict | list; optional):
    activation.

- className (string; default ''):
    className.

- contained (boolean; default False):
    contained.

- fullWidth (boolean | number | string | dict | list; optional):
    fullWidth.

- iconSize (a list of or a singular dash component, string or number; optional):
    iconSize.

- leftOverflowButtonProps (boolean | number | string | dict | list; optional):
    leftOverflowButtonProps.

- light (boolean | number | string | dict | list; optional):
    light.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- rightOverflowButtonProps (boolean | number | string | dict | list; optional):
    rightOverflowButtonProps.

- scrollDebounceWait (boolean | number | string | dict | list; optional):
    scrollDebounceWait.

- scrollIntoView (boolean | number | string | dict | list; optional):
    scrollIntoView."""
    _children_props: typing.List[str] = ['iconSize']
    _base_nodes = ['iconSize', 'children']
    _namespace = 'carbon_dash'
    _type = 'TabList'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        activation: typing.Optional[typing.Any] = None,
        contained: typing.Optional[bool] = None,
        fullWidth: typing.Optional[typing.Any] = None,
        iconSize: typing.Optional[ComponentType] = None,
        leftOverflowButtonProps: typing.Optional[typing.Any] = None,
        light: typing.Optional[typing.Any] = None,
        rightOverflowButtonProps: typing.Optional[typing.Any] = None,
        scrollDebounceWait: typing.Optional[typing.Any] = None,
        scrollIntoView: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'activation', 'className', 'contained', 'fullWidth', 'iconSize', 'leftOverflowButtonProps', 'light', 'loading_state', 'rightOverflowButtonProps', 'scrollDebounceWait', 'scrollIntoView', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'activation', 'className', 'contained', 'fullWidth', 'iconSize', 'leftOverflowButtonProps', 'light', 'loading_state', 'rightOverflowButtonProps', 'scrollDebounceWait', 'scrollIntoView', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(TabList, self).__init__(children=children, **args)

setattr(TabList, "__init__", _explicitize_args(TabList.__init__))
