# AUTO GENERATED FILE - DO NOT EDIT

export toggletiplabel

"""
    toggletiplabel(;kwargs...)
    toggletiplabel(children::Any;kwargs...)
    toggletiplabel(children_maker::Function;kwargs...)


A ToggletipLabel component.
ToggletipLabel is a wrapper for the Carbon ToggletipLabel component.
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
- `style` (Dict; optional): style
"""
function toggletiplabel(; kwargs...)
        available_props = Symbol[:children, :id, :as_, :className, :loading_state, :style]
        wild_props = Symbol[]
        return Component("toggletiplabel", "ToggletipLabel", "carbon_dash", available_props, wild_props; kwargs...)
end

toggletiplabel(children::Any; kwargs...) = toggletiplabel(;kwargs..., children = children)
toggletiplabel(children_maker::Function; kwargs...) = toggletiplabel(children_maker(); kwargs...)

