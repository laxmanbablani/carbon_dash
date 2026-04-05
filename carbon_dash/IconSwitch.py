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


class IconSwitch(Component):
    """An IconSwitch component.
IconSwitch is a wrapper for the Carbon IconSwitch component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- align (boolean | number | string | dict | list; optional):
    align.

- className (string; default ''):
    className.

- disabled (boolean | number | string | dict | list; optional):
    disabled.

- enterDelayMs (boolean | number | string | dict | list; optional):
    enterDelayMs.

- index (boolean | number | string | dict | list; optional):
    index.

- leaveDelayMs (boolean | number | string | dict | list; optional):
    leaveDelayMs.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- name (boolean | number | string | dict | list; optional):
    name.

- onClick (boolean | number | string | dict | list; optional):
    onClick.

- onKeyDown (boolean | number | string | dict | list; optional):
    onKeyDown.

- selected (boolean | number | string | dict | list; optional):
    selected.

- size (boolean | number | string | dict | list; optional):
    size.

- text (boolean | number | string | dict | list; optional):
    text."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'IconSwitch'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        align: typing.Optional[typing.Any] = None,
        disabled: typing.Optional[typing.Any] = None,
        enterDelayMs: typing.Optional[typing.Any] = None,
        index: typing.Optional[typing.Any] = None,
        leaveDelayMs: typing.Optional[typing.Any] = None,
        name: typing.Optional[typing.Any] = None,
        onClick: typing.Optional[typing.Any] = None,
        onKeyDown: typing.Optional[typing.Any] = None,
        selected: typing.Optional[typing.Any] = None,
        size: typing.Optional[typing.Optional[str]] = None,
        text: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'align', 'className', 'disabled', 'enterDelayMs', 'index', 'leaveDelayMs', 'loading_state', 'name', 'onClick', 'onKeyDown', 'selected', 'size', 'style', 'text']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'align', 'className', 'disabled', 'enterDelayMs', 'index', 'leaveDelayMs', 'loading_state', 'name', 'onClick', 'onKeyDown', 'selected', 'size', 'style', 'text']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(IconSwitch, self).__init__(children=children, **args)

setattr(IconSwitch, "__init__", _explicitize_args(IconSwitch.__init__))
