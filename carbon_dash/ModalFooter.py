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


class ModalFooter(Component):
    """A ModalFooter component.
ModalFooter is a wrapper for the Carbon ModalFooter component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- className (string; default ''):
    className.

- closeModal (boolean | number | string | dict | list; optional):
    closeModal.

- danger (boolean | number | string | dict | list; optional):
    danger.

- inputref (boolean | number | string | dict | list; optional):
    inputref.

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

- onLoadingSuccess (boolean | number | string | dict | list; optional):
    onLoadingSuccess.

- onRequestClose (boolean | number | string | dict | list; optional):
    onRequestClose.

- onRequestSubmit (boolean | number | string | dict | list; optional):
    onRequestSubmit.

- primaryButtonDisabled (boolean | number | string | dict | list; optional):
    primaryButtonDisabled.

- primaryButtonText (boolean | number | string | dict | list; optional):
    primaryButtonText.

- primaryClassName (boolean | number | string | dict | list; optional):
    primaryClassName.

- secondaryButtonText (boolean | number | string | dict | list; optional):
    secondaryButtonText.

- secondaryButtons (boolean | number | string | dict | list; optional):
    secondaryButtons.

- secondaryClassName (boolean | number | string | dict | list; optional):
    secondaryClassName."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'ModalFooter'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        closeModal: typing.Optional[typing.Any] = None,
        danger: typing.Optional[typing.Any] = None,
        inputref: typing.Optional[typing.Any] = None,
        loadingDescription: typing.Optional[typing.Any] = None,
        loadingIconDescription: typing.Optional[typing.Any] = None,
        loadingStatus: typing.Optional[typing.Any] = None,
        onLoadingSuccess: typing.Optional[typing.Any] = None,
        onRequestClose: typing.Optional[typing.Any] = None,
        onRequestSubmit: typing.Optional[typing.Any] = None,
        primaryButtonDisabled: typing.Optional[typing.Any] = None,
        primaryButtonText: typing.Optional[typing.Any] = None,
        primaryClassName: typing.Optional[typing.Any] = None,
        secondaryButtonText: typing.Optional[typing.Any] = None,
        secondaryButtons: typing.Optional[typing.Any] = None,
        secondaryClassName: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'closeModal', 'danger', 'inputref', 'loadingDescription', 'loadingIconDescription', 'loadingStatus', 'loading_state', 'onLoadingSuccess', 'onRequestClose', 'onRequestSubmit', 'primaryButtonDisabled', 'primaryButtonText', 'primaryClassName', 'secondaryButtonText', 'secondaryButtons', 'secondaryClassName', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'closeModal', 'danger', 'inputref', 'loadingDescription', 'loadingIconDescription', 'loadingStatus', 'loading_state', 'onLoadingSuccess', 'onRequestClose', 'onRequestSubmit', 'primaryButtonDisabled', 'primaryButtonText', 'primaryClassName', 'secondaryButtonText', 'secondaryButtons', 'secondaryClassName', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(ModalFooter, self).__init__(children=children, **args)

setattr(ModalFooter, "__init__", _explicitize_args(ModalFooter.__init__))
