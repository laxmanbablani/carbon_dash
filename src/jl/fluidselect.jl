# AUTO GENERATED FILE - DO NOT EDIT

export fluidselect

"""
    fluidselect(;kwargs...)
    fluidselect(children::Any;kwargs...)
    fluidselect(children_maker::Function;kwargs...)


A FluidSelect component.
FluidSelect is a wrapper for the Carbon FluidSelect component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `defaultValue` (Bool | Real | String | Dict | Array; optional): defaultValue
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `invalid` (Bool | Real | String | Dict | Array; optional): invalid
- `invalidText` (Bool | Real | String | Dict | Array; optional): invalidText
- `labelText` (Bool | Real | String | Dict | Array; optional): labelText
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `onChange` (Bool | Real | String | Dict | Array; optional): onChange
- `readOnly` (Bool | Real | String | Dict | Array; optional): readOnly
- `style` (Dict; optional): style
- `warn` (Bool | Real | String | Dict | Array; optional): warn
- `warnText` (Bool | Real | String | Dict | Array; optional): warnText
"""
function fluidselect(; kwargs...)
        available_props = Symbol[:children, :id, :className, :defaultValue, :disabled, :invalid, :invalidText, :labelText, :loading_state, :onChange, :readOnly, :style, :warn, :warnText]
        wild_props = Symbol[]
        return Component("fluidselect", "FluidSelect", "carbon_dash", available_props, wild_props; kwargs...)
end

fluidselect(children::Any; kwargs...) = fluidselect(;kwargs..., children = children)
fluidselect(children_maker::Function; kwargs...) = fluidselect(children_maker(); kwargs...)

