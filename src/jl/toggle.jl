# AUTO GENERATED FILE - DO NOT EDIT

export toggle

"""
    toggle(;kwargs...)
    toggle(children::Any;kwargs...)
    toggle(children_maker::Function;kwargs...)


A Toggle component.
Toggle is a wrapper for the Carbon Toggle component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `defaultToggled` (Bool | Real | String | Dict | Array; optional): defaultToggled
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `hideLabel` (Bool | Real | String | Dict | Array; optional): hideLabel
- `label` (String; optional): label
- `labelA` (Bool | Real | String | Dict | Array; optional): labelA
- `labelB` (Bool | Real | String | Dict | Array; optional): labelB
- `labelText` (Bool | Real | String | Dict | Array; optional): labelText
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `onClick` (Bool | Real | String | Dict | Array; optional): onClick
- `onToggle` (Bool | Real | String | Dict | Array; optional): onToggle
- `persisted_props` (Array of Strings; optional): persisted_props
- `persistence` (Bool | String | Real; optional): persistence
- `persistence_type` (a value equal to: 'local', 'session', 'memory'; optional): persistence_type
- `readOnly` (Bool | Real | String | Dict | Array; optional): readOnly
- `size` (Bool | Real | String | Dict | Array; optional): size
- `style` (Dict; optional): style
- `toggled` (Bool; optional): toggled
"""
function toggle(; kwargs...)
        available_props = Symbol[:children, :id, :className, :defaultToggled, :disabled, :hideLabel, :label, :labelA, :labelB, :labelText, :loading_state, :onClick, :onToggle, :persisted_props, :persistence, :persistence_type, :readOnly, :size, :style, :toggled]
        wild_props = Symbol[]
        return Component("toggle", "Toggle", "carbon_dash", available_props, wild_props; kwargs...)
end

toggle(children::Any; kwargs...) = toggle(;kwargs..., children = children)
toggle(children_maker::Function; kwargs...) = toggle(children_maker(); kwargs...)

