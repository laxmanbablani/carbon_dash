# AUTO GENERATED FILE - DO NOT EDIT

export fluidtimepickerselect

"""
    fluidtimepickerselect(;kwargs...)
    fluidtimepickerselect(children::Any;kwargs...)
    fluidtimepickerselect(children_maker::Function;kwargs...)


A FluidTimePickerSelect component.
FluidTimePickerSelect is a wrapper for the Carbon FluidTimePickerSelect component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `defaultValue` (Bool | Real | String | Dict | Array; optional): defaultValue
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `labelText` (Bool | Real | String | Dict | Array; optional): labelText
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `onChange` (Bool | Real | String | Dict | Array; optional): onChange
- `style` (Dict; optional): style
"""
function fluidtimepickerselect(; kwargs...)
        available_props = Symbol[:children, :id, :className, :defaultValue, :disabled, :labelText, :loading_state, :onChange, :style]
        wild_props = Symbol[]
        return Component("fluidtimepickerselect", "FluidTimePickerSelect", "carbon_dash", available_props, wild_props; kwargs...)
end

fluidtimepickerselect(children::Any; kwargs...) = fluidtimepickerselect(;kwargs..., children = children)
fluidtimepickerselect(children_maker::Function; kwargs...) = fluidtimepickerselect(children_maker(); kwargs...)

