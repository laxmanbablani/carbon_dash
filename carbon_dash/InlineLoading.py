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


class InlineLoading(Component):
    """An InlineLoading component.
InlineLoading is a wrapper for the Carbon InlineLoading component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- className (string; default ''):
    className.

- description (boolean | number | string | dict | list; optional):
    description.

- iconDescription (boolean | number | string | dict | list; optional):
    iconDescription.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- onSuccess (boolean | number | string | dict | list; optional):
    onSuccess.

- status (boolean | number | string | dict | list; optional):
    status.

- successDelay (boolean | number | string | dict | list; optional):
    successDelay."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'InlineLoading'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[typing.Any] = None,
        iconDescription: typing.Optional[typing.Any] = None,
        onSuccess: typing.Optional[typing.Any] = None,
        status: typing.Optional[typing.Any] = None,
        successDelay: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'description', 'iconDescription', 'loading_state', 'onSuccess', 'status', 'style', 'successDelay']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'description', 'iconDescription', 'loading_state', 'onSuccess', 'status', 'style', 'successDelay']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(InlineLoading, self).__init__(children=children, **args)

setattr(InlineLoading, "__init__", _explicitize_args(InlineLoading.__init__))
