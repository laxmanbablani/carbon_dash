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


class Loading(Component):
    """A Loading component.
Loading is a wrapper for the Carbon Loading component.
Displays a loading indicator for async operations.

Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- active (boolean; default True):
    Specify whether the loading indicator should be spinning or not.

- className (string; optional):
    Custom CSS class.

- description (string; default 'loading'):
    Specify a description for the loading state.

- loading_state (dict; optional):
    Dash loading state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- small (boolean; default False):
    Specify whether you would like the small variant of Loading.

- withOverlay (boolean; default True):
    Specify whether you want the loader to be applied with an overlay."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'Loading'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        active: typing.Optional[bool] = None,
        small: typing.Optional[bool] = None,
        withOverlay: typing.Optional[bool] = None,
        description: typing.Optional[str] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'active', 'className', 'description', 'loading_state', 'small', 'style', 'withOverlay']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'active', 'className', 'description', 'loading_state', 'small', 'style', 'withOverlay']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(Loading, self).__init__(**args)

setattr(Loading, "__init__", _explicitize_args(Loading.__init__))
