# AUTO GENERATED FILE - DO NOT EDIT

export controlledpasswordinput

"""
    controlledpasswordinput(;kwargs...)
    controlledpasswordinput(children::Any;kwargs...)
    controlledpasswordinput(children_maker::Function;kwargs...)


A ControlledPasswordInput component.
ControlledPasswordInput is a wrapper for the Carbon ControlledPasswordInput component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `debounce` (Bool | Real; optional): debounce
- `defaultValue` (Bool | Real | String | Dict | Array; optional): defaultValue
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `helperText` (Bool | Real | String | Dict | Array; optional): helperText
- `hideLabel` (Bool | Real | String | Dict | Array; optional): hideLabel
- `hidePasswordLabel` (Bool | Real | String | Dict | Array; optional): hidePasswordLabel
- `invalid` (Bool | Real | String | Dict | Array; optional): invalid
- `invalidText` (Bool | Real | String | Dict | Array; optional): invalidText
- `labelText` (Bool | Real | String | Dict | Array; optional): labelText
- `light` (Bool | Real | String | Dict | Array; optional): light
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `n_blur` (Real; optional): n_blur
- `n_submit` (Real; optional): n_submit
- `onChange` (Bool | Real | String | Dict | Array; optional): onChange
- `onClick` (Bool | Real | String | Dict | Array; optional): onClick
- `persisted_props` (Array of Strings; optional): persisted_props
- `persistence` (Bool | String | Real; optional): persistence
- `persistence_type` (a value equal to: 'local', 'session', 'memory'; optional): persistence_type
- `placeholder` (Bool | Real | String | Dict | Array; optional): placeholder
- `showPasswordLabel` (Bool | Real | String | Dict | Array; optional): showPasswordLabel
- `size` (Bool | Real | String | Dict | Array; optional): size
- `style` (Dict; optional): style
- `tooltipAlignment` (Bool | Real | String | Dict | Array; optional): tooltipAlignment
- `tooltipPosition` (Bool | Real | String | Dict | Array; optional): tooltipPosition
- `value` (Bool | Real | String | Dict | Array; optional): value
"""
function controlledpasswordinput(; kwargs...)
        available_props = Symbol[:children, :id, :className, :debounce, :defaultValue, :disabled, :helperText, :hideLabel, :hidePasswordLabel, :invalid, :invalidText, :labelText, :light, :loading_state, :n_blur, :n_submit, :onChange, :onClick, :persisted_props, :persistence, :persistence_type, :placeholder, :showPasswordLabel, :size, :style, :tooltipAlignment, :tooltipPosition, :value]
        wild_props = Symbol[]
        return Component("controlledpasswordinput", "ControlledPasswordInput", "carbon_dash", available_props, wild_props; kwargs...)
end

controlledpasswordinput(children::Any; kwargs...) = controlledpasswordinput(;kwargs..., children = children)
controlledpasswordinput(children_maker::Function; kwargs...) = controlledpasswordinput(children_maker(); kwargs...)

