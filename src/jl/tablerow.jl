# AUTO GENERATED FILE - DO NOT EDIT

export tablerow

"""
    tablerow(;kwargs...)
    tablerow(children::Any;kwargs...)
    tablerow(children_maker::Function;kwargs...)


A TableRow component.
TableRow is a wrapper for the Carbon TableRow component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `ariaLabel` (Bool | Real | String | Dict | Array; optional): ariaLabel
- `className` (String; optional): className
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
function tablerow(; kwargs...)
        available_props = Symbol[:children, :id, :ariaLabel, :className, :isExpanded, :isSelected, :loading_state, :onExpand, :style]
        wild_props = Symbol[]
        return Component("tablerow", "TableRow", "carbon_dash", available_props, wild_props; kwargs...)
end

tablerow(children::Any; kwargs...) = tablerow(;kwargs..., children = children)
tablerow(children_maker::Function; kwargs...) = tablerow(children_maker(); kwargs...)

