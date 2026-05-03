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


class ProgressStep(Component):
    """A ProgressStep component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional)

- className (string; optional)

- complete (boolean; default False)

- current (boolean; default False)

- description (a list of or a singular dash component, string or number; optional)

- disabled (boolean; default False)

- invalid (boolean; default False)

- label (a list of or a singular dash component, string or number; optional)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- secondaryLabel (a list of or a singular dash component, string or number; optional)"""
    _children_props: typing.List[str] = ['label', 'description', 'secondaryLabel']
    _base_nodes = ['label', 'description', 'secondaryLabel', 'children']
    _namespace = 'carbon_dash'
    _type = 'ProgressStep'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        label: typing.Optional[ComponentType] = None,
        description: typing.Optional[ComponentType] = None,
        secondaryLabel: typing.Optional[ComponentType] = None,
        complete: typing.Optional[bool] = None,
        current: typing.Optional[bool] = None,
        invalid: typing.Optional[bool] = None,
        disabled: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'complete', 'current', 'description', 'disabled', 'invalid', 'label', 'loading_state', 'secondaryLabel', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'complete', 'current', 'description', 'disabled', 'invalid', 'label', 'loading_state', 'secondaryLabel', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(ProgressStep, self).__init__(children=children, **args)

setattr(ProgressStep, "__init__", _explicitize_args(ProgressStep.__init__))
