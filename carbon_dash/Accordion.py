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


class Accordion(Component):
    """An Accordion component.
Accordion is a wrapper for the Carbon Accordion component.
Used for organizing content in collapsible panels.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The content of the accordion (AccordionItem children).

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- align (a value equal to: 'start', 'end'; default 'end'):
    Specify the alignment of the accordion heading title and chevron.

- className (string; optional):
    Custom CSS class.

- disabled (boolean; default False):
    Specify whether an individual AccordionItem should be disabled.

- isFlush (boolean; default False):
    Specify whether Accordion text should be flush, does not work with
    align=\"start\".

- loading_state (dict; optional):
    Dash loading state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- ordered (boolean; default False):
    Specify if the Accordion should be an ordered list.

- size (a value equal to: 'sm', 'md', 'lg'; optional):
    Specify the size of the Accordion."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'Accordion'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        align: typing.Optional[Literal["start", "end"]] = None,
        disabled: typing.Optional[bool] = None,
        isFlush: typing.Optional[bool] = None,
        ordered: typing.Optional[bool] = None,
        size: typing.Optional[typing.Optional[str]] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'align', 'className', 'disabled', 'isFlush', 'loading_state', 'ordered', 'size', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'align', 'className', 'disabled', 'isFlush', 'loading_state', 'ordered', 'size', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Accordion, self).__init__(children=children, **args)

setattr(Accordion, "__init__", _explicitize_args(Accordion.__init__))
