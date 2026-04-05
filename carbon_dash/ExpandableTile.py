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


class ExpandableTile(Component):
    """An ExpandableTile component.
ExpandableTile is a wrapper for the Carbon ExpandableTile component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- className (string; default ''):
    className.

- decorator (boolean | number | string | dict | list; optional):
    decorator.

- expanded (boolean | number | string | dict | list; optional):
    expanded.

- hasRoundedCorners (boolean | number | string | dict | list; optional):
    hasRoundedCorners.

- light (boolean | number | string | dict | list; optional):
    light.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- onClick (boolean | number | string | dict | list; optional):
    onClick.

- onKeyUp (boolean | number | string | dict | list; optional):
    onKeyUp.

- slug (boolean | number | string | dict | list; optional):
    slug.

- tabIndex (boolean | number | string | dict | list; optional):
    tabIndex.

- tileCollapsedIconText (boolean | number | string | dict | list; optional):
    tileCollapsedIconText.

- tileCollapsedLabel (boolean | number | string | dict | list; optional):
    tileCollapsedLabel.

- tileExpandedIconText (boolean | number | string | dict | list; optional):
    tileExpandedIconText.

- tileExpandedLabel (boolean | number | string | dict | list; optional):
    tileExpandedLabel."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'ExpandableTile'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        decorator: typing.Optional[typing.Any] = None,
        expanded: typing.Optional[typing.Any] = None,
        hasRoundedCorners: typing.Optional[typing.Any] = None,
        light: typing.Optional[typing.Any] = None,
        onClick: typing.Optional[typing.Any] = None,
        onKeyUp: typing.Optional[typing.Any] = None,
        slug: typing.Optional[typing.Any] = None,
        tabIndex: typing.Optional[typing.Any] = None,
        tileCollapsedIconText: typing.Optional[typing.Any] = None,
        tileCollapsedLabel: typing.Optional[typing.Any] = None,
        tileExpandedIconText: typing.Optional[typing.Any] = None,
        tileExpandedLabel: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'decorator', 'expanded', 'hasRoundedCorners', 'light', 'loading_state', 'onClick', 'onKeyUp', 'slug', 'style', 'tabIndex', 'tileCollapsedIconText', 'tileCollapsedLabel', 'tileExpandedIconText', 'tileExpandedLabel']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'decorator', 'expanded', 'hasRoundedCorners', 'light', 'loading_state', 'onClick', 'onKeyUp', 'slug', 'style', 'tabIndex', 'tileCollapsedIconText', 'tileCollapsedLabel', 'tileExpandedIconText', 'tileExpandedLabel']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(ExpandableTile, self).__init__(children=children, **args)

setattr(ExpandableTile, "__init__", _explicitize_args(ExpandableTile.__init__))
