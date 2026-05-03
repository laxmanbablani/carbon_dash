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


class Stack(Component):
    """A Stack component.
Stack is a wrapper for the Carbon Stack component.
A layout utility that provides consistent spacing between child elements.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The content of the stack.

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- as (string; default 'div'):
    Provide a custom element type to render as the outermost element.

- className (string; optional):
    Custom CSS class.

- gap (string | number; optional):
    Provide either a custom value or a step from the spacing scale to
    be used as the gap in the layout (1-12).

- loading_state (dict; optional):
    Dash loading state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- orientation (a value equal to: 'horizontal', 'vertical'; default 'vertical'):
    Specify the orientation of items in the Stack."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'Stack'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        gap: typing.Optional[typing.Union[str, NumberType]] = None,
        orientation: typing.Optional[Literal["horizontal", "vertical"]] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'as', 'className', 'gap', 'loading_state', 'orientation', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'as', 'className', 'gap', 'loading_state', 'orientation', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Stack, self).__init__(children=children, **args)

setattr(Stack, "__init__", _explicitize_args(Stack.__init__))
