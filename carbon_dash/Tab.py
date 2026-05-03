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


class Tab(Component):
    """A Tab component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The content of the tab.

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- className (string; optional):
    Custom CSS class.

- closeButtonLabel (string; optional):
    Optional dismissible button label.

- disabled (boolean; default False):
    Whether the tab is disabled.

- dismissable (boolean; optional):
    Whether the tab is dismissable.

- href (string; optional):
    Provide an href for the tab, making it an <a> element.

- label (a list of or a singular dash component, string or number; optional):
    The label text for the tab.

- loading_state (dict; optional):
    Dash loading state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- selected (boolean; optional):
    Whether the tab is selected. Overrides the parent's selectedIndex."""
    _children_props: typing.List[str] = ['label']
    _base_nodes = ['label', 'children']
    _namespace = 'carbon_dash'
    _type = 'Tab'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        label: typing.Optional[ComponentType] = None,
        disabled: typing.Optional[bool] = None,
        selected: typing.Optional[bool] = None,
        href: typing.Optional[str] = None,
        closeButtonLabel: typing.Optional[str] = None,
        dismissable: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'closeButtonLabel', 'disabled', 'dismissable', 'href', 'label', 'loading_state', 'selected', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'closeButtonLabel', 'disabled', 'dismissable', 'href', 'label', 'loading_state', 'selected', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Tab, self).__init__(children=children, **args)

setattr(Tab, "__init__", _explicitize_args(Tab.__init__))
