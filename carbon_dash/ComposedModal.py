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


class ComposedModal(Component):
    """A ComposedModal component.
ComposedModal is a wrapper for the Carbon ComposedModal component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- className (string; default ''):
    className.

- containerClassName (boolean | number | string | dict | list; optional):
    containerClassName.

- current (boolean | number | string | dict | list; optional):
    current.

- danger (boolean | number | string | dict | list; optional):
    danger.

- decorator (boolean | number | string | dict | list; optional):
    decorator.

- isFullWidth (boolean | number | string | dict | list; optional):
    isFullWidth.

- launcherButtonRef (boolean | number | string | dict | list; optional):
    launcherButtonRef.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- onClose (boolean | number | string | dict | list; optional):
    onClose.

- onKeyDown (boolean | number | string | dict | list; optional):
    onKeyDown.

- open (boolean | number | string | dict | list; optional):
    open.

- preventCloseOnClickOutside (boolean | number | string | dict | list; optional):
    preventCloseOnClickOutside.

- selectorPrimaryFocus (boolean | number | string | dict | list; optional):
    selectorPrimaryFocus.

- selectorsFloatingMenus (boolean | number | string | dict | list; optional):
    selectorsFloatingMenus.

- size (boolean | number | string | dict | list; optional):
    size.

- slug (boolean | number | string | dict | list; optional):
    slug."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'ComposedModal'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        containerClassName: typing.Optional[typing.Any] = None,
        danger: typing.Optional[typing.Any] = None,
        decorator: typing.Optional[typing.Any] = None,
        isFullWidth: typing.Optional[typing.Any] = None,
        launcherButtonRef: typing.Optional[typing.Any] = None,
        current: typing.Optional[typing.Any] = None,
        onClose: typing.Optional[typing.Any] = None,
        onKeyDown: typing.Optional[typing.Any] = None,
        open: typing.Optional[typing.Any] = None,
        preventCloseOnClickOutside: typing.Optional[typing.Any] = None,
        selectorPrimaryFocus: typing.Optional[typing.Any] = None,
        selectorsFloatingMenus: typing.Optional[typing.Any] = None,
        size: typing.Optional[typing.Optional[str]] = None,
        slug: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'containerClassName', 'current', 'danger', 'decorator', 'isFullWidth', 'launcherButtonRef', 'loading_state', 'onClose', 'onKeyDown', 'open', 'preventCloseOnClickOutside', 'selectorPrimaryFocus', 'selectorsFloatingMenus', 'size', 'slug', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'containerClassName', 'current', 'danger', 'decorator', 'isFullWidth', 'launcherButtonRef', 'loading_state', 'onClose', 'onKeyDown', 'open', 'preventCloseOnClickOutside', 'selectorPrimaryFocus', 'selectorsFloatingMenus', 'size', 'slug', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(ComposedModal, self).__init__(children=children, **args)

setattr(ComposedModal, "__init__", _explicitize_args(ComposedModal.__init__))
