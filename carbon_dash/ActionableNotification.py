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


class ActionableNotification(Component):
    """An ActionableNotification component.
ActionableNotification is a wrapper for the Carbon ActionableNotification component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- actionButtonLabel (boolean | number | string | dict | list; optional):
    actionButtonLabel.

- ariaLabel (boolean | number | string | dict | list; optional):
    ariaLabel.

- caption (boolean | number | string | dict | list; optional):
    caption.

- className (string; default ''):
    className.

- closeOnEscape (boolean | number | string | dict | list; optional):
    closeOnEscape.

- hasFocus (boolean | number | string | dict | list; optional):
    hasFocus.

- hideCloseButton (boolean | number | string | dict | list; optional):
    hideCloseButton.

- inline (boolean | number | string | dict | list; optional):
    inline.

- kind (boolean | number | string | dict | list; optional):
    kind.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- lowContrast (boolean | number | string | dict | list; optional):
    lowContrast.

- onActionButtonClick (boolean | number | string | dict | list; optional):
    onActionButtonClick.

- onClose (boolean | number | string | dict | list; optional):
    onClose.

- onCloseButtonClick (boolean | number | string | dict | list; optional):
    onCloseButtonClick.

- role (boolean | number | string | dict | list; optional):
    role.

- statusIconDescription (boolean | number | string | dict | list; optional):
    statusIconDescription.

- subtitle (boolean | number | string | dict | list; optional):
    subtitle.

- title (boolean | number | string | dict | list; optional):
    title."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'ActionableNotification'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        actionButtonLabel: typing.Optional[typing.Any] = None,
        ariaLabel: typing.Optional[typing.Any] = None,
        caption: typing.Optional[typing.Any] = None,
        closeOnEscape: typing.Optional[typing.Any] = None,
        hasFocus: typing.Optional[typing.Any] = None,
        hideCloseButton: typing.Optional[typing.Any] = None,
        inline: typing.Optional[typing.Any] = None,
        kind: typing.Optional[typing.Optional[str]] = None,
        lowContrast: typing.Optional[typing.Any] = None,
        onActionButtonClick: typing.Optional[typing.Any] = None,
        onClose: typing.Optional[typing.Any] = None,
        onCloseButtonClick: typing.Optional[typing.Any] = None,
        role: typing.Optional[typing.Any] = None,
        statusIconDescription: typing.Optional[typing.Any] = None,
        subtitle: typing.Optional[typing.Any] = None,
        title: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'actionButtonLabel', 'ariaLabel', 'caption', 'className', 'closeOnEscape', 'hasFocus', 'hideCloseButton', 'inline', 'kind', 'loading_state', 'lowContrast', 'onActionButtonClick', 'onClose', 'onCloseButtonClick', 'role', 'statusIconDescription', 'style', 'subtitle', 'title']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'actionButtonLabel', 'ariaLabel', 'caption', 'className', 'closeOnEscape', 'hasFocus', 'hideCloseButton', 'inline', 'kind', 'loading_state', 'lowContrast', 'onActionButtonClick', 'onClose', 'onCloseButtonClick', 'role', 'statusIconDescription', 'style', 'subtitle', 'title']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(ActionableNotification, self).__init__(children=children, **args)

setattr(ActionableNotification, "__init__", _explicitize_args(ActionableNotification.__init__))
