# AUTO GENERATED FILE - DO NOT EDIT

export flexgrid

"""
    flexgrid(;kwargs...)
    flexgrid(children::Any;kwargs...)
    flexgrid(children_maker::Function;kwargs...)


A FlexGrid component.
FlexGrid is a wrapper for the Carbon FlexGrid component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `as_` (Bool | Real | String | Dict | Array; optional): as
- `className` (String; optional): className
- `condensed` (Bool | Real | String | Dict | Array; optional): condensed
- `fullWidth` (Bool | Real | String | Dict | Array; optional): fullWidth
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `narrow` (Bool | Real | String | Dict | Array; optional): narrow
- `style` (Dict; optional): style
"""
function flexgrid(; kwargs...)
        available_props = Symbol[:children, :id, :as_, :className, :condensed, :fullWidth, :loading_state, :narrow, :style]
        wild_props = Symbol[]
        return Component("flexgrid", "FlexGrid", "carbon_dash", available_props, wild_props; kwargs...)
end

flexgrid(children::Any; kwargs...) = flexgrid(;kwargs..., children = children)
flexgrid(children_maker::Function; kwargs...) = flexgrid(children_maker(); kwargs...)

