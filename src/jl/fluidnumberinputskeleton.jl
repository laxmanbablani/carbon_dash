# AUTO GENERATED FILE - DO NOT EDIT

export fluidnumberinputskeleton

"""
    fluidnumberinputskeleton(;kwargs...)
    fluidnumberinputskeleton(children::Any;kwargs...)
    fluidnumberinputskeleton(children_maker::Function;kwargs...)


A FluidNumberInputSkeleton component.
FluidNumberInputSkeleton is a wrapper for the Carbon FluidNumberInputSkeleton component.
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
function fluidnumberinputskeleton(; kwargs...)
        available_props = Symbol[:children, :id, :className, :loading_state, :style]
        wild_props = Symbol[]
        return Component("fluidnumberinputskeleton", "FluidNumberInputSkeleton", "carbon_dash", available_props, wild_props; kwargs...)
end

fluidnumberinputskeleton(children::Any; kwargs...) = fluidnumberinputskeleton(;kwargs..., children = children)
fluidnumberinputskeleton(children_maker::Function; kwargs...) = fluidnumberinputskeleton(children_maker(); kwargs...)

