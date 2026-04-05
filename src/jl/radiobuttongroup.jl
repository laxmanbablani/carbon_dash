# AUTO GENERATED FILE - DO NOT EDIT

export radiobuttongroup

"""
    radiobuttongroup(;kwargs...)
    radiobuttongroup(children::Any;kwargs...)
    radiobuttongroup(children_maker::Function;kwargs...)


A RadioButtonGroup component.
RadioButtonGroup is a wrapper for the Carbon RadioButtonGroup component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `decorator` (Bool | Real | String | Dict | Array; optional): decorator
- `defaultSelected` (Bool | Real | String | Dict | Array; optional): defaultSelected
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `helperText` (Bool | Real | String | Dict | Array; optional): helperText
- `invalid` (Bool | Real | String | Dict | Array; optional): invalid
- `invalidText` (Bool | Real | String | Dict | Array; optional): invalidText
- `label` (String; optional): label
- `labelPosition` (Bool | Real | String | Dict | Array; optional): labelPosition
- `legendText` (Bool | Real | String | Dict | Array; optional): legendText
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `name` (Bool | Real | String | Dict | Array; optional): name
- `onChange` (Bool | Real | String | Dict | Array; optional): onChange
- `orientation` (Bool | Real | String | Dict | Array; optional): orientation
- `persisted_props` (Array of Strings; optional): persisted_props
- `persistence` (Bool | String | Real; optional): persistence
- `persistence_type` (a value equal to: 'local', 'session', 'memory'; optional): persistence_type
- `readOnly` (Bool | Real | String | Dict | Array; optional): readOnly
- `required` (Bool | Real | String | Dict | Array; optional): required
- `slug` (Bool | Real | String | Dict | Array; optional): slug
- `style` (Dict; optional): style
- `valueSelected` (Bool | Real | String | Dict | Array; optional): valueSelected
- `warn` (Bool | Real | String | Dict | Array; optional): warn
- `warnText` (Bool | Real | String | Dict | Array; optional): warnText
"""
function radiobuttongroup(; kwargs...)
        available_props = Symbol[:children, :id, :className, :decorator, :defaultSelected, :disabled, :helperText, :invalid, :invalidText, :label, :labelPosition, :legendText, :loading_state, :name, :onChange, :orientation, :persisted_props, :persistence, :persistence_type, :readOnly, :required, :slug, :style, :valueSelected, :warn, :warnText]
        wild_props = Symbol[]
        return Component("radiobuttongroup", "RadioButtonGroup", "carbon_dash", available_props, wild_props; kwargs...)
end

radiobuttongroup(children::Any; kwargs...) = radiobuttongroup(;kwargs..., children = children)
radiobuttongroup(children_maker::Function; kwargs...) = radiobuttongroup(children_maker(); kwargs...)

