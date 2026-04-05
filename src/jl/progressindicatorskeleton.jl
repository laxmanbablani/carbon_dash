# AUTO GENERATED FILE - DO NOT EDIT

export progressindicatorskeleton

"""
    progressindicatorskeleton(;kwargs...)
    progressindicatorskeleton(children::Any;kwargs...)
    progressindicatorskeleton(children_maker::Function;kwargs...)


A ProgressIndicatorSkeleton component.
ProgressIndicatorSkeleton is a wrapper for the Carbon ProgressIndicatorSkeleton component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `style` (Dict; optional): style
- `vertical` (Bool | Real | String | Dict | Array; optional): vertical
"""
function progressindicatorskeleton(; kwargs...)
        available_props = Symbol[:children, :id, :className, :loading_state, :style, :vertical]
        wild_props = Symbol[]
        return Component("progressindicatorskeleton", "ProgressIndicatorSkeleton", "carbon_dash", available_props, wild_props; kwargs...)
end

progressindicatorskeleton(children::Any; kwargs...) = progressindicatorskeleton(;kwargs..., children = children)
progressindicatorskeleton(children_maker::Function; kwargs...) = progressindicatorskeleton(children_maker(); kwargs...)

