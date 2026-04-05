# AUTO GENERATED FILE - DO NOT EDIT

export row

"""
    row(;kwargs...)
    row(children::Any;kwargs...)
    row(children_maker::Function;kwargs...)


A Row component.
Row is a wrapper for the Carbon Row component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `as_` (Bool | Real | String | Dict | Array; optional): as
- `className` (String; optional): className
- `condensed` (Bool; optional): condensed
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `narrow` (Bool; optional): narrow
- `style` (Dict; optional): style
"""
function row(; kwargs...)
        available_props = Symbol[:children, :id, :as_, :className, :condensed, :loading_state, :narrow, :style]
        wild_props = Symbol[]
        return Component("row", "Row", "carbon_dash", available_props, wild_props; kwargs...)
end

row(children::Any; kwargs...) = row(;kwargs..., children = children)
row(children_maker::Function; kwargs...) = row(children_maker(); kwargs...)

