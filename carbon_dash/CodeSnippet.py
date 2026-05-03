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
Displays a block or inline snippet of code with copy functionality.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The code content to be displayed.

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- className (string; optional):
    Custom CSS class.

- copyButtonDescription (string; optional):
    Specify the description for the Copy Button.

- copyText (string; optional):
    Optional text to copy. If not specified, children innerText will
    be used.

- disabled (boolean; optional):
    Specify whether or not the CodeSnippet should be disabled.

- feedback (string; optional):
    Specify the string displayed when the snippet is copied.

- feedbackTimeout (number; optional):
    Specify the time it takes for the feedback message to timeout.

- hideCopyButton (boolean; optional):
    Specify whether or not a copy button should be rendered.

- loading_state (dict; optional):
    Dash loading state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- maxCollapsedNumberOfRows (number; default 15):
    Specify the maximum number of rows to show when collapsed.

- maxExpandedNumberOfRows (number; optional):
    Specify the maximum number of rows to show when expanded.

- type (a value equal to: 'single', 'multi', 'inline'; default 'single'):
    The type of code snippet.

- wrapText (boolean; default False):
    Specify whether to wrap the text."""
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
        type: typing.Optional[Literal["single", "multi", "inline"]] = None,
        feedback: typing.Optional[str] = None,
        copyButtonDescription: typing.Optional[str] = None,
        wrapText: typing.Optional[bool] = None,
        maxCollapsedNumberOfRows: typing.Optional[NumberType] = None,
        feedbackTimeout: typing.Optional[NumberType] = None,
        copyText: typing.Optional[str] = None,
        hideCopyButton: typing.Optional[bool] = None,
        disabled: typing.Optional[bool] = None,
        maxExpandedNumberOfRows: typing.Optional[NumberType] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'copyButtonDescription', 'copyText', 'disabled', 'feedback', 'feedbackTimeout', 'hideCopyButton', 'loading_state', 'maxCollapsedNumberOfRows', 'maxExpandedNumberOfRows', 'style', 'type', 'wrapText']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'copyButtonDescription', 'copyText', 'disabled', 'feedback', 'feedbackTimeout', 'hideCopyButton', 'loading_state', 'maxCollapsedNumberOfRows', 'maxExpandedNumberOfRows', 'style', 'type', 'wrapText']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(CodeSnippet, self).__init__(children=children, **args)

setattr(CodeSnippet, "__init__", _explicitize_args(CodeSnippet.__init__))
