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


class ModalWrapper(Component):
    """A ModalWrapper component.
ModalWrapper is a wrapper for the Carbon ModalWrapper component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- buttonTriggerClassName (boolean | number | string | dict | list; optional):
    buttonTriggerClassName.

- buttonTriggerText (boolean | number | string | dict | list; optional):
    buttonTriggerText.

- className (string; default ''):
    className.

- disabled (boolean | number | string | dict | list; optional):
    disabled.

- handleOpen (boolean | number | string | dict | list; optional):
    handleOpen.

- handleSubmit (boolean | number | string | dict | list; optional):
    handleSubmit.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- modalBeforeContent (boolean | number | string | dict | list; optional):
    modalBeforeContent.

- modalHeading (boolean | number | string | dict | list; optional):
    modalHeading.

- modalLabel (boolean | number | string | dict | list; optional):
    modalLabel.

- modalText (boolean | number | string | dict | list; optional):
    modalText.

- onKeyDown (boolean | number | string | dict | list; optional):
    onKeyDown.

- passiveModal (boolean | number | string | dict | list; optional):
    passiveModal.

- preventCloseOnClickOutside (boolean | number | string | dict | list; optional):
    preventCloseOnClickOutside.

- primaryButtonText (boolean | number | string | dict | list; optional):
    primaryButtonText.

- renderTriggerButtonIcon (boolean | number | string | dict | list; optional):
    renderTriggerButtonIcon.

- secondaryButtonText (boolean | number | string | dict | list; optional):
    secondaryButtonText.

- selectorPrimaryFocus (boolean | number | string | dict | list; optional):
    selectorPrimaryFocus.

- shouldCloseAfterSubmit (boolean | number | string | dict | list; optional):
    shouldCloseAfterSubmit.

- status (boolean | number | string | dict | list; optional):
    status.

- triggerButtonIconDescription (boolean | number | string | dict | list; optional):
    triggerButtonIconDescription.

- triggerButtonKind (boolean | number | string | dict | list; optional):
    triggerButtonKind.

- withHeader (boolean | number | string | dict | list; optional):
    withHeader."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'ModalWrapper'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        buttonTriggerClassName: typing.Optional[typing.Any] = None,
        buttonTriggerText: typing.Optional[typing.Any] = None,
        disabled: typing.Optional[typing.Any] = None,
        handleOpen: typing.Optional[typing.Any] = None,
        handleSubmit: typing.Optional[typing.Any] = None,
        modalBeforeContent: typing.Optional[typing.Any] = None,
        modalHeading: typing.Optional[typing.Any] = None,
        modalLabel: typing.Optional[typing.Any] = None,
        modalText: typing.Optional[typing.Any] = None,
        onKeyDown: typing.Optional[typing.Any] = None,
        passiveModal: typing.Optional[typing.Any] = None,
        preventCloseOnClickOutside: typing.Optional[typing.Any] = None,
        primaryButtonText: typing.Optional[typing.Any] = None,
        renderTriggerButtonIcon: typing.Optional[typing.Any] = None,
        secondaryButtonText: typing.Optional[typing.Any] = None,
        selectorPrimaryFocus: typing.Optional[typing.Any] = None,
        shouldCloseAfterSubmit: typing.Optional[typing.Any] = None,
        status: typing.Optional[typing.Any] = None,
        triggerButtonIconDescription: typing.Optional[typing.Any] = None,
        triggerButtonKind: typing.Optional[typing.Any] = None,
        withHeader: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'buttonTriggerClassName', 'buttonTriggerText', 'className', 'disabled', 'handleOpen', 'handleSubmit', 'loading_state', 'modalBeforeContent', 'modalHeading', 'modalLabel', 'modalText', 'onKeyDown', 'passiveModal', 'preventCloseOnClickOutside', 'primaryButtonText', 'renderTriggerButtonIcon', 'secondaryButtonText', 'selectorPrimaryFocus', 'shouldCloseAfterSubmit', 'status', 'style', 'triggerButtonIconDescription', 'triggerButtonKind', 'withHeader']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'buttonTriggerClassName', 'buttonTriggerText', 'className', 'disabled', 'handleOpen', 'handleSubmit', 'loading_state', 'modalBeforeContent', 'modalHeading', 'modalLabel', 'modalText', 'onKeyDown', 'passiveModal', 'preventCloseOnClickOutside', 'primaryButtonText', 'renderTriggerButtonIcon', 'secondaryButtonText', 'selectorPrimaryFocus', 'shouldCloseAfterSubmit', 'status', 'style', 'triggerButtonIconDescription', 'triggerButtonKind', 'withHeader']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(ModalWrapper, self).__init__(children=children, **args)

setattr(ModalWrapper, "__init__", _explicitize_args(ModalWrapper.__init__))
