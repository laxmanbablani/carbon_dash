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


class Button(Component):
    """A Button component.
Button is a wrapper for the Carbon Button component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The content of the button.

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- aiLabel (boolean; default False):
    Whether to render the AI label decorator.

- className (string; optional):
    Specify a custom className to be applied to the component.

- dangerDescription (string; optional):
    Description for the danger variant (screen readers).

- disabled (boolean; default False):
    Whether the button is disabled.

- hasIconOnly (boolean; default False):
    Whether the button should only render an icon.

- href (string; optional):
    If provided, renders as a link.

- iconDescription (string; optional):
    Icon description for screen readers.

- isExpressive (boolean; default False):
    Enable expressive styling.

- isSelected (boolean; default False):
    Whether the button is in a selected state.

- kind (a value equal to: 'primary', 'secondary', 'tertiary', 'ghost', 'danger'; default 'primary'):
    Specify the kind of button. Default: 'primary'.

- loading_state (dict; optional):
    Dash loading state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- n_clicks (number; default 0):
    An integer that represents the number of times that this element
    has been clicked.

- n_clicks_timestamp (number; optional):
    Timestamp of the last click in milliseconds since epoch.

- persisted_props (list of strings; optional):
    Properties whose user interactions will persist.

- persistence (boolean | string | number; optional):
    Used to allow user interactions in this component to be persisted.

- persistence_type (a value equal to: 'local', 'session', 'memory'; optional):
    Where persisted user changes will be stored.

- renderIcon (a list of or a singular dash component, string or number; optional):
    An icon component to render in the button. Accepts DashIconify,
    html.Div, Carbon icon name string, or any React node.

- size (a value equal to: 'sm', 'md', 'lg', 'xl', '2xl'; default 'lg'):
    Specify the size of the button. Default: 'lg'.

- tooltipAlignment (a value equal to: 'start', 'center', 'end'; optional):
    Tooltip alignment.

- tooltipPosition (a value equal to: 'top', 'bottom', 'left', 'right'; optional):
    Tooltip position."""
    _children_props: typing.List[str] = ['renderIcon']
    _base_nodes = ['renderIcon', 'children']
    _namespace = 'carbon_dash'
    _type = 'Button'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        n_clicks: typing.Optional[NumberType] = None,
        n_clicks_timestamp: typing.Optional[NumberType] = None,
        kind: typing.Optional[typing.Optional[str]] = None,
        size: typing.Optional[typing.Optional[str]] = None,
        disabled: typing.Optional[bool] = None,
        isExpressive: typing.Optional[bool] = None,
        isSelected: typing.Optional[bool] = None,
        hasIconOnly: typing.Optional[bool] = None,
        dangerDescription: typing.Optional[str] = None,
        iconDescription: typing.Optional[str] = None,
        href: typing.Optional[str] = None,
        renderIcon: typing.Optional[ComponentType] = None,
        tooltipAlignment: typing.Optional[Literal["start", "center", "end"]] = None,
        tooltipPosition: typing.Optional[Literal["top", "bottom", "left", "right"]] = None,
        aiLabel: typing.Optional[bool] = None,
        persistence: typing.Optional[typing.Union[bool, str, NumberType]] = None,
        persisted_props: typing.Optional[typing.Sequence[str]] = None,
        persistence_type: typing.Optional[Literal["local", "session", "memory"]] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'aiLabel', 'className', 'dangerDescription', 'disabled', 'hasIconOnly', 'href', 'iconDescription', 'isExpressive', 'isSelected', 'kind', 'loading_state', 'n_clicks', 'n_clicks_timestamp', 'persisted_props', 'persistence', 'persistence_type', 'renderIcon', 'size', 'style', 'tooltipAlignment', 'tooltipPosition']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'aiLabel', 'className', 'dangerDescription', 'disabled', 'hasIconOnly', 'href', 'iconDescription', 'isExpressive', 'isSelected', 'kind', 'loading_state', 'n_clicks', 'n_clicks_timestamp', 'persisted_props', 'persistence', 'persistence_type', 'renderIcon', 'size', 'style', 'tooltipAlignment', 'tooltipPosition']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Button, self).__init__(children=children, **args)

setattr(Button, "__init__", _explicitize_args(Button.__init__))
