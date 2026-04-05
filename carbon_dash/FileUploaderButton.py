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


class FileUploaderButton(Component):
    """A FileUploaderButton component.
FileUploaderButton is a wrapper for the Carbon FileUploaderButton component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- accept (boolean | number | string | dict | list; optional):
    accept.

- buttonKind (boolean | number | string | dict | list; optional):
    buttonKind.

- className (string; default ''):
    className.

- disableLabelChanges (boolean | number | string | dict | list; optional):
    disableLabelChanges.

- disabled (boolean | number | string | dict | list; optional):
    disabled.

- labelText (boolean | number | string | dict | list; optional):
    labelText.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- multiple (boolean | number | string | dict | list; optional):
    multiple.

- name (boolean | number | string | dict | list; optional):
    name.

- onChange (boolean | number | string | dict | list; optional):
    onChange.

- onClick (boolean | number | string | dict | list; optional):
    onClick.

- role (boolean | number | string | dict | list; optional):
    role.

- size (boolean | number | string | dict | list; optional):
    size.

- tabIndex (boolean | number | string | dict | list; optional):
    tabIndex."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'FileUploaderButton'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        accept: typing.Optional[typing.Any] = None,
        buttonKind: typing.Optional[typing.Any] = None,
        disableLabelChanges: typing.Optional[typing.Any] = None,
        disabled: typing.Optional[typing.Any] = None,
        labelText: typing.Optional[typing.Any] = None,
        multiple: typing.Optional[typing.Any] = None,
        name: typing.Optional[typing.Any] = None,
        onChange: typing.Optional[typing.Any] = None,
        onClick: typing.Optional[typing.Any] = None,
        role: typing.Optional[typing.Any] = None,
        size: typing.Optional[typing.Optional[str]] = None,
        tabIndex: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'accept', 'buttonKind', 'className', 'disableLabelChanges', 'disabled', 'labelText', 'loading_state', 'multiple', 'name', 'onChange', 'onClick', 'role', 'size', 'style', 'tabIndex']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'accept', 'buttonKind', 'className', 'disableLabelChanges', 'disabled', 'labelText', 'loading_state', 'multiple', 'name', 'onChange', 'onClick', 'role', 'size', 'style', 'tabIndex']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FileUploaderButton, self).__init__(children=children, **args)

setattr(FileUploaderButton, "__init__", _explicitize_args(FileUploaderButton.__init__))
