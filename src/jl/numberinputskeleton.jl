# AUTO GENERATED FILE - DO NOT EDIT

export numberinputskeleton

"""
    numberinputskeleton(;kwargs...)
    numberinputskeleton(children::Any;kwargs...)
    numberinputskeleton(children_maker::Function;kwargs...)


A NumberInputSkeleton component.
NumberInputSkeleton is a wrapper for the Carbon NumberInputSkeleton component.
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
- `size` (Bool | Real | String | Dict | Array; optional): size
- `style` (Dict; optional): style
"""
function numberinputskeleton(; kwargs...)
        available_props = Symbol[:children, :id, :className, :hideLabel, :loading_state, :size, :style]
        wild_props = Symbol[]
        return Component("numberinputskeleton", "NumberInputSkeleton", "carbon_dash", available_props, wild_props; kwargs...)
end

numberinputskeleton(children::Any; kwargs...) = numberinputskeleton(;kwargs..., children = children)
numberinputskeleton(children_maker::Function; kwargs...) = numberinputskeleton(children_maker(); kwargs...)

