# AUTO GENERATED FILE - DO NOT EDIT

export timepickerselect

"""
    timepickerselect(;kwargs...)
    timepickerselect(children::Any;kwargs...)
    timepickerselect(children_maker::Function;kwargs...)


A TimePickerSelect component.
TimePickerSelect is a wrapper for the Carbon TimePickerSelect component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `defaultValue` (Bool | Real | String | Dict | Array; optional): defaultValue
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `style` (Dict; optional): style
"""
function timepickerselect(; kwargs...)
        available_props = Symbol[:children, :id, :className, :defaultValue, :disabled, :loading_state, :style]
        wild_props = Symbol[]
        return Component("timepickerselect", "TimePickerSelect", "carbon_dash", available_props, wild_props; kwargs...)
end

timepickerselect(children::Any; kwargs...) = timepickerselect(;kwargs..., children = children)
timepickerselect(children_maker::Function; kwargs...) = timepickerselect(children_maker(); kwargs...)

