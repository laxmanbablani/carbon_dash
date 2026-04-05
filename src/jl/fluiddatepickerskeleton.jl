# AUTO GENERATED FILE - DO NOT EDIT

export fluiddatepickerskeleton

"""
    fluiddatepickerskeleton(;kwargs...)
    fluiddatepickerskeleton(children::Any;kwargs...)
    fluiddatepickerskeleton(children_maker::Function;kwargs...)


A FluidDatePickerSkeleton component.
FluidDatePickerSkeleton is a wrapper for the Carbon FluidDatePickerSkeleton component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `datePickerType` (Bool | Real | String | Dict | Array; optional): datePickerType
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `style` (Dict; optional): style
"""
function fluiddatepickerskeleton(; kwargs...)
        available_props = Symbol[:children, :id, :className, :datePickerType, :loading_state, :style]
        wild_props = Symbol[]
        return Component("fluiddatepickerskeleton", "FluidDatePickerSkeleton", "carbon_dash", available_props, wild_props; kwargs...)
end

fluiddatepickerskeleton(children::Any; kwargs...) = fluiddatepickerskeleton(;kwargs..., children = children)
fluiddatepickerskeleton(children_maker::Function; kwargs...) = fluiddatepickerskeleton(children_maker(); kwargs...)

