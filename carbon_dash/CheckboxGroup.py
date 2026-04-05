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


class CheckboxGroup(Component):
    """A CheckboxGroup component.
CheckboxGroup is a wrapper for the Carbon CheckboxGroup component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- className (string; default ''):
    className.

- decorator (boolean | number | string | dict | list; optional):
    decorator.

- helperText (boolean | number | string | dict | list; optional):
    helperText.

- invalid (boolean | number | string | dict | list; optional):
    invalid.

- invalidText (boolean | number | string | dict | list; optional):
    invalidText.

- legendId (boolean | number | string | dict | list; optional):
    legendId.

- legendText (boolean | number | string | dict | list; optional):
    legendText.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- orientation (boolean | number | string | dict | list; optional):
    orientation.

- readOnly (boolean | number | string | dict | list; optional):
    readOnly.

- slug (boolean | number | string | dict | list; optional):
    slug.

- warn (boolean | number | string | dict | list; optional):
    warn.

- warnText (boolean | number | string | dict | list; optional):
    warnText."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'CheckboxGroup'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        decorator: typing.Optional[typing.Any] = None,
        helperText: typing.Optional[typing.Any] = None,
        invalid: typing.Optional[typing.Any] = None,
        invalidText: typing.Optional[typing.Any] = None,
        legendId: typing.Optional[typing.Any] = None,
        orientation: typing.Optional[typing.Any] = None,
        legendText: typing.Optional[typing.Any] = None,
        readOnly: typing.Optional[typing.Any] = None,
        slug: typing.Optional[typing.Any] = None,
        warn: typing.Optional[typing.Any] = None,
        warnText: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'decorator', 'helperText', 'invalid', 'invalidText', 'legendId', 'legendText', 'loading_state', 'orientation', 'readOnly', 'slug', 'style', 'warn', 'warnText']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'decorator', 'helperText', 'invalid', 'invalidText', 'legendId', 'legendText', 'loading_state', 'orientation', 'readOnly', 'slug', 'style', 'warn', 'warnText']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(CheckboxGroup, self).__init__(children=children, **args)

setattr(CheckboxGroup, "__init__", _explicitize_args(CheckboxGroup.__init__))
