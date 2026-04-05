# AUTO GENERATED FILE - DO NOT EDIT

export tablebatchactions

"""
    tablebatchactions(;kwargs...)
    tablebatchactions(children::Any;kwargs...)
    tablebatchactions(children_maker::Function;kwargs...)


A TableBatchActions component.
TableBatchActions is a wrapper for the Carbon TableBatchActions component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `onCancel` (Bool | Real | String | Dict | Array; optional): onCancel
- `onSelectAll` (Bool | Real | String | Dict | Array; optional): onSelectAll
- `shouldShowBatchActions` (Bool | Real | String | Dict | Array; optional): shouldShowBatchActions
- `style` (Dict; optional): style
- `totalCount` (Bool | Real | String | Dict | Array; optional): totalCount
- `totalSelected` (Bool | Real | String | Dict | Array; optional): totalSelected
- `translateWithId` (Bool | Real | String | Dict | Array; optional): translateWithId
"""
function tablebatchactions(; kwargs...)
        available_props = Symbol[:children, :id, :className, :loading_state, :onCancel, :onSelectAll, :shouldShowBatchActions, :style, :totalCount, :totalSelected, :translateWithId]
        wild_props = Symbol[]
        return Component("tablebatchactions", "TableBatchActions", "carbon_dash", available_props, wild_props; kwargs...)
end

tablebatchactions(children::Any; kwargs...) = tablebatchactions(;kwargs..., children = children)
tablebatchactions(children_maker::Function; kwargs...) = tablebatchactions(children_maker(); kwargs...)

