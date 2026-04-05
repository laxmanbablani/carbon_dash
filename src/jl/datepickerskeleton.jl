# AUTO GENERATED FILE - DO NOT EDIT

export datepickerskeleton

"""
    datepickerskeleton(;kwargs...)
    datepickerskeleton(children::Any;kwargs...)
    datepickerskeleton(children_maker::Function;kwargs...)


A DatePickerSkeleton component.
DatePickerSkeleton is a wrapper for the Carbon DatePickerSkeleton component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `hideLabel` (Bool | Real | String | Dict | Array; optional): hideLabel
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `range` (Bool | Real | String | Dict | Array; optional): range
- `style` (Dict; optional): style
"""
function datepickerskeleton(; kwargs...)
        available_props = Symbol[:children, :id, :className, :hideLabel, :loading_state, :range, :style]
        wild_props = Symbol[]
        return Component("datepickerskeleton", "DatePickerSkeleton", "carbon_dash", available_props, wild_props; kwargs...)
end

datepickerskeleton(children::Any; kwargs...) = datepickerskeleton(;kwargs..., children = children)
datepickerskeleton(children_maker::Function; kwargs...) = datepickerskeleton(children_maker(); kwargs...)

