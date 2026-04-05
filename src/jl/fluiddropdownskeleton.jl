# AUTO GENERATED FILE - DO NOT EDIT

export fluiddropdownskeleton

"""
    fluiddropdownskeleton(;kwargs...)
    fluiddropdownskeleton(children::Any;kwargs...)
    fluiddropdownskeleton(children_maker::Function;kwargs...)


A FluidDropdownSkeleton component.
FluidDropdownSkeleton is a wrapper for the Carbon FluidDropdownSkeleton component.
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
function fluiddropdownskeleton(; kwargs...)
        available_props = Symbol[:children, :id, :className, :loading_state, :style]
        wild_props = Symbol[]
        return Component("fluiddropdownskeleton", "FluidDropdownSkeleton", "carbon_dash", available_props, wild_props; kwargs...)
end

fluiddropdownskeleton(children::Any; kwargs...) = fluiddropdownskeleton(;kwargs..., children = children)
fluiddropdownskeleton(children_maker::Function; kwargs...) = fluiddropdownskeleton(children_maker(); kwargs...)

