# AUTO GENERATED FILE - DO NOT EDIT

export pagination

"""
    pagination(;kwargs...)
    pagination(children::Any;kwargs...)
    pagination(children_maker::Function;kwargs...)


A Pagination component.
Pagination is a wrapper for the Carbon Pagination component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `backwardText` (Bool | Real | String | Dict | Array; optional): backwardText
- `className` (String; optional): className
- `debounce` (Bool | Real; optional): debounce
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `forwardText` (Bool | Real | String | Dict | Array; optional): forwardText
- `isLastPage` (Bool | Real | String | Dict | Array; optional): isLastPage
- `itemRangeText` (Bool | Real | String | Dict | Array; optional): itemRangeText
- `itemText` (Bool | Real | String | Dict | Array; optional): itemText
- `itemsPerPageText` (Bool | Real | String | Dict | Array; optional): itemsPerPageText
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `n_blur` (Real; optional): n_blur
- `n_submit` (Real; optional): n_submit
- `onChange` (Bool | Real | String | Dict | Array; optional): onChange
- `page` (Bool | Real | String | Dict | Array; optional): page
- `pageInputDisabled` (Bool | Real | String | Dict | Array; optional): pageInputDisabled
- `pageNumberText` (Bool | Real | String | Dict | Array; optional): pageNumberText
- `pageRangeText` (Bool | Real | String | Dict | Array; optional): pageRangeText
- `pageSelectLabelText` (Bool | Real | String | Dict | Array; optional): pageSelectLabelText
- `pageSize` (Bool | Real | String | Dict | Array; optional): pageSize
- `pageSizeInputDisabled` (Bool | Real | String | Dict | Array; optional): pageSizeInputDisabled
- `pageSizes` (Bool | Real | String | Dict | Array; optional): pageSizes
- `pageText` (Bool | Real | String | Dict | Array; optional): pageText
- `pagesUnknown` (Bool | Real | String | Dict | Array; optional): pagesUnknown
- `persisted_props` (Array of Strings; optional): persisted_props
- `persistence` (Bool | String | Real; optional): persistence
- `persistence_type` (a value equal to: 'local', 'session', 'memory'; optional): persistence_type
- `size` (Bool | Real | String | Dict | Array; optional): size
- `style` (Dict; optional): style
- `text` (Bool | Real | String | Dict | Array; optional): text
- `totalItems` (Bool | Real | String | Dict | Array; optional): totalItems
- `value` (Bool | Real | String | Dict | Array; optional): value
"""
function pagination(; kwargs...)
        available_props = Symbol[:children, :id, :backwardText, :className, :debounce, :disabled, :forwardText, :isLastPage, :itemRangeText, :itemText, :itemsPerPageText, :loading_state, :n_blur, :n_submit, :onChange, :page, :pageInputDisabled, :pageNumberText, :pageRangeText, :pageSelectLabelText, :pageSize, :pageSizeInputDisabled, :pageSizes, :pageText, :pagesUnknown, :persisted_props, :persistence, :persistence_type, :size, :style, :text, :totalItems, :value]
        wild_props = Symbol[]
        return Component("pagination", "Pagination", "carbon_dash", available_props, wild_props; kwargs...)
end

pagination(children::Any; kwargs...) = pagination(;kwargs..., children = children)
pagination(children_maker::Function; kwargs...) = pagination(children_maker(); kwargs...)

