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


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional)

- className (string; optional)

- disabled (boolean; default False)

- invalid (boolean; default False)

- legendId (a list of or a singular dash component, string or number; optional)

- legendText (a list of or a singular dash component, string or number; required)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- message (boolean; default False)

- messageText (string; default '')"""
    _children_props: typing.List[str] = ['legendText', 'legendId']
    _base_nodes = ['legendText', 'legendId', 'children']
    _namespace = 'carbon_dash'
    _type = 'FormGroup'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        legendText: typing.Optional[ComponentType] = None,
        legendId: typing.Optional[ComponentType] = None,
        message: typing.Optional[bool] = None,
        messageText: typing.Optional[str] = None,
        invalid: typing.Optional[bool] = None,
        disabled: typing.Optional[bool] = None,
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

        for k in ['legendText']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(FormGroup, self).__init__(children=children, **args)

setattr(FormGroup, "__init__", _explicitize_args(FormGroup.__init__))
