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


class Tag(Component):
    """A Tag component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional)

- className (string; optional)

- disabled (boolean; default False):
    Whether the tag is disabled.

- filter (boolean; default False):
    Filter/tag variant.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- overflowMenu (a list of or a singular dash component, string or number; optional)

- size (a value equal to: 'sm', 'md'; default 'md'):
    Size.

- type (a value equal to: 'red', 'magenta', 'purple', 'blue', 'cyan', 'teal', 'green', 'gray', 'cool-gray', 'warm-gray', 'high-contrast', 'outline'; default 'gray'):
    Type of tag (determines color)."""
    _children_props: typing.List[str] = ['overflowMenu']
    _base_nodes = ['overflowMenu', 'children']
    _namespace = 'carbon_dash'
    _type = 'Tag'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        type: typing.Optional[Literal["red", "magenta", "purple", "blue", "cyan", "teal", "green", "gray", "cool-gray", "warm-gray", "high-contrast", "outline"]] = None,
        size: typing.Optional[typing.Optional[str]] = None,
        disabled: typing.Optional[bool] = None,
        filter: typing.Optional[bool] = None,
        onClose: typing.Optional[typing.Any] = None,
        overflowMenu: typing.Optional[ComponentType] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'disabled', 'filter', 'loading_state', 'overflowMenu', 'size', 'style', 'type']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'disabled', 'filter', 'loading_state', 'overflowMenu', 'size', 'style', 'type']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Tag, self).__init__(children=children, **args)

setattr(Tag, "__init__", _explicitize_args(Tag.__init__))
