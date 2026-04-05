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


class FeatureFlags(Component):
    """A FeatureFlags component.
FeatureFlags is a wrapper for the Carbon FeatureFlags component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- className (string; default ''):
    className.

- enableDialogElement (boolean | number | string | dict | list; optional):
    enableDialogElement.

- enableEnhancedFileUploader (boolean | number | string | dict | list; optional):
    enableEnhancedFileUploader.

- enableExperimentalFocusWrapWithoutSentinels (boolean | number | string | dict | list; optional):
    enableExperimentalFocusWrapWithoutSentinels.

- enableFocusWrapWithoutSentinels (boolean | number | string | dict | list; optional):
    enableFocusWrapWithoutSentinels.

- enablePresence (boolean | number | string | dict | list; optional):
    enablePresence.

- enableTreeviewControllable (boolean | number | string | dict | list; optional):
    enableTreeviewControllable.

- enableV12DynamicFloatingStyles (boolean | number | string | dict | list; optional):
    enableV12DynamicFloatingStyles.

- enableV12Overflowmenu (boolean | number | string | dict | list; optional):
    enableV12Overflowmenu.

- enableV12TileDefaultIcons (boolean | number | string | dict | list; optional):
    enableV12TileDefaultIcons.

- enableV12TileRadioIcons (boolean | number | string | dict | list; optional):
    enableV12TileRadioIcons.

- flags (boolean | number | string | dict | list; optional):
    flags.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)"""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'FeatureFlags'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        flags: typing.Optional[typing.Any] = None,
        enableV12TileDefaultIcons: typing.Optional[typing.Any] = None,
        enableV12TileRadioIcons: typing.Optional[typing.Any] = None,
        enableV12Overflowmenu: typing.Optional[typing.Any] = None,
        enableTreeviewControllable: typing.Optional[typing.Any] = None,
        enableExperimentalFocusWrapWithoutSentinels: typing.Optional[typing.Any] = None,
        enableFocusWrapWithoutSentinels: typing.Optional[typing.Any] = None,
        enableDialogElement: typing.Optional[typing.Any] = None,
        enableV12DynamicFloatingStyles: typing.Optional[typing.Any] = None,
        enableEnhancedFileUploader: typing.Optional[typing.Any] = None,
        enablePresence: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'enableDialogElement', 'enableEnhancedFileUploader', 'enableExperimentalFocusWrapWithoutSentinels', 'enableFocusWrapWithoutSentinels', 'enablePresence', 'enableTreeviewControllable', 'enableV12DynamicFloatingStyles', 'enableV12Overflowmenu', 'enableV12TileDefaultIcons', 'enableV12TileRadioIcons', 'flags', 'loading_state', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'enableDialogElement', 'enableEnhancedFileUploader', 'enableExperimentalFocusWrapWithoutSentinels', 'enableFocusWrapWithoutSentinels', 'enablePresence', 'enableTreeviewControllable', 'enableV12DynamicFloatingStyles', 'enableV12Overflowmenu', 'enableV12TileDefaultIcons', 'enableV12TileRadioIcons', 'flags', 'loading_state', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FeatureFlags, self).__init__(children=children, **args)

setattr(FeatureFlags, "__init__", _explicitize_args(FeatureFlags.__init__))
