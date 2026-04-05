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


class DefinitionTooltip(Component):
    """A DefinitionTooltip component.
DefinitionTooltip is a wrapper for the Carbon DefinitionTooltip component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- align (boolean | number | string | dict | list; optional):
    align.

- autoAlign (boolean | number | string | dict | list; optional):
    autoAlign.

- className (string; default ''):
    className.

- defaultOpen (boolean | number | string | dict | list; optional):
    defaultOpen.

- definition (boolean | number | string | dict | list; optional):
    definition.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- openOnHover (boolean | number | string | dict | list; optional):
    openOnHover.

- tooltipText (boolean | number | string | dict | list; optional):
    tooltipText.

- triggerClassName (boolean | number | string | dict | list; optional):
    triggerClassName."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'DefinitionTooltip'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        align: typing.Optional[typing.Any] = None,
        autoAlign: typing.Optional[typing.Any] = None,
        defaultOpen: typing.Optional[typing.Any] = None,
        definition: typing.Optional[typing.Any] = None,
        openOnHover: typing.Optional[typing.Any] = None,
        tooltipText: typing.Optional[typing.Any] = None,
        triggerClassName: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'align', 'autoAlign', 'className', 'defaultOpen', 'definition', 'loading_state', 'openOnHover', 'style', 'tooltipText', 'triggerClassName']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'align', 'autoAlign', 'className', 'defaultOpen', 'definition', 'loading_state', 'openOnHover', 'style', 'tooltipText', 'triggerClassName']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(DefinitionTooltip, self).__init__(children=children, **args)

setattr(DefinitionTooltip, "__init__", _explicitize_args(DefinitionTooltip.__init__))
