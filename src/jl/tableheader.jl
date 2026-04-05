# AUTO GENERATED FILE - DO NOT EDIT

export tableheader

"""
    tableheader(;kwargs...)
    tableheader(children::Any;kwargs...)
    tableheader(children_maker::Function;kwargs...)


A TableHeader component.
TableHeader is a wrapper for the Carbon TableHeader component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `colSpan` (Bool | Real | String | Dict | Array; optional): colSpan
- `isSortHeader` (Bool | Real | String | Dict | Array; optional): isSortHeader
- `isSortable` (Bool | Real | String | Dict | Array; optional): isSortable
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `onClick` (Bool | Real | String | Dict | Array; optional): onClick
- `scope` (Bool | Real | String | Dict | Array; optional): scope
- `sortDirection` (Bool | Real | String | Dict | Array; optional): sortDirection
- `style` (Dict; optional): style
- `translateWithId` (Bool | Real | String | Dict | Array; optional): translateWithId
"""
function tableheader(; kwargs...)
        available_props = Symbol[:children, :id, :className, :colSpan, :isSortHeader, :isSortable, :loading_state, :onClick, :scope, :sortDirection, :style, :translateWithId]
        wild_props = Symbol[]
        return Component("tableheader", "TableHeader", "carbon_dash", available_props, wild_props; kwargs...)
end

tableheader(children::Any; kwargs...) = tableheader(;kwargs..., children = children)
tableheader(children_maker::Function; kwargs...) = tableheader(children_maker(); kwargs...)

