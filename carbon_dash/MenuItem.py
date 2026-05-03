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
MenuItem is a component for rendering menu items within ComboButton or OverflowMenu.

Usage with ComboButton:
<ComboButton label="Primary action">
  <MenuItem label="Second action" />
  <MenuItem label="Third action" />
</ComboButton>

Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- disabled (boolean; default False):
    Specify whether the menu item is disabled.

- kind (a value equal to: 'danger'; optional):
    Specify the kind of menu item.

- label (string; required):
    Specify the label of the menu item."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'MenuItem'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        label: typing.Optional[str] = None,
        kind: typing.Optional[typing.Optional[str]] = None,
        disabled: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'disabled', 'kind', 'label']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'disabled', 'kind', 'label']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['label']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(MenuItem, self).__init__(**args)

setattr(MenuItem, "__init__", _explicitize_args(MenuItem.__init__))
