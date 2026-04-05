# AUTO GENERATED FILE - DO NOT EDIT

export select

"""
    select(;kwargs...)
    select(children::Any;kwargs...)
    select(children_maker::Function;kwargs...)


A Select component.
Select is a wrapper for the Carbon Select component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `decorator` (Bool | Real | String | Dict | Array; optional): decorator
- `defaultValue` (Bool | Real | String | Dict | Array; optional): defaultValue
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
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
- `noLabel` (Bool | Real | String | Dict | Array; optional): noLabel
- `onChange` (Bool | Real | String | Dict | Array; optional): onChange
- `persisted_props` (Array of Strings; optional): persisted_props
- `persistence` (Bool | String | Real; optional): persistence
- `persistence_type` (a value equal to: 'local', 'session', 'memory'; optional): persistence_type
- `readOnly` (Bool | Real | String | Dict | Array; optional): readOnly
- `size` (Bool | Real | String | Dict | Array; optional): size
- `slug` (Bool | Real | String | Dict | Array; optional): slug
- `style` (Dict; optional): style
- `value` (Bool | Real | String | Dict | Array; optional): value
- `warn` (Bool | Real | String | Dict | Array; optional): warn
- `warnText` (Bool | Real | String | Dict | Array; optional): warnText
"""
function select(; kwargs...)
        available_props = Symbol[:children, :id, :className, :decorator, :defaultValue, :disabled, :helperText, :hideLabel, :inline, :invalid, :invalidText, :label, :labelText, :light, :loading_state, :noLabel, :onChange, :persisted_props, :persistence, :persistence_type, :readOnly, :size, :slug, :style, :value, :warn, :warnText]
        wild_props = Symbol[]
        return Component("select", "Select", "carbon_dash", available_props, wild_props; kwargs...)
end

select(children::Any; kwargs...) = select(;kwargs..., children = children)
select(children_maker::Function; kwargs...) = select(children_maker(); kwargs...)

