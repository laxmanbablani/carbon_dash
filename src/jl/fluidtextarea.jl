# AUTO GENERATED FILE - DO NOT EDIT

export fluidtextarea

"""
    fluidtextarea(;kwargs...)
    fluidtextarea(children::Any;kwargs...)
    fluidtextarea(children_maker::Function;kwargs...)


A FluidTextArea component.
FluidTextArea is a wrapper for the Carbon FluidTextArea component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `cols` (Bool | Real | String | Dict | Array; optional): cols
- `debounce` (Bool | Real; optional): debounce
- `defaultValue` (Bool | Real | String | Dict | Array; optional): defaultValue
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `enableCounter` (Bool | Real | String | Dict | Array; optional): enableCounter
- `helperText` (Bool | Real | String | Dict | Array; optional): helperText
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
- `rows` (Bool | Real | String | Dict | Array; optional): rows
- `style` (Dict; optional): style
- `value` (Bool | Real | String | Dict | Array; optional): value
- `warn` (Bool | Real | String | Dict | Array; optional): warn
- `warnText` (Bool | Real | String | Dict | Array; optional): warnText
"""
function fluidtextarea(; kwargs...)
        available_props = Symbol[:children, :id, :className, :cols, :debounce, :defaultValue, :disabled, :enableCounter, :helperText, :hideLabel, :invalid, :invalidText, :labelText, :light, :loading_state, :maxCount, :n_blur, :n_submit, :onChange, :onClick, :persisted_props, :persistence, :persistence_type, :placeholder, :readOnly, :rows, :style, :value, :warn, :warnText]
        wild_props = Symbol[]
        return Component("fluidtextarea", "FluidTextArea", "carbon_dash", available_props, wild_props; kwargs...)
end

fluidtextarea(children::Any; kwargs...) = fluidtextarea(;kwargs..., children = children)
fluidtextarea(children_maker::Function; kwargs...) = fluidtextarea(children_maker(); kwargs...)

