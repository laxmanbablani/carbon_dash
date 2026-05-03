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


class AspectRatio(Component):
    """An AspectRatio component.
AspectRatio is a wrapper for the Carbon AspectRatio component.
Maintains a specific width:height ratio for its content.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The content of the aspect ratio container.

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- className (string; optional):
    Custom CSS class.

- loading_state (dict; optional):
    Dash loading state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- ratio (a value equal to: '1x1', '2x3', '3x2', '3x4', '4x3', '1x2', '2x1', '9x16', '16x9'; default '1x1'):
    Specify the aspect ratio (width:height) to maintain."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'AspectRatio'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        ratio: typing.Optional[Literal["1x1", "2x3", "3x2", "3x4", "4x3", "1x2", "2x1", "9x16", "16x9"]] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'loading_state', 'ratio', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'loading_state', 'ratio', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(AspectRatio, self).__init__(children=children, **args)

setattr(AspectRatio, "__init__", _explicitize_args(AspectRatio.__init__))
