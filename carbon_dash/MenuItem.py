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


class MenuItem(Component):
    """A MenuItem component.
MenuItem is a wrapper for the Carbon MenuItem component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- className (string; default ''):
    className.

- dangerDescription (boolean | number | string | dict | list; optional):
    dangerDescription.

- disabled (boolean | number | string | dict | list; optional):
    disabled.

- kind (boolean | number | string | dict | list; optional):
    kind.

- label (boolean | number | string | dict | list; optional):
    label.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- onClick (boolean | number | string | dict | list; optional):
    onClick.

- renderIcon (boolean | number | string | dict | list; optional):
    renderIcon.

- shortcut (boolean | number | string | dict | list; optional):
    shortcut."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'MenuItem'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        dangerDescription: typing.Optional[typing.Any] = None,
        disabled: typing.Optional[typing.Any] = None,
        kind: typing.Optional[typing.Optional[str]] = None,
        label: typing.Optional[typing.Any] = None,
        onClick: typing.Optional[typing.Any] = None,
        renderIcon: typing.Optional[typing.Any] = None,
        shortcut: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'dangerDescription', 'disabled', 'kind', 'label', 'loading_state', 'onClick', 'renderIcon', 'shortcut', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'dangerDescription', 'disabled', 'kind', 'label', 'loading_state', 'onClick', 'renderIcon', 'shortcut', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(MenuItem, self).__init__(children=children, **args)

setattr(MenuItem, "__init__", _explicitize_args(MenuItem.__init__))
