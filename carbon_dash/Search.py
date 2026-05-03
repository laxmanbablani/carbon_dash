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


class Search(Component):
    """A Search component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional)

- className (string; optional)

- closeButtonLabelText (string; optional):
    Close button label.

- disabled (boolean; default False):
    Whether disabled.

- isExpanded (boolean; default True):
    Whether expanded (small screens).

- labelText (a list of or a singular dash component, string or number; optional):
    Label text.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- persisted_props (list of strings; optional)

- persistence (boolean | string | number; optional)

- persistence_type (a value equal to: 'local', 'session', 'memory'; optional)

- placeholder (string; optional):
    Placeholder text.

- size (a value equal to: 'sm', 'md', 'lg'; default 'md'):
    Size.

- value (string | number; optional):
    Current value of the search input."""
    _children_props: typing.List[str] = ['labelText']
    _base_nodes = ['labelText', 'children']
    _namespace = 'carbon_dash'
    _type = 'Search'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        value: typing.Optional[typing.Union[str, NumberType]] = None,
        labelText: typing.Optional[ComponentType] = None,
        placeholder: typing.Optional[str] = None,
        disabled: typing.Optional[bool] = None,
        size: typing.Optional[typing.Optional[str]] = None,
        closeButtonLabelText: typing.Optional[str] = None,
        isExpanded: typing.Optional[bool] = None,
        persistence: typing.Optional[typing.Union[bool, str, NumberType]] = None,
        persisted_props: typing.Optional[typing.Sequence[str]] = None,
        persistence_type: typing.Optional[Literal["local", "session", "memory"]] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'closeButtonLabelText', 'disabled', 'isExpanded', 'labelText', 'loading_state', 'persisted_props', 'persistence', 'persistence_type', 'placeholder', 'size', 'style', 'value']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'closeButtonLabelText', 'disabled', 'isExpanded', 'labelText', 'loading_state', 'persisted_props', 'persistence', 'persistence_type', 'placeholder', 'size', 'style', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Search, self).__init__(children=children, **args)

setattr(Search, "__init__", _explicitize_args(Search.__init__))
