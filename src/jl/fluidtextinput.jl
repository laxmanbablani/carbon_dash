# AUTO GENERATED FILE - DO NOT EDIT

export fluidtextinput

"""
    fluidtextinput(;kwargs...)
    fluidtextinput(children::Any;kwargs...)
    fluidtextinput(children_maker::Function;kwargs...)


A FluidTextInput component.
FluidTextInput is a wrapper for the Carbon FluidTextInput component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `debounce` (Bool | Real; optional): debounce
- `defaultValue` (Bool | Real | String | Dict | Array; optional): defaultValue
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `enableCounter` (Bool | Real | String | Dict | Array; optional): enableCounter
- `invalid` (Bool | Real | String | Dict | Array; optional): invalid
- `invalidText` (Bool | Real | String | Dict | Array; optional): invalidText
- `isPassword` (Bool | Real | String | Dict | Array; optional): isPassword
- `labelText` (Bool | Real | String | Dict | Array; optional): labelText
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `maxCount` (Bool | Real | String | Dict | Array; optional): maxCount
- `n_blur` (Real; optional): n_blur
- `n_submit` (Real; optional): n_submit
- `onChange` (Bool | Real | String | Dict | Array; optional): onChange
- `onClick` (Bool | Real | String | Dict | Array; optional): onClick
- `persisted_props` (Array of Strings; optional): persisted_props
- `persistence` (Bool | String | Real; optional): persistence
- `persistence_type` (a value equal to: 'local', 'session', 'memory'; optional): persistence_type
- `placeholder` (Bool | Real | String | Dict | Array; optional): placeholder
- `readOnly` (Bool | Real | String | Dict | Array; optional): readOnly
- `style` (Dict; optional): style
- `value` (Bool | Real | String | Dict | Array; optional): value
- `warn` (Bool | Real | String | Dict | Array; optional): warn
- `warnText` (Bool | Real | String | Dict | Array; optional): warnText
"""
function fluidtextinput(; kwargs...)
        available_props = Symbol[:children, :id, :className, :debounce, :defaultValue, :disabled, :enableCounter, :invalid, :invalidText, :isPassword, :labelText, :loading_state, :maxCount, :n_blur, :n_submit, :onChange, :onClick, :persisted_props, :persistence, :persistence_type, :placeholder, :readOnly, :style, :value, :warn, :warnText]
        wild_props = Symbol[]
        return Component("fluidtextinput", "FluidTextInput", "carbon_dash", available_props, wild_props; kwargs...)
end

fluidtextinput(children::Any; kwargs...) = fluidtextinput(;kwargs..., children = children)
fluidtextinput(children_maker::Function; kwargs...) = fluidtextinput(children_maker(); kwargs...)

