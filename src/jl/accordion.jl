# AUTO GENERATED FILE - DO NOT EDIT

export accordion

"""
    accordion(;kwargs...)
    accordion(children::Any;kwargs...)
    accordion(children_maker::Function;kwargs...)


An Accordion component.
Accordion is a wrapper for the Carbon Accordion component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `align` (String; optional): align
- `className` (String; optional): className
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `isFlush` (Bool; optional): isFlush
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `ordered` (Bool | Real | String | Dict | Array; optional): ordered
- `size` (String; optional): size
- `style` (Dict; optional): style
"""
function accordion(; kwargs...)
        available_props = Symbol[:children, :id, :align, :className, :disabled, :isFlush, :loading_state, :ordered, :size, :style]
        wild_props = Symbol[]
        return Component("accordion", "Accordion", "carbon_dash", available_props, wild_props; kwargs...)
end

accordion(children::Any; kwargs...) = accordion(;kwargs..., children = children)
accordion(children_maker::Function; kwargs...) = accordion(children_maker(); kwargs...)

