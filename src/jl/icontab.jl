# AUTO GENERATED FILE - DO NOT EDIT

export icontab

"""
    icontab(;kwargs...)
    icontab(children::Any;kwargs...)
    icontab(children_maker::Function;kwargs...)


An IconTab component.
IconTab is a wrapper for the Carbon IconTab component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `badgeIndicator` (Bool | Real | String | Dict | Array; optional): badgeIndicator
- `className` (String; optional): className
- `defaultOpen` (Bool | Real | String | Dict | Array; optional): defaultOpen
- `enterDelayMs` (Bool | Real | String | Dict | Array; optional): enterDelayMs
- `label` (Bool | Real | String | Dict | Array; optional): label
- `leaveDelayMs` (Bool | Real | String | Dict | Array; optional): leaveDelayMs
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `style` (Dict; optional): style
"""
function icontab(; kwargs...)
        available_props = Symbol[:children, :id, :badgeIndicator, :className, :defaultOpen, :enterDelayMs, :label, :leaveDelayMs, :loading_state, :style]
        wild_props = Symbol[]
        return Component("icontab", "IconTab", "carbon_dash", available_props, wild_props; kwargs...)
end

icontab(children::Any; kwargs...) = icontab(;kwargs..., children = children)
icontab(children_maker::Function; kwargs...) = icontab(children_maker(); kwargs...)

