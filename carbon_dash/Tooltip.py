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
Tooltip is a wrapper for the Carbon Tooltip component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- align (string; default 'top'):
    align.

- className (string; default ''):
    className.

- closeOnActivation (boolean | number | string | dict | list; optional):
    closeOnActivation.

- defaultOpen (boolean; default False):
    defaultOpen.

- description (string; default 'Tooltip Content'):
    description.

- dropShadow (boolean | number | string | dict | list; optional):
    dropShadow.

- enterDelayMs (boolean | number | string | dict | list; optional):
    enterDelayMs.

- highContrast (boolean | number | string | dict | list; optional):
    highContrast.

- label (boolean | number | string | dict | list; optional):
    label.

- leaveDelayMs (boolean | number | string | dict | list; optional):
    leaveDelayMs.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)"""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'Tooltip'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        align: typing.Optional[str] = None,
        closeOnActivation: typing.Optional[typing.Any] = None,
        defaultOpen: typing.Optional[bool] = None,
        description: typing.Optional[str] = None,
        dropShadow: typing.Optional[typing.Any] = None,
        enterDelayMs: typing.Optional[typing.Any] = None,
        highContrast: typing.Optional[typing.Any] = None,
        label: typing.Optional[typing.Any] = None,
        leaveDelayMs: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'align', 'className', 'closeOnActivation', 'defaultOpen', 'description', 'dropShadow', 'enterDelayMs', 'highContrast', 'label', 'leaveDelayMs', 'loading_state', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'align', 'className', 'closeOnActivation', 'defaultOpen', 'description', 'dropShadow', 'enterDelayMs', 'highContrast', 'label', 'leaveDelayMs', 'loading_state', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Tooltip, self).__init__(children=children, **args)

setattr(Tooltip, "__init__", _explicitize_args(Tooltip.__init__))
