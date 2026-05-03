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


class Tooltip(Component):
    """A Tooltip component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional)

- align (a value equal to: 'top', 'bottom', 'left', 'right', 'top-left', 'top-right', 'bottom-left', 'bottom-right'; default 'top'):
    Alignment relative to trigger.

- autoAlign (boolean; optional):
    Auto-align to viewport.

- className (string; optional)

- closeOnActivation (boolean; default False):
    Whether to close on activation.

- defaultOpen (boolean; default False):
    Whether open by default.

- description (a list of or a singular dash component, string or number; optional):
    Tooltip description/content.

- dropShadow (boolean; default False):
    Whether to show a drop shadow.

- enterDelayMs (number; default 100):
    Delay before showing (ms).

- highContrast (boolean; default False):
    High contrast variant.

- label (a list of or a singular dash component, string or number; optional):
    Tooltip trigger label.

- leaveDelayMs (number; default 300):
    Delay before hiding (ms).

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)"""
    _children_props: typing.List[str] = ['label', 'description']
    _base_nodes = ['label', 'description', 'children']
    _namespace = 'carbon_dash'
    _type = 'Tooltip'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        label: typing.Optional[ComponentType] = None,
        description: typing.Optional[ComponentType] = None,
        align: typing.Optional[Literal["top", "bottom", "left", "right", "top-left", "top-right", "bottom-left", "bottom-right"]] = None,
        defaultOpen: typing.Optional[bool] = None,
        closeOnActivation: typing.Optional[bool] = None,
        enterDelayMs: typing.Optional[NumberType] = None,
        leaveDelayMs: typing.Optional[NumberType] = None,
        dropShadow: typing.Optional[bool] = None,
        highContrast: typing.Optional[bool] = None,
        autoAlign: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'align', 'autoAlign', 'className', 'closeOnActivation', 'defaultOpen', 'description', 'dropShadow', 'enterDelayMs', 'highContrast', 'label', 'leaveDelayMs', 'loading_state', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'align', 'autoAlign', 'className', 'closeOnActivation', 'defaultOpen', 'description', 'dropShadow', 'enterDelayMs', 'highContrast', 'label', 'leaveDelayMs', 'loading_state', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Tooltip, self).__init__(children=children, **args)

setattr(Tooltip, "__init__", _explicitize_args(Tooltip.__init__))
