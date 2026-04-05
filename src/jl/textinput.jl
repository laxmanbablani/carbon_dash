# AUTO GENERATED FILE - DO NOT EDIT

export textinput

"""
    textinput(;kwargs...)
    textinput(children::Any;kwargs...)
    textinput(children_maker::Function;kwargs...)


A TextInput component.
TextInput is a wrapper for the Carbon TextInput component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `ai_label` (Bool; optional): ai_label
- `className` (String; optional): className
- `debounce` (Bool | Real; optional): debounce
- `decorator` (Bool | Real | String | Dict | Array; optional): decorator
- `defaultValue` (Bool | Real | String | Dict | Array; optional): defaultValue
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `enableCounter` (Bool | Real | String | Dict | Array; optional): enableCounter
- `helperText` (Bool | Real | String | Dict | Array; optional): helperText
- `hideLabel` (Bool | Real | String | Dict | Array; optional): hideLabel
- `inline` (Bool | Real | String | Dict | Array; optional): inline
- `invalid` (Bool | Real | String | Dict | Array; optional): invalid
- `invalidText` (Bool | Real | String | Dict | Array; optional): invalidText
- `label` (String; optional): label
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
- `size` (Bool | Real | String | Dict | Array; optional): size
- `slug` (Bool | Real | String | Dict | Array; optional): slug
- `style` (Dict; optional): style
- `type` (Bool | Real | String | Dict | Array; optional): type
- `value` (String; optional): value
- `warn` (Bool | Real | String | Dict | Array; optional): warn
- `warnText` (Bool | Real | String | Dict | Array; optional): warnText
"""
function textinput(; kwargs...)
        available_props = Symbol[:children, :id, :ai_label, :className, :debounce, :decorator, :defaultValue, :disabled, :enableCounter, :helperText, :hideLabel, :inline, :invalid, :invalidText, :label, :labelText, :light, :loading_state, :maxCount, :n_blur, :n_submit, :onChange, :onClick, :persisted_props, :persistence, :persistence_type, :placeholder, :readOnly, :size, :slug, :style, :type, :value, :warn, :warnText]
        wild_props = Symbol[]
        return Component("textinput", "TextInput", "carbon_dash", available_props, wild_props; kwargs...)
end

textinput(children::Any; kwargs...) = textinput(;kwargs..., children = children)
textinput(children_maker::Function; kwargs...) = textinput(children_maker(); kwargs...)

