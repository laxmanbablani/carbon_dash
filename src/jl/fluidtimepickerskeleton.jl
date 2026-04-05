# AUTO GENERATED FILE - DO NOT EDIT

export fluidtimepickerskeleton

"""
    fluidtimepickerskeleton(;kwargs...)
    fluidtimepickerskeleton(children::Any;kwargs...)
    fluidtimepickerskeleton(children_maker::Function;kwargs...)


A FluidTimePickerSkeleton component.
FluidTimePickerSkeleton is a wrapper for the Carbon FluidTimePickerSkeleton component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `isOnlyTwo` (Bool | Real | String | Dict | Array; optional): isOnlyTwo
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `style` (Dict; optional): style
"""
function fluidtimepickerskeleton(; kwargs...)
        available_props = Symbol[:children, :id, :className, :isOnlyTwo, :loading_state, :style]
        wild_props = Symbol[]
        return Component("fluidtimepickerskeleton", "FluidTimePickerSkeleton", "carbon_dash", available_props, wild_props; kwargs...)
end

fluidtimepickerskeleton(children::Any; kwargs...) = fluidtimepickerskeleton(;kwargs..., children = children)
fluidtimepickerskeleton(children_maker::Function; kwargs...) = fluidtimepickerskeleton(children_maker(); kwargs...)

