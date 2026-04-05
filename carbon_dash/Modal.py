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


class Modal(Component):
    """A Modal component.
Modal is a wrapper for the Carbon Modal component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- alert (boolean | number | string | dict | list; optional):
    alert.

- className (string; default ''):
    className.

- closeButtonLabel (boolean | number | string | dict | list; optional):
    closeButtonLabel.

- current (boolean | number | string | dict | list; optional):
    current.

- danger (boolean | number | string | dict | list; optional):
    danger.

- decorator (boolean | number | string | dict | list; optional):
    decorator.

- hasScrollingContent (boolean | number | string | dict | list; optional):
    hasScrollingContent.

- isFullWidth (boolean | number | string | dict | list; optional):
    isFullWidth.

- launcherButtonRef (boolean | number | string | dict | list; optional):
    launcherButtonRef.

- loadingDescription (boolean | number | string | dict | list; optional):
    loadingDescription.

- loadingIconDescription (boolean | number | string | dict | list; optional):
    loadingIconDescription.

- loadingStatus (boolean | number | string | dict | list; optional):
    loadingStatus.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- modalAriaLabel (boolean | number | string | dict | list; optional):
    modalAriaLabel.

- modalHeading (string; default 'Modal Heading'):
    modalHeading.

- modalLabel (boolean | number | string | dict | list; optional):
    modalLabel.

- onKeyDown (boolean | number | string | dict | list; optional):
    onKeyDown.

- onLoadingSuccess (boolean | number | string | dict | list; optional):
    onLoadingSuccess.

- onRequestClose (boolean | number | string | dict | list; optional):
    onRequestClose.

- onRequestSubmit (boolean | number | string | dict | list; optional):
    onRequestSubmit.

- onSecondarySubmit (boolean | number | string | dict | list; optional):
    onSecondarySubmit.

- open (boolean; default False):
    open.

- passiveModal (boolean | number | string | dict | list; optional):
    passiveModal.

- persisted_props (list of strings; optional):
    persisted_props.

- persistence (boolean | string | number; optional):
    persistence.

- persistence_type (a value equal to: 'local', 'session', 'memory'; optional):
    persistence_type.

- preventCloseOnClickOutside (boolean | number | string | dict | list; optional):
    preventCloseOnClickOutside.

- primaryButtonDisabled (boolean | number | string | dict | list; optional):
    primaryButtonDisabled.

- primaryButtonText (string; default 'Primary Button'):
    primaryButtonText.

- secondaryButtonText (string; default 'Secondary Button'):
    secondaryButtonText.

- secondaryButtons (boolean | number | string | dict | list; optional):
    secondaryButtons.

- selectorPrimaryFocus (boolean | number | string | dict | list; optional):
    selectorPrimaryFocus.

- selectorsFloatingMenus (boolean | number | string | dict | list; optional):
    selectorsFloatingMenus.

- shouldSubmitOnEnter (boolean | number | string | dict | list; optional):
    shouldSubmitOnEnter.

- size (boolean | number | string | dict | list; optional):
    size.

- slug (boolean | number | string | dict | list; optional):
    slug."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'Modal'


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
        alert: typing.Optional[typing.Any] = None,
        closeButtonLabel: typing.Optional[typing.Any] = None,
        danger: typing.Optional[typing.Any] = None,
        decorator: typing.Optional[typing.Any] = None,
        hasScrollingContent: typing.Optional[typing.Any] = None,
        isFullWidth: typing.Optional[typing.Any] = None,
        launcherButtonRef: typing.Optional[typing.Any] = None,
        current: typing.Optional[typing.Any] = None,
        loadingDescription: typing.Optional[typing.Any] = None,
        loadingIconDescription: typing.Optional[typing.Any] = None,
        loadingStatus: typing.Optional[typing.Any] = None,
        modalAriaLabel: typing.Optional[typing.Any] = None,
        modalHeading: typing.Optional[str] = None,
        modalLabel: typing.Optional[typing.Any] = None,
        onKeyDown: typing.Optional[typing.Any] = None,
        onLoadingSuccess: typing.Optional[typing.Any] = None,
        onRequestClose: typing.Optional[typing.Any] = None,
        onRequestSubmit: typing.Optional[typing.Any] = None,
        onSecondarySubmit: typing.Optional[typing.Any] = None,
        open: typing.Optional[bool] = None,
        passiveModal: typing.Optional[typing.Any] = None,
        preventCloseOnClickOutside: typing.Optional[typing.Any] = None,
        primaryButtonDisabled: typing.Optional[typing.Any] = None,
        primaryButtonText: typing.Optional[str] = None,
        secondaryButtonText: typing.Optional[str] = None,
        secondaryButtons: typing.Optional[typing.Any] = None,
        selectorPrimaryFocus: typing.Optional[typing.Any] = None,
        selectorsFloatingMenus: typing.Optional[typing.Any] = None,
        shouldSubmitOnEnter: typing.Optional[typing.Any] = None,
        size: typing.Optional[typing.Optional[str]] = None,
        slug: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'alert', 'className', 'closeButtonLabel', 'current', 'danger', 'decorator', 'hasScrollingContent', 'isFullWidth', 'launcherButtonRef', 'loadingDescription', 'loadingIconDescription', 'loadingStatus', 'loading_state', 'modalAriaLabel', 'modalHeading', 'modalLabel', 'onKeyDown', 'onLoadingSuccess', 'onRequestClose', 'onRequestSubmit', 'onSecondarySubmit', 'open', 'passiveModal', 'persisted_props', 'persistence', 'persistence_type', 'preventCloseOnClickOutside', 'primaryButtonDisabled', 'primaryButtonText', 'secondaryButtonText', 'secondaryButtons', 'selectorPrimaryFocus', 'selectorsFloatingMenus', 'shouldSubmitOnEnter', 'size', 'slug', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'alert', 'className', 'closeButtonLabel', 'current', 'danger', 'decorator', 'hasScrollingContent', 'isFullWidth', 'launcherButtonRef', 'loadingDescription', 'loadingIconDescription', 'loadingStatus', 'loading_state', 'modalAriaLabel', 'modalHeading', 'modalLabel', 'onKeyDown', 'onLoadingSuccess', 'onRequestClose', 'onRequestSubmit', 'onSecondarySubmit', 'open', 'passiveModal', 'persisted_props', 'persistence', 'persistence_type', 'preventCloseOnClickOutside', 'primaryButtonDisabled', 'primaryButtonText', 'secondaryButtonText', 'secondaryButtons', 'selectorPrimaryFocus', 'selectorsFloatingMenus', 'shouldSubmitOnEnter', 'size', 'slug', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Modal, self).__init__(children=children, **args)

setattr(Modal, "__init__", _explicitize_args(Modal.__init__))
