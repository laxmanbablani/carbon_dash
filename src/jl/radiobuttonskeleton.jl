# AUTO GENERATED FILE - DO NOT EDIT

export radiobuttonskeleton

"""
    radiobuttonskeleton(;kwargs...)
    radiobuttonskeleton(children::Any;kwargs...)
    radiobuttonskeleton(children_maker::Function;kwargs...)


A RadioButtonSkeleton component.
RadioButtonSkeleton is a wrapper for the Carbon RadioButtonSkeleton component.
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
"""
function radiobuttonskeleton(; kwargs...)
        available_props = Symbol[:children, :id, :className, :loading_state, :style]
        wild_props = Symbol[]
        return Component("radiobuttonskeleton", "RadioButtonSkeleton", "carbon_dash", available_props, wild_props; kwargs...)
end

radiobuttonskeleton(children::Any; kwargs...) = radiobuttonskeleton(;kwargs..., children = children)
radiobuttonskeleton(children_maker::Function; kwargs...) = radiobuttonskeleton(children_maker(); kwargs...)

