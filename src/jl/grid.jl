# AUTO GENERATED FILE - DO NOT EDIT

export grid

"""
    grid(;kwargs...)
    grid(children::Any;kwargs...)
    grid(children_maker::Function;kwargs...)


A Grid component.
Grid is a wrapper for the Carbon Grid component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `align` (Bool | Real | String | Dict | Array; optional): align
- `as_` (Bool | Real | String | Dict | Array; optional): as
- `className` (String; optional): className
- `condensed` (Bool; optional): condensed
- `fullWidth` (Bool; optional): fullWidth
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `narrow` (Bool; optional): narrow
- `style` (Dict; optional): style
"""
function grid(; kwargs...)
        available_props = Symbol[:children, :id, :align, :as_, :className, :condensed, :fullWidth, :loading_state, :narrow, :style]
        wild_props = Symbol[]
        return Component("grid", "Grid", "carbon_dash", available_props, wild_props; kwargs...)
end

grid(children::Any; kwargs...) = grid(;kwargs..., children = children)
grid(children_maker::Function; kwargs...) = grid(children_maker(); kwargs...)

