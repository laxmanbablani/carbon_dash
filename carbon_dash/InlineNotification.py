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


class InlineNotification(Component):
    """An InlineNotification component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional)

- className (string; optional)

- hideCloseButton (boolean; default False)

- kind (a value equal to: 'error', 'info', 'info-square', 'success', 'warning'; default 'info')

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- lowContrast (boolean; default False)

- role (string; optional)

- statusIconDescription (string; optional)

- subtitle (a list of or a singular dash component, string or number; optional)

- title (string; optional)"""
    _children_props: typing.List[str] = ['subtitle']
    _base_nodes = ['subtitle', 'children']
    _namespace = 'carbon_dash'
    _type = 'InlineNotification'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        title: typing.Optional[str] = None,
        subtitle: typing.Optional[ComponentType] = None,
        kind: typing.Optional[typing.Optional[str]] = None,
        lowContrast: typing.Optional[bool] = None,
        hideCloseButton: typing.Optional[bool] = None,
        statusIconDescription: typing.Optional[str] = None,
        role: typing.Optional[str] = None,
        onCloseButtonClick: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'hideCloseButton', 'kind', 'loading_state', 'lowContrast', 'role', 'statusIconDescription', 'style', 'subtitle', 'title']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'hideCloseButton', 'kind', 'loading_state', 'lowContrast', 'role', 'statusIconDescription', 'style', 'subtitle', 'title']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(InlineNotification, self).__init__(children=children, **args)

setattr(InlineNotification, "__init__", _explicitize_args(InlineNotification.__init__))
