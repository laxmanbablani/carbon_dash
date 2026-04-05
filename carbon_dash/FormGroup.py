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


class FormGroup(Component):
    """A FormGroup component.
FormGroup is a wrapper for the Carbon FormGroup component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- className (string; default ''):
    className.

- disabled (boolean | number | string | dict | list; optional):
    disabled.

- invalid (boolean | number | string | dict | list; optional):
    invalid.

- legendId (boolean | number | string | dict | list; optional):
    legendId.

- legendText (boolean | number | string | dict | list; optional):
    legendText.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- message (boolean | number | string | dict | list; optional):
    message.

- messageText (boolean | number | string | dict | list; optional):
    messageText."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'FormGroup'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        disabled: typing.Optional[typing.Any] = None,
        invalid: typing.Optional[typing.Any] = None,
        legendId: typing.Optional[typing.Any] = None,
        legendText: typing.Optional[typing.Any] = None,
        message: typing.Optional[typing.Any] = None,
        messageText: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'disabled', 'invalid', 'legendId', 'legendText', 'loading_state', 'message', 'messageText', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'disabled', 'invalid', 'legendId', 'legendText', 'loading_state', 'message', 'messageText', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FormGroup, self).__init__(children=children, **args)

setattr(FormGroup, "__init__", _explicitize_args(FormGroup.__init__))
