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


class ModalHeader(Component):
    """A ModalHeader component.
ModalHeader is a wrapper for the Carbon ModalHeader component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- buttonOnClick (boolean | number | string | dict | list; optional):
    buttonOnClick.

- className (string; default ''):
    className.

- closeClassName (boolean | number | string | dict | list; optional):
    closeClassName.

- closeIconClassName (a list of or a singular dash component, string or number; optional):
    closeIconClassName.

- closeModal (boolean | number | string | dict | list; optional):
    closeModal.

- iconDescription (boolean | number | string | dict | list; optional):
    iconDescription.

- label (boolean | number | string | dict | list; optional):
    label.

- labelClassName (boolean | number | string | dict | list; optional):
    labelClassName.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- title (boolean | number | string | dict | list; optional):
    title.

- titleClassName (boolean | number | string | dict | list; optional):
    titleClassName."""
    _children_props: typing.List[str] = ['closeIconClassName']
    _base_nodes = ['closeIconClassName', 'children']
    _namespace = 'carbon_dash'
    _type = 'ModalHeader'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        buttonOnClick: typing.Optional[typing.Any] = None,
        closeClassName: typing.Optional[typing.Any] = None,
        closeIconClassName: typing.Optional[ComponentType] = None,
        closeModal: typing.Optional[typing.Any] = None,
        iconDescription: typing.Optional[typing.Any] = None,
        label: typing.Optional[typing.Any] = None,
        labelClassName: typing.Optional[typing.Any] = None,
        title: typing.Optional[typing.Any] = None,
        titleClassName: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'buttonOnClick', 'className', 'closeClassName', 'closeIconClassName', 'closeModal', 'iconDescription', 'label', 'labelClassName', 'loading_state', 'style', 'title', 'titleClassName']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'buttonOnClick', 'className', 'closeClassName', 'closeIconClassName', 'closeModal', 'iconDescription', 'label', 'labelClassName', 'loading_state', 'style', 'title', 'titleClassName']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(ModalHeader, self).__init__(children=children, **args)

setattr(ModalHeader, "__init__", _explicitize_args(ModalHeader.__init__))
