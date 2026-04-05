# AUTO GENERATED FILE - DO NOT EDIT

export tablebatchaction

"""
    tablebatchaction(;kwargs...)
    tablebatchaction(children::Any;kwargs...)
    tablebatchaction(children_maker::Function;kwargs...)


A TableBatchAction component.
TableBatchAction is a wrapper for the Carbon TableBatchAction component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `hasIconOnly` (Bool | Real | String | Dict | Array; optional): hasIconOnly
- `iconDescription` (Bool | Real | String | Dict | Array; optional): iconDescription
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `renderIcon` (Bool | Real | String | Dict | Array; optional): renderIcon
- `style` (Dict; optional): style
"""
function tablebatchaction(; kwargs...)
        available_props = Symbol[:children, :id, :className, :hasIconOnly, :iconDescription, :loading_state, :renderIcon, :style]
        wild_props = Symbol[]
        return Component("tablebatchaction", "TableBatchAction", "carbon_dash", available_props, wild_props; kwargs...)
end

tablebatchaction(children::Any; kwargs...) = tablebatchaction(;kwargs..., children = children)
tablebatchaction(children_maker::Function; kwargs...) = tablebatchaction(children_maker(); kwargs...)

