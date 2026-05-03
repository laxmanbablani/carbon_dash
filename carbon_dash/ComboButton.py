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


class ComboButton(Component):
    """A ComboButton component.
ComboButton is a button with a menu attached for additional actions.
It renders a primary button with a dropdown menu of secondary actions.

Children should be Carbon MenuItem components (e.g., cd.MenuItem(label="Action")).
These can be created using carbon_dash.MenuItem in Python.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The content of the ComboButton (MenuItem components).

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- className (string; optional):
    Custom CSS class.

- disabled (boolean; default False):
    Specify whether the ComboButton should be disabled.

- kind (a value equal to: 'primary', 'secondary', 'tertiary', 'ghost', 'danger'; default 'primary'):
    Specify the kind of button.

- label (string; required):
    The label text for the primary button.

- loading_state (dict; optional):
    Dash loading state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- menuAlignment (a value equal to: 'top', 'top-start', 'top-end', 'bottom', 'bottom-start', 'bottom-end'; default 'bottom'):
    Specify the alignment of the menu relative to the button.

- n_clicks (number; default 0):
    Number of times the button has been clicked.

- size (a value equal to: 'sm', 'md', 'lg', 'xl'; optional):
    Specify the size of the button.

- tooltipAlignment (a value equal to: 'start', 'center', 'end'; optional):
    Specify the alignment of the tooltip."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'ComboButton'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        label: typing.Optional[str] = None,
        menuAlignment: typing.Optional[Literal["top", "top-start", "top-end", "bottom", "bottom-start", "bottom-end"]] = None,
        tooltipAlignment: typing.Optional[Literal["start", "center", "end"]] = None,
        size: typing.Optional[typing.Optional[str]] = None,
        kind: typing.Optional[typing.Optional[str]] = None,
        disabled: typing.Optional[bool] = None,
        n_clicks: typing.Optional[NumberType] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'disabled', 'kind', 'label', 'loading_state', 'menuAlignment', 'n_clicks', 'size', 'style', 'tooltipAlignment']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'disabled', 'kind', 'label', 'loading_state', 'menuAlignment', 'n_clicks', 'size', 'style', 'tooltipAlignment']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['label']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(ComboButton, self).__init__(children=children, **args)

setattr(ComboButton, "__init__", _explicitize_args(ComboButton.__init__))
