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


class SelectableTag(Component):
    """A SelectableTag component.
SelectableTag is a wrapper for the Carbon SelectableTag component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- className (string; default ''):
    className.

- defaultSelected (boolean | number | string | dict | list; optional):
    defaultSelected.

- disabled (boolean | number | string | dict | list; optional):
    disabled.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- onChange (boolean | number | string | dict | list; optional):
    onChange.

- onClick (boolean | number | string | dict | list; optional):
    onClick.

- renderIcon (boolean | number | string | dict | list; optional):
    renderIcon.

- selected (boolean | number | string | dict | list; optional):
    selected.

- size (boolean | number | string | dict | list; optional):
    size.

- text (boolean | number | string | dict | list; optional):
    text."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'SelectableTag'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        disabled: typing.Optional[typing.Any] = None,
        renderIcon: typing.Optional[typing.Any] = None,
        onChange: typing.Optional[typing.Any] = None,
        onClick: typing.Optional[typing.Any] = None,
        selected: typing.Optional[typing.Any] = None,
        defaultSelected: typing.Optional[typing.Any] = None,
        size: typing.Optional[typing.Optional[str]] = None,
        text: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'defaultSelected', 'disabled', 'loading_state', 'onChange', 'onClick', 'renderIcon', 'selected', 'size', 'style', 'text']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'defaultSelected', 'disabled', 'loading_state', 'onChange', 'onClick', 'renderIcon', 'selected', 'size', 'style', 'text']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(SelectableTag, self).__init__(children=children, **args)

setattr(SelectableTag, "__init__", _explicitize_args(SelectableTag.__init__))
