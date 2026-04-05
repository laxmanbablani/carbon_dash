# AUTO GENERATED FILE - DO NOT EDIT

export sliderskeleton

"""
    sliderskeleton(;kwargs...)
    sliderskeleton(children::Any;kwargs...)
    sliderskeleton(children_maker::Function;kwargs...)


A SliderSkeleton component.
SliderSkeleton is a wrapper for the Carbon SliderSkeleton component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `ariaLabel` (Bool | Real | String | Dict | Array; optional): ariaLabel
- `className` (String; optional): className
- `hideLabel` (Bool | Real | String | Dict | Array; optional): hideLabel
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `style` (Dict; optional): style
- `twoHandles` (Bool | Real | String | Dict | Array; optional): twoHandles
- `unstable_ariaLabelHandleUpper` (Bool | Real | String | Dict | Array; optional): unstable_ariaLabelHandleUpper
"""
function sliderskeleton(; kwargs...)
        available_props = Symbol[:children, :id, :ariaLabel, :className, :hideLabel, :loading_state, :style, :twoHandles, :unstable_ariaLabelHandleUpper]
        wild_props = Symbol[]
        return Component("sliderskeleton", "SliderSkeleton", "carbon_dash", available_props, wild_props; kwargs...)
end

sliderskeleton(children::Any; kwargs...) = sliderskeleton(;kwargs..., children = children)
sliderskeleton(children_maker::Function; kwargs...) = sliderskeleton(children_maker(); kwargs...)

