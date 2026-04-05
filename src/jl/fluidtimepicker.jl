# AUTO GENERATED FILE - DO NOT EDIT

export fluidtimepicker

"""
    fluidtimepicker(;kwargs...)
    fluidtimepicker(children::Any;kwargs...)
    fluidtimepicker(children_maker::Function;kwargs...)


A FluidTimePicker component.
FluidTimePicker is a wrapper for the Carbon FluidTimePicker component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `invalid` (Bool | Real | String | Dict | Array; optional): invalid
- `invalidText` (Bool | Real | String | Dict | Array; optional): invalidText
- `labelText` (Bool | Real | String | Dict | Array; optional): labelText
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
function fluidtimepicker(; kwargs...)
        available_props = Symbol[:children, :id, :className, :disabled, :invalid, :invalidText, :labelText, :loading_state, :readOnly, :style, :warn, :warnText]
        wild_props = Symbol[]
        return Component("fluidtimepicker", "FluidTimePicker", "carbon_dash", available_props, wild_props; kwargs...)
end

fluidtimepicker(children::Any; kwargs...) = fluidtimepicker(;kwargs..., children = children)
fluidtimepicker(children_maker::Function; kwargs...) = fluidtimepicker(children_maker(); kwargs...)

