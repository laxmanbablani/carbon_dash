# AUTO GENERATED FILE - DO NOT EDIT

export togglesmallskeleton

"""
    togglesmallskeleton(;kwargs...)
    togglesmallskeleton(children::Any;kwargs...)
    togglesmallskeleton(children_maker::Function;kwargs...)


A ToggleSmallSkeleton component.
ToggleSmallSkeleton is a wrapper for the Carbon ToggleSmallSkeleton component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `labelText` (Bool | Real | String | Dict | Array; optional): labelText
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `style` (Dict; optional): style
"""
function togglesmallskeleton(; kwargs...)
        available_props = Symbol[:children, :id, :className, :labelText, :loading_state, :style]
        wild_props = Symbol[]
        return Component("togglesmallskeleton", "ToggleSmallSkeleton", "carbon_dash", available_props, wild_props; kwargs...)
end

togglesmallskeleton(children::Any; kwargs...) = togglesmallskeleton(;kwargs..., children = children)
togglesmallskeleton(children_maker::Function; kwargs...) = togglesmallskeleton(children_maker(); kwargs...)

