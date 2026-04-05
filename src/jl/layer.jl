# AUTO GENERATED FILE - DO NOT EDIT

export layer

"""
    layer(;kwargs...)
    layer(children::Any;kwargs...)
    layer(children_maker::Function;kwargs...)


A Layer component.
Layer is a wrapper for the Carbon Layer component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `as_` (Bool | Real | String | Dict | Array; optional): as
- `className` (String; optional): className
- `level` (Bool | Real | String | Dict | Array; optional): level
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `style` (Dict; optional): style
- `withBackground` (Bool | Real | String | Dict | Array; optional): withBackground
"""
function layer(; kwargs...)
        available_props = Symbol[:children, :id, :as_, :className, :level, :loading_state, :style, :withBackground]
        wild_props = Symbol[]
        return Component("layer", "Layer", "carbon_dash", available_props, wild_props; kwargs...)
end

layer(children::Any; kwargs...) = layer(;kwargs..., children = children)
layer(children_maker::Function; kwargs...) = layer(children_maker(); kwargs...)

