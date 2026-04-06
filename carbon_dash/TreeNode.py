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


class TreeNode(Component):
    """A TreeNode component.
TreeNode is a wrapper for the Carbon TreeNode component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- active (boolean | number | string | dict | list; optional):
    active.

- align (boolean | number | string | dict | list; optional):
    align.

- autoAlign (boolean | number | string | dict | list; optional):
    autoAlign.

- className (string; default ''):
    className.

- debounce (boolean | number; optional):
    debounce.

- defaultIsExpanded (boolean | number | string | dict | list; optional):
    defaultIsExpanded.

- depth (boolean | number | string | dict | list; optional):
    depth.

- disabled (boolean | number | string | dict | list; optional):
    disabled.

- href (boolean | number | string | dict | list; optional):
    href.

- isExpanded (boolean | number | string | dict | list; optional):
    isExpanded.

- label (boolean | number | string | dict | list; optional):
    label.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- n_blur (number; optional):
    n_blur.

- n_submit (number; optional):
    n_submit.

- onNodeFocusEvent (boolean | number | string | dict | list; optional):
    onNodeFocusEvent.

- onSelect (boolean | number | string | dict | list; optional):
    onSelect.

- onToggle (boolean | number | string | dict | list; optional):
    onToggle.

- onTreeSelect (boolean | number | string | dict | list; optional):
    onTreeSelect.

- persisted_props (list of strings; optional):
    persisted_props.

- persistence (boolean | string | number; optional):
    persistence.

- persistence_type (a value equal to: 'local', 'session', 'memory'; optional):
    persistence_type.

- renderIcon (a list of or a singular dash component, string or number; optional):
    renderIcon.

- selected (boolean | number | string | dict | list; optional):
    selected.

- value (boolean | number | string | dict | list; default ''):
    value."""
    _children_props: typing.List[str] = ['renderIcon']
    _base_nodes = ['renderIcon', 'children']
    _namespace = 'carbon_dash'
    _type = 'TreeNode'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        persistence: typing.Optional[typing.Union[bool, str, NumberType]] = None,
        persisted_props: typing.Optional[typing.Sequence[str]] = None,
        persistence_type: typing.Optional[Literal["local", "session", "memory"]] = None,
        n_blur: typing.Optional[NumberType] = None,
        n_submit: typing.Optional[NumberType] = None,
        debounce: typing.Optional[typing.Union[bool, NumberType]] = None,
        active: typing.Optional[typing.Any] = None,
        defaultIsExpanded: typing.Optional[typing.Any] = None,
        depth: typing.Optional[typing.Any] = None,
        disabled: typing.Optional[typing.Any] = None,
        isExpanded: typing.Optional[typing.Any] = None,
        label: typing.Optional[typing.Any] = None,
        onNodeFocusEvent: typing.Optional[typing.Any] = None,
        onSelect: typing.Optional[typing.Any] = None,
        onToggle: typing.Optional[typing.Any] = None,
        onTreeSelect: typing.Optional[typing.Any] = None,
        renderIcon: typing.Optional[ComponentType] = None,
        selected: typing.Optional[typing.Any] = None,
        value: typing.Optional[typing.Any] = None,
        href: typing.Optional[typing.Any] = None,
        align: typing.Optional[typing.Any] = None,
        autoAlign: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'active', 'align', 'autoAlign', 'className', 'debounce', 'defaultIsExpanded', 'depth', 'disabled', 'href', 'isExpanded', 'label', 'loading_state', 'n_blur', 'n_submit', 'onNodeFocusEvent', 'onSelect', 'onToggle', 'onTreeSelect', 'persisted_props', 'persistence', 'persistence_type', 'renderIcon', 'selected', 'style', 'value']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'active', 'align', 'autoAlign', 'className', 'debounce', 'defaultIsExpanded', 'depth', 'disabled', 'href', 'isExpanded', 'label', 'loading_state', 'n_blur', 'n_submit', 'onNodeFocusEvent', 'onSelect', 'onToggle', 'onTreeSelect', 'persisted_props', 'persistence', 'persistence_type', 'renderIcon', 'selected', 'style', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(TreeNode, self).__init__(children=children, **args)

setattr(TreeNode, "__init__", _explicitize_args(TreeNode.__init__))
