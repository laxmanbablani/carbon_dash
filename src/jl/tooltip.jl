# AUTO GENERATED FILE - DO NOT EDIT

export tooltip

"""
    tooltip(;kwargs...)
    tooltip(children::Any;kwargs...)
    tooltip(children_maker::Function;kwargs...)


A Tooltip component.
Tooltip is a wrapper for the Carbon Tooltip component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `align` (String; optional): align
- `className` (String; optional): className
- `closeOnActivation` (Bool | Real | String | Dict | Array; optional): closeOnActivation
- `defaultOpen` (Bool; optional): defaultOpen
- `description` (String; optional): description
- `dropShadow` (Bool | Real | String | Dict | Array; optional): dropShadow
- `enterDelayMs` (Bool | Real | String | Dict | Array; optional): enterDelayMs
- `highContrast` (Bool | Real | String | Dict | Array; optional): highContrast
- `label` (Bool | Real | String | Dict | Array; optional): label
- `leaveDelayMs` (Bool | Real | String | Dict | Array; optional): leaveDelayMs
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `style` (Dict; optional): style
"""
function tooltip(; kwargs...)
        available_props = Symbol[:children, :id, :align, :className, :closeOnActivation, :defaultOpen, :description, :dropShadow, :enterDelayMs, :highContrast, :label, :leaveDelayMs, :loading_state, :style]
        wild_props = Symbol[]
        return Component("tooltip", "Tooltip", "carbon_dash", available_props, wild_props; kwargs...)
end

tooltip(children::Any; kwargs...) = tooltip(;kwargs..., children = children)
tooltip(children_maker::Function; kwargs...) = tooltip(children_maker(); kwargs...)

