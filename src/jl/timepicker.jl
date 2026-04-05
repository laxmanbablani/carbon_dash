# AUTO GENERATED FILE - DO NOT EDIT

export timepicker

"""
    timepicker(;kwargs...)
    timepicker(children::Any;kwargs...)
    timepicker(children_maker::Function;kwargs...)


A TimePicker component.
TimePicker is a wrapper for the Carbon TimePicker component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `debounce` (Bool | Real; optional): debounce
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `hideLabel` (Bool | Real | String | Dict | Array; optional): hideLabel
- `invalid` (Bool | Real | String | Dict | Array; optional): invalid
- `invalidText` (Bool | Real | String | Dict | Array; optional): invalidText
- `labelText` (Bool | Real | String | Dict | Array; optional): labelText
- `light` (Bool | Real | String | Dict | Array; optional): light
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `maxLength` (Bool | Real | String | Dict | Array; optional): maxLength
- `n_blur` (Real; optional): n_blur
- `n_submit` (Real; optional): n_submit
- `onBlur` (Bool | Real | String | Dict | Array; optional): onBlur
- `onChange` (Bool | Real | String | Dict | Array; optional): onChange
- `onClick` (Bool | Real | String | Dict | Array; optional): onClick
- `pattern` (Bool | Real | String | Dict | Array; optional): pattern
- `persisted_props` (Array of Strings; optional): persisted_props
- `persistence` (Bool | String | Real; optional): persistence
- `persistence_type` (a value equal to: 'local', 'session', 'memory'; optional): persistence_type
- `placeholder` (Bool | Real | String | Dict | Array; optional): placeholder
- `readOnly` (Bool | Real | String | Dict | Array; optional): readOnly
- `size` (Bool | Real | String | Dict | Array; optional): size
- `style` (Dict; optional): style
- `type` (Bool | Real | String | Dict | Array; optional): type
- `value` (Bool | Real | String | Dict | Array; optional): value
- `warning` (Bool | Real | String | Dict | Array; optional): warning
- `warningText` (Bool | Real | String | Dict | Array; optional): warningText
"""
function timepicker(; kwargs...)
        available_props = Symbol[:children, :id, :className, :debounce, :disabled, :hideLabel, :invalid, :invalidText, :labelText, :light, :loading_state, :maxLength, :n_blur, :n_submit, :onBlur, :onChange, :onClick, :pattern, :persisted_props, :persistence, :persistence_type, :placeholder, :readOnly, :size, :style, :type, :value, :warning, :warningText]
        wild_props = Symbol[]
        return Component("timepicker", "TimePicker", "carbon_dash", available_props, wild_props; kwargs...)
end

timepicker(children::Any; kwargs...) = timepicker(;kwargs..., children = children)
timepicker(children_maker::Function; kwargs...) = timepicker(children_maker(); kwargs...)

