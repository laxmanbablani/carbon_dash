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


class ProgressStep(Component):
    """A ProgressStep component.
ProgressStep is a wrapper for the Carbon ProgressStep component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- className (string; default ''):
    className.

- complete (boolean | number | string | dict | list; optional):
    complete.

- current (boolean | number | string | dict | list; optional):
    current.

- description (string; default 'Step description'):
    description.

- disabled (boolean; default False):
    disabled.

- index (boolean | number | string | dict | list; optional):
    index.

- invalid (boolean | number | string | dict | list; optional):
    invalid.

- label (a list of or a singular dash component, string or number; default 'Step'):
    label.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- onClick (boolean | number | string | dict | list; optional):
    onClick.

- overflowTooltipProps (boolean | number | string | dict | list; optional):
    overflowTooltipProps.

- secondaryLabel (string; default ''):
    secondaryLabel.

- tooltipId (boolean | number | string | dict | list; optional):
    tooltipId.

- translateWithId (boolean | number | string | dict | list; optional):
    translateWithId."""
    _children_props: typing.List[str] = ['label']
    _base_nodes = ['label', 'children']
    _namespace = 'carbon_dash'
    _type = 'ProgressStep'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        complete: typing.Optional[typing.Any] = None,
        current: typing.Optional[typing.Any] = None,
        description: typing.Optional[str] = None,
        disabled: typing.Optional[bool] = None,
        index: typing.Optional[typing.Any] = None,
        invalid: typing.Optional[typing.Any] = None,
        label: typing.Optional[ComponentType] = None,
        onClick: typing.Optional[typing.Any] = None,
        overflowTooltipProps: typing.Optional[typing.Any] = None,
        secondaryLabel: typing.Optional[str] = None,
        tooltipId: typing.Optional[typing.Any] = None,
        translateWithId: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'complete', 'current', 'description', 'disabled', 'index', 'invalid', 'label', 'loading_state', 'onClick', 'overflowTooltipProps', 'secondaryLabel', 'style', 'tooltipId', 'translateWithId']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'complete', 'current', 'description', 'disabled', 'index', 'invalid', 'label', 'loading_state', 'onClick', 'overflowTooltipProps', 'secondaryLabel', 'style', 'tooltipId', 'translateWithId']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(ProgressStep, self).__init__(children=children, **args)

setattr(ProgressStep, "__init__", _explicitize_args(ProgressStep.__init__))
