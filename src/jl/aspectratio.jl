# AUTO GENERATED FILE - DO NOT EDIT

export aspectratio

"""
    aspectratio(;kwargs...)
    aspectratio(children::Any;kwargs...)
    aspectratio(children_maker::Function;kwargs...)


An AspectRatio component.
AspectRatio is a wrapper for the Carbon AspectRatio component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `as_` (Bool | Real | String | Dict | Array; optional): as
- `className` (String; optional): className
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `ratio` (Bool | Real | String | Dict | Array; optional): ratio
- `style` (Dict; optional): style
"""
function aspectratio(; kwargs...)
        available_props = Symbol[:children, :id, :as_, :className, :loading_state, :ratio, :style]
        wild_props = Symbol[]
        return Component("aspectratio", "AspectRatio", "carbon_dash", available_props, wild_props; kwargs...)
end

aspectratio(children::Any; kwargs...) = aspectratio(;kwargs..., children = children)
aspectratio(children_maker::Function; kwargs...) = aspectratio(children_maker(); kwargs...)

