# AUTO GENERATED FILE - DO NOT EDIT

export vstack

"""
    vstack(;kwargs...)
    vstack(children::Any;kwargs...)
    vstack(children_maker::Function;kwargs...)


A VStack component.
VStack is a wrapper for the Carbon VStack component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `as_` (Bool | Real | String | Dict | Array; optional): as
- `className` (String; optional): className
- `gap` (Bool | Real | String | Dict | Array; optional): gap
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `orientation` (Bool | Real | String | Dict | Array; optional): orientation
- `style` (Dict; optional): style
"""
function vstack(; kwargs...)
        available_props = Symbol[:children, :id, :as_, :className, :gap, :loading_state, :orientation, :style]
        wild_props = Symbol[]
        return Component("vstack", "VStack", "carbon_dash", available_props, wild_props; kwargs...)
end

vstack(children::Any; kwargs...) = vstack(;kwargs..., children = children)
vstack(children_maker::Function; kwargs...) = vstack(children_maker(); kwargs...)

