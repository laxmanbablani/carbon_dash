# AUTO GENERATED FILE - DO NOT EDIT

export checkbox

"""
    checkbox(;kwargs...)
    checkbox(children::Any;kwargs...)
    checkbox(children_maker::Function;kwargs...)


A Checkbox component.
Checkbox is a wrapper for the Carbon Checkbox component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `checked` (Bool; optional): checked
- `className` (String; optional): className
- `debounce` (Bool | Real; optional): debounce
- `decorator` (Bool | Real | String | Dict | Array; optional): decorator
- `defaultChecked` (Bool | Real | String | Dict | Array; optional): defaultChecked
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `helperText` (Bool | Real | String | Dict | Array; optional): helperText
- `hideLabel` (Bool | Real | String | Dict | Array; optional): hideLabel
- `indeterminate` (Bool | Real | String | Dict | Array; optional): indeterminate
- `invalid` (Bool | Real | String | Dict | Array; optional): invalid
- `invalidText` (Bool | Real | String | Dict | Array; optional): invalidText
- `label` (String; optional): label
- `labelText` (Bool | Real | String | Dict | Array; optional): labelText
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `n_blur` (Real; optional): n_blur
- `n_submit` (Real; optional): n_submit
- `onChange` (Bool | Real | String | Dict | Array; optional): onChange
- `persisted_props` (Array of Strings; optional): persisted_props
- `persistence` (Bool | String | Real; optional): persistence
- `persistence_type` (a value equal to: 'local', 'session', 'memory'; optional): persistence_type
- `readOnly` (Bool | Real | String | Dict | Array; optional): readOnly
- `slug` (Bool | Real | String | Dict | Array; optional): slug
- `style` (Dict; optional): style
- `title` (Bool | Real | String | Dict | Array; optional): title
- `warn` (Bool | Real | String | Dict | Array; optional): warn
- `warnText` (Bool | Real | String | Dict | Array; optional): warnText
"""
function checkbox(; kwargs...)
        available_props = Symbol[:children, :id, :checked, :className, :debounce, :decorator, :defaultChecked, :disabled, :helperText, :hideLabel, :indeterminate, :invalid, :invalidText, :label, :labelText, :loading_state, :n_blur, :n_submit, :onChange, :persisted_props, :persistence, :persistence_type, :readOnly, :slug, :style, :title, :warn, :warnText]
        wild_props = Symbol[]
        return Component("checkbox", "Checkbox", "carbon_dash", available_props, wild_props; kwargs...)
end

checkbox(children::Any; kwargs...) = checkbox(;kwargs..., children = children)
checkbox(children_maker::Function; kwargs...) = checkbox(children_maker(); kwargs...)

