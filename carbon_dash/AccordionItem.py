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


class AccordionItem(Component):
    """An AccordionItem component.
AccordionItem is a wrapper for the Carbon AccordionItem component.
Represents a single collapsible section within an Accordion.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The content of the accordion item.

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- className (string; optional):
    Custom CSS class.

- disabled (boolean; optional):
    Specify whether an individual AccordionItem should be disabled.

- loading_state (dict; optional):
    Dash loading state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- open (boolean; default False):
    Whether the accordion item is open.

- title (a list of or a singular dash component, string or number; default 'title'):
    The accordion title."""
    _children_props: typing.List[str] = ['title']
    _base_nodes = ['title', 'children']
    _namespace = 'carbon_dash'
    _type = 'AccordionItem'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        title: typing.Optional[ComponentType] = None,
        open: typing.Optional[bool] = None,
        disabled: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'disabled', 'loading_state', 'open', 'style', 'title']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'disabled', 'loading_state', 'open', 'style', 'title']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(AccordionItem, self).__init__(children=children, **args)

setattr(AccordionItem, "__init__", _explicitize_args(AccordionItem.__init__))
