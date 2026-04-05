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


class Pagination(Component):
    """A Pagination component.
Pagination is a wrapper for the Carbon Pagination component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    children.

- id (string; optional):
    id.

- backwardText (boolean | number | string | dict | list; optional):
    backwardText.

- className (string; default ''):
    className.

- debounce (boolean | number; optional):
    debounce.

- disabled (boolean | number | string | dict | list; optional):
    disabled.

- forwardText (boolean | number | string | dict | list; optional):
    forwardText.

- isLastPage (boolean | number | string | dict | list; optional):
    isLastPage.

- itemRangeText (boolean | number | string | dict | list; optional):
    itemRangeText.

- itemText (boolean | number | string | dict | list; optional):
    itemText.

- itemsPerPageText (boolean | number | string | dict | list; optional):
    itemsPerPageText.

- loading_state (dict; optional):
    loading_state.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

    - prop_name (string; optional)

    - component_name (string; optional)

- n_blur (number; optional):
    n_blur.

- n_submit (number; optional):
    n_submit.

- onChange (boolean | number | string | dict | list; optional):
    onChange.

- page (boolean | number | string | dict | list; optional):
    page.

- pageInputDisabled (boolean | number | string | dict | list; optional):
    pageInputDisabled.

- pageNumberText (boolean | number | string | dict | list; optional):
    pageNumberText.

- pageRangeText (boolean | number | string | dict | list; optional):
    pageRangeText.

- pageSelectLabelText (boolean | number | string | dict | list; optional):
    pageSelectLabelText.

- pageSize (boolean | number | string | dict | list; optional):
    pageSize.

- pageSizeInputDisabled (boolean | number | string | dict | list; optional):
    pageSizeInputDisabled.

- pageSizes (boolean | number | string | dict | list; optional):
    pageSizes.

- pageText (boolean | number | string | dict | list; optional):
    pageText.

- pagesUnknown (boolean | number | string | dict | list; optional):
    pagesUnknown.

- persisted_props (list of strings; optional):
    persisted_props.

- persistence (boolean | string | number; optional):
    persistence.

- persistence_type (a value equal to: 'local', 'session', 'memory'; optional):
    persistence_type.

- size (boolean | number | string | dict | list; optional):
    size.

- text (boolean | number | string | dict | list; optional):
    text.

- totalItems (boolean | number | string | dict | list; optional):
    totalItems.

- value (boolean | number | string | dict | list; optional):
    value."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'carbon_dash'
    _type = 'Pagination'


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
        n_blur: typing.Optional[NumberType] = None,
        n_submit: typing.Optional[NumberType] = None,
        debounce: typing.Optional[typing.Union[bool, NumberType]] = None,
        backwardText: typing.Optional[typing.Any] = None,
        disabled: typing.Optional[typing.Any] = None,
        forwardText: typing.Optional[typing.Any] = None,
        isLastPage: typing.Optional[typing.Any] = None,
        itemRangeText: typing.Optional[typing.Any] = None,
        itemText: typing.Optional[typing.Any] = None,
        itemsPerPageText: typing.Optional[typing.Any] = None,
        onChange: typing.Optional[typing.Any] = None,
        page: typing.Optional[typing.Any] = None,
        pageInputDisabled: typing.Optional[typing.Any] = None,
        pageNumberText: typing.Optional[typing.Any] = None,
        pageRangeText: typing.Optional[typing.Any] = None,
        pageSelectLabelText: typing.Optional[typing.Any] = None,
        pageSize: typing.Optional[typing.Any] = None,
        pageSizeInputDisabled: typing.Optional[typing.Any] = None,
        pageSizes: typing.Optional[typing.Any] = None,
        text: typing.Optional[typing.Any] = None,
        value: typing.Optional[typing.Any] = None,
        pageText: typing.Optional[typing.Any] = None,
        pagesUnknown: typing.Optional[typing.Any] = None,
        size: typing.Optional[typing.Optional[str]] = None,
        totalItems: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'backwardText', 'className', 'debounce', 'disabled', 'forwardText', 'isLastPage', 'itemRangeText', 'itemText', 'itemsPerPageText', 'loading_state', 'n_blur', 'n_submit', 'onChange', 'page', 'pageInputDisabled', 'pageNumberText', 'pageRangeText', 'pageSelectLabelText', 'pageSize', 'pageSizeInputDisabled', 'pageSizes', 'pageText', 'pagesUnknown', 'persisted_props', 'persistence', 'persistence_type', 'size', 'style', 'text', 'totalItems', 'value']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'backwardText', 'className', 'debounce', 'disabled', 'forwardText', 'isLastPage', 'itemRangeText', 'itemText', 'itemsPerPageText', 'loading_state', 'n_blur', 'n_submit', 'onChange', 'page', 'pageInputDisabled', 'pageNumberText', 'pageRangeText', 'pageSelectLabelText', 'pageSize', 'pageSizeInputDisabled', 'pageSizes', 'pageText', 'pagesUnknown', 'persisted_props', 'persistence', 'persistence_type', 'size', 'style', 'text', 'totalItems', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Pagination, self).__init__(children=children, **args)

setattr(Pagination, "__init__", _explicitize_args(Pagination.__init__))
