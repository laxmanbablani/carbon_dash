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


class CodeSnippet(Component):
    """A CodeSnippet component.
CodeSnippet is a wrapper for the Carbon CodeSnippet component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- align (boolean | number | string | dict | list; optional):
    align.

- ariaLabel (boolean | number | string | dict | list; optional):
    ariaLabel.

- autoAlign (boolean | number | string | dict | list; optional):
    autoAlign.

- className (string; default ''):
    className.

- copyButtonDescription (boolean | number | string | dict | list; optional):
    copyButtonDescription.

- copyText (boolean | number | string | dict | list; optional):
    copyText.

- disabled (boolean | number | string | dict | list; optional):
    disabled.

- feedback (boolean | number | string | dict | list; optional):
    feedback.

- feedbackTimeout (boolean | number | string | dict | list; optional):
    feedbackTimeout.

- hideCopyButton (boolean | number | string | dict | list; optional):
    hideCopyButton.

- light (boolean | number | string | dict | list; optional):
    light.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- maxCollapsedNumberOfRows (boolean | number | string | dict | list; optional):
    maxCollapsedNumberOfRows.

- maxExpandedNumberOfRows (boolean | number | string | dict | list; optional):
    maxExpandedNumberOfRows.

- minCollapsedNumberOfRows (boolean | number | string | dict | list; optional):
    minCollapsedNumberOfRows.

- minExpandedNumberOfRows (boolean | number | string | dict | list; optional):
    minExpandedNumberOfRows.

- onClick (boolean | number | string | dict | list; optional):
    onClick.

- showLessText (boolean | number | string | dict | list; optional):
    showLessText.

- showMoreText (boolean | number | string | dict | list; optional):
    showMoreText.

- type (boolean | number | string | dict | list; optional):
    type.

- wrapText (boolean | number | string | dict | list; optional):
    wrapText."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'CodeSnippet'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Optional[str]] = None,
        style: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        loading_state: typing.Optional[typing.Optional[typing.Dict[str, typing.Any]]] = None,
        align: typing.Optional[typing.Any] = None,
        autoAlign: typing.Optional[typing.Any] = None,
        ariaLabel: typing.Optional[typing.Any] = None,
        copyButtonDescription: typing.Optional[typing.Any] = None,
        copyText: typing.Optional[typing.Any] = None,
        disabled: typing.Optional[typing.Any] = None,
        feedback: typing.Optional[typing.Any] = None,
        feedbackTimeout: typing.Optional[typing.Any] = None,
        hideCopyButton: typing.Optional[typing.Any] = None,
        light: typing.Optional[typing.Any] = None,
        maxCollapsedNumberOfRows: typing.Optional[typing.Any] = None,
        maxExpandedNumberOfRows: typing.Optional[typing.Any] = None,
        minCollapsedNumberOfRows: typing.Optional[typing.Any] = None,
        minExpandedNumberOfRows: typing.Optional[typing.Any] = None,
        onClick: typing.Optional[typing.Any] = None,
        showLessText: typing.Optional[typing.Any] = None,
        showMoreText: typing.Optional[typing.Any] = None,
        type: typing.Optional[typing.Any] = None,
        wrapText: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'align', 'ariaLabel', 'autoAlign', 'className', 'copyButtonDescription', 'copyText', 'disabled', 'feedback', 'feedbackTimeout', 'hideCopyButton', 'light', 'loading_state', 'maxCollapsedNumberOfRows', 'maxExpandedNumberOfRows', 'minCollapsedNumberOfRows', 'minExpandedNumberOfRows', 'onClick', 'showLessText', 'showMoreText', 'style', 'type', 'wrapText']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'align', 'ariaLabel', 'autoAlign', 'className', 'copyButtonDescription', 'copyText', 'disabled', 'feedback', 'feedbackTimeout', 'hideCopyButton', 'light', 'loading_state', 'maxCollapsedNumberOfRows', 'maxExpandedNumberOfRows', 'minCollapsedNumberOfRows', 'minExpandedNumberOfRows', 'onClick', 'showLessText', 'showMoreText', 'style', 'type', 'wrapText']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(CodeSnippet, self).__init__(children=children, **args)

setattr(CodeSnippet, "__init__", _explicitize_args(CodeSnippet.__init__))
