# AUTO GENERATED FILE - DO NOT EDIT

export fluiddatepickerinput

"""
    fluiddatepickerinput(;kwargs...)
    fluiddatepickerinput(children::Any;kwargs...)
    fluiddatepickerinput(children_maker::Function;kwargs...)


A FluidDatePickerInput component.
FluidDatePickerInput is a wrapper for the Carbon FluidDatePickerInput component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `datePickerType` (Bool | Real | String | Dict | Array; optional): datePickerType
- `decorator` (Bool | Real | String | Dict | Array; optional): decorator
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `helperText` (Bool | Real | String | Dict | Array; optional): helperText
- `hideLabel` (Bool | Real | String | Dict | Array; optional): hideLabel
- `invalid` (Bool | Real | String | Dict | Array; optional): invalid
- `invalidText` (Bool | Real | String | Dict | Array; optional): invalidText
- `labelText` (Bool | Real | String | Dict | Array; optional): labelText
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `onChange` (Bool | Real | String | Dict | Array; optional): onChange
- `onClick` (Bool | Real | String | Dict | Array; optional): onClick
- `pattern` (Bool | Real | String | Dict | Array; optional): pattern
- `placeholder` (Bool | Real | String | Dict | Array; optional): placeholder
- `readOnly` (Bool | Real | String | Dict | Array; optional): readOnly
- `size` (Bool | Real | String | Dict | Array; optional): size
- `slug` (Bool | Real | String | Dict | Array; optional): slug
- `style` (Dict; optional): style
- `type` (Bool | Real | String | Dict | Array; optional): type
- `warn` (Bool | Real | String | Dict | Array; optional): warn
- `warnText` (Bool | Real | String | Dict | Array; optional): warnText
"""
function fluiddatepickerinput(; kwargs...)
        available_props = Symbol[:children, :id, :className, :datePickerType, :decorator, :disabled, :helperText, :hideLabel, :invalid, :invalidText, :labelText, :loading_state, :onChange, :onClick, :pattern, :placeholder, :readOnly, :size, :slug, :style, :type, :warn, :warnText]
        wild_props = Symbol[]
        return Component("fluiddatepickerinput", "FluidDatePickerInput", "carbon_dash", available_props, wild_props; kwargs...)
end

fluiddatepickerinput(children::Any; kwargs...) = fluiddatepickerinput(;kwargs..., children = children)
fluiddatepickerinput(children_maker::Function; kwargs...) = fluiddatepickerinput(children_maker(); kwargs...)

