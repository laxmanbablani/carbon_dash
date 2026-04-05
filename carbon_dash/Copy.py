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


class Copy(Component):
    """A Copy component.
Copy is a wrapper for the Carbon Copy component.

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

- feedback (boolean | number | string | dict | list; optional):
    feedback.

- feedbackTimeout (boolean | number | string | dict | list; optional):
    feedbackTimeout.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- onAnimationEnd (boolean | number | string | dict | list; optional):
    onAnimationEnd.

- onClick (boolean | number | string | dict | list; optional):
    onClick."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'Copy'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        align: typing.Optional[typing.Any] = None,
        autoAlign: typing.Optional[typing.Any] = None,
        feedback: typing.Optional[typing.Any] = None,
        feedbackTimeout: typing.Optional[typing.Any] = None,
        onAnimationEnd: typing.Optional[typing.Any] = None,
        onClick: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'align', 'autoAlign', 'className', 'feedback', 'feedbackTimeout', 'loading_state', 'onAnimationEnd', 'onClick', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'align', 'autoAlign', 'className', 'feedback', 'feedbackTimeout', 'loading_state', 'onAnimationEnd', 'onClick', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Copy, self).__init__(children=children, **args)

setattr(Copy, "__init__", _explicitize_args(Copy.__init__))
