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


class FileUploader(Component):
    """A FileUploader component.
FileUploader is a wrapper for the Carbon FileUploader component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- accept (boolean | number | string | dict | list; optional):
    accept.

- buttonKind (boolean | number | string | dict | list; optional):
    buttonKind.

- buttonLabel (boolean | number | string | dict | list; optional):
    buttonLabel.

- className (string; default ''):
    className.

- disabled (boolean | number | string | dict | list; optional):
    disabled.

- filenameStatus (boolean | number | string | dict | list; optional):
    filenameStatus.

- iconDescription (boolean | number | string | dict | list; optional):
    iconDescription.

- labelDescription (boolean | number | string | dict | list; optional):
    labelDescription.

- labelTitle (boolean | number | string | dict | list; optional):
    labelTitle.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- maxFileSize (boolean | number | string | dict | list; optional):
    maxFileSize.

- multiple (boolean | number | string | dict | list; optional):
    multiple.

- name (boolean | number | string | dict | list; optional):
    name.

- onAddFiles (boolean | number | string | dict | list; optional):
    onAddFiles.

- onChange (boolean | number | string | dict | list; optional):
    onChange.

- onClick (boolean | number | string | dict | list; optional):
    onClick.

- onDelete (boolean | number | string | dict | list; optional):
    onDelete.

- size (boolean | number | string | dict | list; optional):
    size."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'FileUploader'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        accept: typing.Optional[typing.Any] = None,
        buttonKind: typing.Optional[typing.Any] = None,
        buttonLabel: typing.Optional[typing.Any] = None,
        disabled: typing.Optional[typing.Any] = None,
        filenameStatus: typing.Optional[typing.Any] = None,
        iconDescription: typing.Optional[typing.Any] = None,
        labelDescription: typing.Optional[typing.Any] = None,
        labelTitle: typing.Optional[typing.Any] = None,
        maxFileSize: typing.Optional[typing.Any] = None,
        multiple: typing.Optional[typing.Any] = None,
        name: typing.Optional[typing.Any] = None,
        onAddFiles: typing.Optional[typing.Any] = None,
        onChange: typing.Optional[typing.Any] = None,
        onClick: typing.Optional[typing.Any] = None,
        onDelete: typing.Optional[typing.Any] = None,
        size: typing.Optional[typing.Optional[str]] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'accept', 'buttonKind', 'buttonLabel', 'className', 'disabled', 'filenameStatus', 'iconDescription', 'labelDescription', 'labelTitle', 'loading_state', 'maxFileSize', 'multiple', 'name', 'onAddFiles', 'onChange', 'onClick', 'onDelete', 'size', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'accept', 'buttonKind', 'buttonLabel', 'className', 'disabled', 'filenameStatus', 'iconDescription', 'labelDescription', 'labelTitle', 'loading_state', 'maxFileSize', 'multiple', 'name', 'onAddFiles', 'onChange', 'onClick', 'onDelete', 'size', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FileUploader, self).__init__(children=children, **args)

setattr(FileUploader, "__init__", _explicitize_args(FileUploader.__init__))
