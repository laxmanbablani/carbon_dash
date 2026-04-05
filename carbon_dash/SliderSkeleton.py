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


class SliderSkeleton(Component):
    """A SliderSkeleton component.
SliderSkeleton is a wrapper for the Carbon SliderSkeleton component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- ariaLabel (boolean | number | string | dict | list; optional):
    ariaLabel.

- className (string; default ''):
    className.

- hideLabel (boolean | number | string | dict | list; optional):
    hideLabel.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- twoHandles (boolean | number | string | dict | list; optional):
    twoHandles.

- unstable_ariaLabelHandleUpper (boolean | number | string | dict | list; optional):
    unstable_ariaLabelHandleUpper."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'SliderSkeleton'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        ariaLabel: typing.Optional[typing.Any] = None,
        unstable_ariaLabelHandleUpper: typing.Optional[typing.Any] = None,
        hideLabel: typing.Optional[typing.Any] = None,
        twoHandles: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'ariaLabel', 'className', 'hideLabel', 'loading_state', 'style', 'twoHandles', 'unstable_ariaLabelHandleUpper']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'ariaLabel', 'className', 'hideLabel', 'loading_state', 'style', 'twoHandles', 'unstable_ariaLabelHandleUpper']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(SliderSkeleton, self).__init__(children=children, **args)

setattr(SliderSkeleton, "__init__", _explicitize_args(SliderSkeleton.__init__))
