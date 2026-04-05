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


class IconButton(Component):
    """An IconButton component.
IconButton is a wrapper for the Carbon IconButton component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- align (boolean | number | string | dict | list; optional):
    align.

- autoAlign (boolean | number | string | dict | list; optional):
    autoAlign.

- badgeCount (boolean | number | string | dict | list; optional):
    badgeCount.

- className (string; default ''):
    className.

- closeOnActivation (boolean | number | string | dict | list; optional):
    closeOnActivation.

- defaultOpen (boolean | number | string | dict | list; optional):
    defaultOpen.

- disabled (boolean | number | string | dict | list; optional):
    disabled.

- dropShadow (boolean | number | string | dict | list; optional):
    dropShadow.

- enterDelayMs (boolean | number | string | dict | list; optional):
    enterDelayMs.

- highContrast (boolean | number | string | dict | list; optional):
    highContrast.

- href (boolean | number | string | dict | list; optional):
    href.

- isSelected (boolean | number | string | dict | list; optional):
    isSelected.

- kind (boolean | number | string | dict | list; optional):
    kind.

- label (boolean | number | string | dict | list; optional):
    label.

- leaveDelayMs (boolean | number | string | dict | list; optional):
    leaveDelayMs.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- rel (boolean | number | string | dict | list; optional):
    rel.

- size (boolean | number | string | dict | list; optional):
    size.

- target (boolean | number | string | dict | list; optional):
    target.

- wrapperClasses (boolean | number | string | dict | list; optional):
    wrapperClasses."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'IconButton'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        align: typing.Optional[typing.Any] = None,
        autoAlign: typing.Optional[typing.Any] = None,
        badgeCount: typing.Optional[typing.Any] = None,
        href: typing.Optional[typing.Any] = None,
        closeOnActivation: typing.Optional[typing.Any] = None,
        defaultOpen: typing.Optional[typing.Any] = None,
        dropShadow: typing.Optional[typing.Any] = None,
        disabled: typing.Optional[typing.Any] = None,
        enterDelayMs: typing.Optional[typing.Any] = None,
        isSelected: typing.Optional[typing.Any] = None,
        highContrast: typing.Optional[typing.Any] = None,
        kind: typing.Optional[typing.Optional[str]] = None,
        label: typing.Optional[typing.Any] = None,
        leaveDelayMs: typing.Optional[typing.Any] = None,
        rel: typing.Optional[typing.Any] = None,
        size: typing.Optional[typing.Optional[str]] = None,
        target: typing.Optional[typing.Any] = None,
        wrapperClasses: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'align', 'autoAlign', 'badgeCount', 'className', 'closeOnActivation', 'defaultOpen', 'disabled', 'dropShadow', 'enterDelayMs', 'highContrast', 'href', 'isSelected', 'kind', 'label', 'leaveDelayMs', 'loading_state', 'rel', 'size', 'style', 'target', 'wrapperClasses']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'align', 'autoAlign', 'badgeCount', 'className', 'closeOnActivation', 'defaultOpen', 'disabled', 'dropShadow', 'enterDelayMs', 'highContrast', 'href', 'isSelected', 'kind', 'label', 'leaveDelayMs', 'loading_state', 'rel', 'size', 'style', 'target', 'wrapperClasses']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(IconButton, self).__init__(children=children, **args)

setattr(IconButton, "__init__", _explicitize_args(IconButton.__init__))
