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


class ContentSwitcher(Component):
    """A ContentSwitcher component.
ContentSwitcher is a wrapper for the Carbon ContentSwitcher component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- className (string; default ''):
    className.

- light (boolean | number | string | dict | list; optional):
    light.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- lowContrast (boolean | number | string | dict | list; optional):
    lowContrast.

- onChange (boolean | number | string | dict | list; optional):
    onChange.

- selectedIndex (boolean | number | string | dict | list; optional):
    selectedIndex.

- selectionMode (boolean | number | string | dict | list; optional):
    selectionMode.

- size (boolean | number | string | dict | list; optional):
    size."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'ContentSwitcher'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        light: typing.Optional[typing.Any] = None,
        lowContrast: typing.Optional[typing.Any] = None,
        onChange: typing.Optional[typing.Any] = None,
        selectedIndex: typing.Optional[typing.Any] = None,
        selectionMode: typing.Optional[typing.Any] = None,
        size: typing.Optional[typing.Optional[str]] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'light', 'loading_state', 'lowContrast', 'onChange', 'selectedIndex', 'selectionMode', 'size', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'light', 'loading_state', 'lowContrast', 'onChange', 'selectedIndex', 'selectionMode', 'size', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(ContentSwitcher, self).__init__(children=children, **args)

setattr(ContentSwitcher, "__init__", _explicitize_args(ContentSwitcher.__init__))
