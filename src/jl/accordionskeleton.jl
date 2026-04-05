# AUTO GENERATED FILE - DO NOT EDIT

export accordionskeleton

"""
    accordionskeleton(;kwargs...)
    accordionskeleton(children::Any;kwargs...)
    accordionskeleton(children_maker::Function;kwargs...)


An AccordionSkeleton component.
AccordionSkeleton is a wrapper for the Carbon AccordionSkeleton component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `align` (Bool | Real | String | Dict | Array; optional): align
- `className` (String; optional): className
- `count` (Bool | Real | String | Dict | Array; optional): count
- `isFlush` (Bool | Real | String | Dict | Array; optional): isFlush
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `open` (Bool | Real | String | Dict | Array; optional): open
- `ordered` (Bool | Real | String | Dict | Array; optional): ordered
- `style` (Dict; optional): style
"""
function accordionskeleton(; kwargs...)
        available_props = Symbol[:children, :id, :align, :className, :count, :isFlush, :loading_state, :open, :ordered, :style]
        wild_props = Symbol[]
        return Component("accordionskeleton", "AccordionSkeleton", "carbon_dash", available_props, wild_props; kwargs...)
end

accordionskeleton(children::Any; kwargs...) = accordionskeleton(;kwargs..., children = children)
accordionskeleton(children_maker::Function; kwargs...) = accordionskeleton(children_maker(); kwargs...)

