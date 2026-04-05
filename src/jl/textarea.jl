# AUTO GENERATED FILE - DO NOT EDIT

export textarea

"""
    textarea(;kwargs...)
    textarea(children::Any;kwargs...)
    textarea(children_maker::Function;kwargs...)


A TextArea component.
TextArea is a wrapper for the Carbon TextArea component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `cols` (Bool | Real | String | Dict | Array; optional): cols
- `counterMode` (Bool | Real | String | Dict | Array; optional): counterMode
- `debounce` (Bool | Real; optional): debounce
- `decorator` (Bool | Real | String | Dict | Array; optional): decorator
- `defaultValue` (Bool | Real | String | Dict | Array; optional): defaultValue
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `enableCounter` (Bool | Real | String | Dict | Array; optional): enableCounter
- `helperText` (Bool | Real | String | Dict | Array; optional): helperText
- `hideLabel` (Bool | Real | String | Dict | Array; optional): hideLabel
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
- `onKeyDown` (Bool | Real | String | Dict | Array; optional): onKeyDown
- `persisted_props` (Array of Strings; optional): persisted_props
- `persistence` (Bool | String | Real; optional): persistence
- `persistence_type` (a value equal to: 'local', 'session', 'memory'; optional): persistence_type
- `placeholder` (Bool | Real | String | Dict | Array; optional): placeholder
- `readOnly` (Bool | Real | String | Dict | Array; optional): readOnly
- `rows` (Bool | Real | String | Dict | Array; optional): rows
- `slug` (Bool | Real | String | Dict | Array; optional): slug
- `style` (Dict; optional): style
- `value` (String; optional): value
- `warn` (Bool | Real | String | Dict | Array; optional): warn
- `warnText` (Bool | Real | String | Dict | Array; optional): warnText
"""
function textarea(; kwargs...)
        available_props = Symbol[:children, :id, :className, :cols, :counterMode, :debounce, :decorator, :defaultValue, :disabled, :enableCounter, :helperText, :hideLabel, :invalid, :invalidText, :label, :labelText, :light, :loading_state, :maxCount, :n_blur, :n_submit, :onChange, :onClick, :onKeyDown, :persisted_props, :persistence, :persistence_type, :placeholder, :readOnly, :rows, :slug, :style, :value, :warn, :warnText]
        wild_props = Symbol[]
        return Component("textarea", "TextArea", "carbon_dash", available_props, wild_props; kwargs...)
end

textarea(children::Any; kwargs...) = textarea(;kwargs..., children = children)
textarea(children_maker::Function; kwargs...) = textarea(children_maker(); kwargs...)

