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


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional)

- alert (boolean; default False):
    Whether to alert the user.

- className (string; optional)

- danger (boolean; default False):
    Whether the modal is a danger modal.

- fullWidth (boolean; default False):
    Whether the modal should be full width.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- modalHeading (a list of or a singular dash component, string or number; optional):
    Modal heading.

- open (boolean; default False):
    Whether the modal is open.

- passiveModal (boolean; default False):
    Whether the modal should be passive.

- preventCloseOnClickOutside (boolean; optional):
    Whether to show the close button.

- primaryButtonDisabled (boolean; optional):
    Primary button disabled.

- primaryButtonText (string; optional):
    Primary button text.

- secondaryButtonText (string; optional):
    Secondary button text.

- selectorPrimaryFocus (string; optional):
    Selector for focus on modal open.

- shouldSubmitOnEnter (boolean; optional):
    Whether the modal should be displayed with a slider.

- size (a value equal to: 'xs', 'sm', 'md', 'lg'; optional):
    Size."""
    _children_props: typing.List[str] = ['modalHeading']
    _base_nodes = ['modalHeading', 'children']
    _namespace = 'carbon_dash'
    _type = 'Modal'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        open: typing.Optional[bool] = None,
        modalHeading: typing.Optional[ComponentType] = None,
        primaryButtonText: typing.Optional[str] = None,
        secondaryButtonText: typing.Optional[str] = None,
        danger: typing.Optional[bool] = None,
        fullWidth: typing.Optional[bool] = None,
        passiveModal: typing.Optional[bool] = None,
        preventCloseOnClickOutside: typing.Optional[bool] = None,
        size: typing.Optional[typing.Optional[str]] = None,
        alert: typing.Optional[bool] = None,
        shouldSubmitOnEnter: typing.Optional[bool] = None,
        primaryButtonDisabled: typing.Optional[bool] = None,
        selectorPrimaryFocus: typing.Optional[str] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'alert', 'className', 'danger', 'fullWidth', 'loading_state', 'modalHeading', 'open', 'passiveModal', 'preventCloseOnClickOutside', 'primaryButtonDisabled', 'primaryButtonText', 'secondaryButtonText', 'selectorPrimaryFocus', 'shouldSubmitOnEnter', 'size', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'alert', 'className', 'danger', 'fullWidth', 'loading_state', 'modalHeading', 'open', 'passiveModal', 'preventCloseOnClickOutside', 'primaryButtonDisabled', 'primaryButtonText', 'secondaryButtonText', 'selectorPrimaryFocus', 'shouldSubmitOnEnter', 'size', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Modal, self).__init__(children=children, **args)

setattr(Modal, "__init__", _explicitize_args(Modal.__init__))
