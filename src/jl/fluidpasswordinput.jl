# AUTO GENERATED FILE - DO NOT EDIT

export fluidpasswordinput

"""
    fluidpasswordinput(;kwargs...)
    fluidpasswordinput(children::Any;kwargs...)
    fluidpasswordinput(children_maker::Function;kwargs...)


A FluidPasswordInput component.
FluidPasswordInput is a wrapper for the Carbon FluidPasswordInput component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `debounce` (Bool | Real; optional): debounce
- `defaultValue` (Bool | Real | String | Dict | Array; optional): defaultValue
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `hidePasswordLabel` (Bool | Real | String | Dict | Array; optional): hidePasswordLabel
- `invalid` (Bool | Real | String | Dict | Array; optional): invalid
- `invalidText` (Bool | Real | String | Dict | Array; optional): invalidText
- `isPassword` (Bool | Real | String | Dict | Array; optional): isPassword
- `labelText` (Bool | Real | String | Dict | Array; optional): labelText
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `n_blur` (Real; optional): n_blur
- `n_submit` (Real; optional): n_submit
- `onChange` (Bool | Real | String | Dict | Array; optional): onChange
- `onClick` (Bool | Real | String | Dict | Array; optional): onClick
- `onTogglePasswordVisibility` (Bool | Real | String | Dict | Array; optional): onTogglePasswordVisibility
- `persisted_props` (Array of Strings; optional): persisted_props
- `persistence` (Bool | String | Real; optional): persistence
- `persistence_type` (a value equal to: 'local', 'session', 'memory'; optional): persistence_type
- `placeholder` (Bool | Real | String | Dict | Array; optional): placeholder
- `readOnly` (Bool | Real | String | Dict | Array; optional): readOnly
- `showPasswordLabel` (Bool | Real | String | Dict | Array; optional): showPasswordLabel
- `style` (Dict; optional): style
- `value` (Bool | Real | String | Dict | Array; optional): value
- `warn` (Bool | Real | String | Dict | Array; optional): warn
- `warnText` (Bool | Real | String | Dict | Array; optional): warnText
"""
function fluidpasswordinput(; kwargs...)
        available_props = Symbol[:children, :id, :className, :debounce, :defaultValue, :disabled, :hidePasswordLabel, :invalid, :invalidText, :isPassword, :labelText, :loading_state, :n_blur, :n_submit, :onChange, :onClick, :onTogglePasswordVisibility, :persisted_props, :persistence, :persistence_type, :placeholder, :readOnly, :showPasswordLabel, :style, :value, :warn, :warnText]
        wild_props = Symbol[]
        return Component("fluidpasswordinput", "FluidPasswordInput", "carbon_dash", available_props, wild_props; kwargs...)
end

fluidpasswordinput(children::Any; kwargs...) = fluidpasswordinput(;kwargs..., children = children)
fluidpasswordinput(children_maker::Function; kwargs...) = fluidpasswordinput(children_maker(); kwargs...)

