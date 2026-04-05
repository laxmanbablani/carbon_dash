# AUTO GENERATED FILE - DO NOT EDIT

export tableexpandrow

"""
    tableexpandrow(;kwargs...)
    tableexpandrow(children::Any;kwargs...)
    tableexpandrow(children_maker::Function;kwargs...)


A TableExpandRow component.
TableExpandRow is a wrapper for the Carbon TableExpandRow component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `ariaLabel` (Bool | Real | String | Dict | Array; optional): ariaLabel
- `className` (String; optional): className
- `expandHeader` (Bool | Real | String | Dict | Array; optional): expandHeader
- `expandIconDescription` (Bool | Real | String | Dict | Array; optional): expandIconDescription
- `isExpanded` (Bool | Real | String | Dict | Array; optional): isExpanded
- `isSelected` (Bool | Real | String | Dict | Array; optional): isSelected
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `onExpand` (Bool | Real | String | Dict | Array; optional): onExpand
- `style` (Dict; optional): style
"""
function tableexpandrow(; kwargs...)
        available_props = Symbol[:children, :id, :ariaLabel, :className, :expandHeader, :expandIconDescription, :isExpanded, :isSelected, :loading_state, :onExpand, :style]
        wild_props = Symbol[]
        return Component("tableexpandrow", "TableExpandRow", "carbon_dash", available_props, wild_props; kwargs...)
end

tableexpandrow(children::Any; kwargs...) = tableexpandrow(;kwargs..., children = children)
tableexpandrow(children_maker::Function; kwargs...) = tableexpandrow(children_maker(); kwargs...)

