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


class CheckboxGroup(Component):
    """A CheckboxGroup component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional)

- className (string; optional)

- helperText (a list of or a singular dash component, string or number; optional)

- invalid (boolean; default False)

- invalidText (a list of or a singular dash component, string or number; optional)

- legendText (a list of or a singular dash component, string or number; optional)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- orientation (a value equal to: 'horizontal', 'vertical'; default 'horizontal')

- readOnly (boolean; default False)

- warn (boolean; default False)

- warnText (a list of or a singular dash component, string or number; optional)"""
    _children_props: typing.List[str] = ['legendText', 'helperText', 'invalidText', 'warnText']
    _base_nodes = ['legendText', 'helperText', 'invalidText', 'warnText', 'children']
    _namespace = 'carbon_dash'
    _type = 'CheckboxGroup'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        legendText: typing.Optional[ComponentType] = None,
        helperText: typing.Optional[ComponentType] = None,
        orientation: typing.Optional[Literal["horizontal", "vertical"]] = None,
        invalid: typing.Optional[bool] = None,
        invalidText: typing.Optional[ComponentType] = None,
        warn: typing.Optional[bool] = None,
        warnText: typing.Optional[ComponentType] = None,
        readOnly: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'helperText', 'invalid', 'invalidText', 'legendText', 'loading_state', 'orientation', 'readOnly', 'style', 'warn', 'warnText']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'helperText', 'invalid', 'invalidText', 'legendText', 'loading_state', 'orientation', 'readOnly', 'style', 'warn', 'warnText']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(CheckboxGroup, self).__init__(children=children, **args)

setattr(CheckboxGroup, "__init__", _explicitize_args(CheckboxGroup.__init__))
