# AUTO GENERATED FILE - DO NOT EDIT

export fluiddatepicker

"""
    fluiddatepicker(;kwargs...)
    fluiddatepicker(children::Any;kwargs...)
    fluiddatepicker(children_maker::Function;kwargs...)


A FluidDatePicker component.
FluidDatePicker is a wrapper for the Carbon FluidDatePicker component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `invalid` (Bool | Real | String | Dict | Array; optional): invalid
- `invalidText` (Bool | Real | String | Dict | Array; optional): invalidText
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `readOnly` (Bool | Real | String | Dict | Array; optional): readOnly
- `style` (Dict; optional): style
- `warn` (Bool | Real | String | Dict | Array; optional): warn
- `warnText` (Bool | Real | String | Dict | Array; optional): warnText
"""
function fluiddatepicker(; kwargs...)
        available_props = Symbol[:children, :id, :className, :invalid, :invalidText, :loading_state, :readOnly, :style, :warn, :warnText]
        wild_props = Symbol[]
        return Component("fluiddatepicker", "FluidDatePicker", "carbon_dash", available_props, wild_props; kwargs...)
end

fluiddatepicker(children::Any; kwargs...) = fluiddatepicker(;kwargs..., children = children)
fluiddatepicker(children_maker::Function; kwargs...) = fluiddatepicker(children_maker(); kwargs...)

