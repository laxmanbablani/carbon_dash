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
    children.

- id (string; optional):
    id.

- as_ (boolean | number | string | dict | list; optional):
    as.

- autoAlign (boolean | number | string | dict | list; optional):
    autoAlign.

- className (string; default ''):
    className.

- dangerDescription (boolean | number | string | dict | list; optional):
    dangerDescription.

- disabled (boolean | number | string | dict | list; optional):
    disabled.

- hasIconOnly (boolean | number | string | dict | list; optional):
    hasIconOnly.

- href (boolean | number | string | dict | list; optional):
    href.

- iconDescription (boolean | number | string | dict | list; optional):
    iconDescription.

- isExpressive (boolean | number | string | dict | list; optional):
    isExpressive.

- isSelected (boolean | number | string | dict | list; optional):
    isSelected.

- kind (boolean | number | string | dict | list; optional):
    kind.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- n_clicks (number; default 0):
    n_clicks.

- onBlur (boolean | number | string | dict | list; optional):
    onBlur.

- onClick (boolean | number | string | dict | list; optional):
    onClick.

- onFocus (boolean | number | string | dict | list; optional):
    onFocus.

- onMouseEnter (boolean | number | string | dict | list; optional):
    onMouseEnter.

- onMouseLeave (boolean | number | string | dict | list; optional):
    onMouseLeave.

- persisted_props (list of strings; optional):
    persisted_props.

- persistence (boolean | string | number; optional):
    persistence.

- persistence_type (a value equal to: 'local', 'session', 'memory'; optional):
    persistence_type.

- rel (boolean | number | string | dict | list; optional):
    rel.

- renderIcon (a list of or a singular dash component, string or number; optional):
    renderIcon.

- role (boolean | number | string | dict | list; optional):
    role.

- size (boolean | number | string | dict | list; optional):
    size.

- tabIndex (boolean | number | string | dict | list; optional):
    tabIndex.

- target (boolean | number | string | dict | list; optional):
    target.

- tooltipAlignment (boolean | number | string | dict | list; optional):
    tooltipAlignment.

- tooltipDropShadow (boolean | number | string | dict | list; optional):
    tooltipDropShadow.

- tooltipHighContrast (boolean | number | string | dict | list; optional):
    tooltipHighContrast.

- tooltipPosition (boolean | number | string | dict | list; optional):
    tooltipPosition.

- type (boolean | number | string | dict | list; optional):
    type."""
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
        persistence: typing.Optional[typing.Union[bool, str, NumberType]] = None,
        persisted_props: typing.Optional[typing.Sequence[str]] = None,
        persistence_type: typing.Optional[Literal["local", "session", "memory"]] = None,
        as_: typing.Optional[typing.Any] = None,
        autoAlign: typing.Optional[typing.Any] = None,
        dangerDescription: typing.Optional[typing.Any] = None,
        disabled: typing.Optional[typing.Any] = None,
        hasIconOnly: typing.Optional[typing.Any] = None,
        href: typing.Optional[typing.Any] = None,
        iconDescription: typing.Optional[typing.Any] = None,
        isExpressive: typing.Optional[typing.Any] = None,
        isSelected: typing.Optional[typing.Any] = None,
        kind: typing.Optional[typing.Optional[str]] = None,
        onBlur: typing.Optional[typing.Any] = None,
        onClick: typing.Optional[typing.Any] = None,
        onFocus: typing.Optional[typing.Any] = None,
        onMouseEnter: typing.Optional[typing.Any] = None,
        onMouseLeave: typing.Optional[typing.Any] = None,
        rel: typing.Optional[typing.Any] = None,
        renderIcon: typing.Optional[ComponentType] = None,
        role: typing.Optional[typing.Any] = None,
        size: typing.Optional[typing.Optional[str]] = None,
        tabIndex: typing.Optional[typing.Any] = None,
        target: typing.Optional[typing.Any] = None,
        tooltipAlignment: typing.Optional[typing.Any] = None,
        tooltipDropShadow: typing.Optional[typing.Any] = None,
        tooltipHighContrast: typing.Optional[typing.Any] = None,
        tooltipPosition: typing.Optional[typing.Any] = None,
        type: typing.Optional[typing.Any] = None,
        n_clicks: typing.Optional[NumberType] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'as_', 'autoAlign', 'className', 'dangerDescription', 'disabled', 'hasIconOnly', 'href', 'iconDescription', 'isExpressive', 'isSelected', 'kind', 'loading_state', 'n_clicks', 'onBlur', 'onClick', 'onFocus', 'onMouseEnter', 'onMouseLeave', 'persisted_props', 'persistence', 'persistence_type', 'rel', 'renderIcon', 'role', 'size', 'style', 'tabIndex', 'target', 'tooltipAlignment', 'tooltipDropShadow', 'tooltipHighContrast', 'tooltipPosition', 'type']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'as_', 'autoAlign', 'className', 'dangerDescription', 'disabled', 'hasIconOnly', 'href', 'iconDescription', 'isExpressive', 'isSelected', 'kind', 'loading_state', 'n_clicks', 'onBlur', 'onClick', 'onFocus', 'onMouseEnter', 'onMouseLeave', 'persisted_props', 'persistence', 'persistence_type', 'rel', 'renderIcon', 'role', 'size', 'style', 'tabIndex', 'target', 'tooltipAlignment', 'tooltipDropShadow', 'tooltipHighContrast', 'tooltipPosition', 'type']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Button, self).__init__(children=children, **args)

setattr(Button, "__init__", _explicitize_args(Button.__init__))
