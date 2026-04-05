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


class DismissibleTag(Component):
    """A DismissibleTag component.
DismissibleTag is a wrapper for the Carbon DismissibleTag component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- className (string; default ''):
    className.

- decorator (boolean | number | string | dict | list; optional):
    decorator.

- disabled (boolean | number | string | dict | list; optional):
    disabled.

- dismissTooltipAlignment (boolean | number | string | dict | list; optional):
    dismissTooltipAlignment.

- dismissTooltipLabel (boolean | number | string | dict | list; optional):
    dismissTooltipLabel.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- onClose (boolean | number | string | dict | list; optional):
    onClose.

- renderIcon (boolean | number | string | dict | list; optional):
    renderIcon.

- size (boolean | number | string | dict | list; optional):
    size.

- slug (boolean | number | string | dict | list; optional):
    slug.

- tagTitle (boolean | number | string | dict | list; optional):
    tagTitle.

- text (boolean | number | string | dict | list; optional):
    text.

- title (boolean | number | string | dict | list; optional):
    title.

- type (boolean | number | string | dict | list; optional):
    type."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'DismissibleTag'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        decorator: typing.Optional[typing.Any] = None,
        disabled: typing.Optional[typing.Any] = None,
        dismissTooltipAlignment: typing.Optional[typing.Any] = None,
        dismissTooltipLabel: typing.Optional[typing.Any] = None,
        onClose: typing.Optional[typing.Any] = None,
        renderIcon: typing.Optional[typing.Any] = None,
        size: typing.Optional[typing.Optional[str]] = None,
        slug: typing.Optional[typing.Any] = None,
        text: typing.Optional[typing.Any] = None,
        tagTitle: typing.Optional[typing.Any] = None,
        title: typing.Optional[typing.Any] = None,
        type: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'decorator', 'disabled', 'dismissTooltipAlignment', 'dismissTooltipLabel', 'loading_state', 'onClose', 'renderIcon', 'size', 'slug', 'style', 'tagTitle', 'text', 'title', 'type']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'decorator', 'disabled', 'dismissTooltipAlignment', 'dismissTooltipLabel', 'loading_state', 'onClose', 'renderIcon', 'size', 'slug', 'style', 'tagTitle', 'text', 'title', 'type']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(DismissibleTag, self).__init__(children=children, **args)

setattr(DismissibleTag, "__init__", _explicitize_args(DismissibleTag.__init__))
