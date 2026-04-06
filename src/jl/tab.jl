# AUTO GENERATED FILE - DO NOT EDIT

export tab

"""
    tab(;kwargs...)
    tab(children::Any;kwargs...)
    tab(children_maker::Function;kwargs...)


A Tab component.
Tab is a wrapper for the Carbon Tab component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `as_` (Bool | Real | String | Dict | Array; optional): as
- `className` (String; optional): className
- `disabled` (Bool; optional): disabled
- `label` (a list of or a singular dash component, string or number; optional): label
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `onClick` (Bool | Real | String | Dict | Array; optional): onClick
- `onKeyDown` (Bool | Real | String | Dict | Array; optional): onKeyDown
- `renderButton` (Bool | Real | String | Dict | Array; optional): renderButton
- `renderIcon` (a list of or a singular dash component, string or number; optional): renderIcon
- `secondaryLabel` (Bool | Real | String | Dict | Array; optional): secondaryLabel
- `style` (Dict; optional): style
"""
function tab(; kwargs...)
        available_props = Symbol[:children, :id, :as_, :className, :disabled, :label, :loading_state, :onClick, :onKeyDown, :renderButton, :renderIcon, :secondaryLabel, :style]
        wild_props = Symbol[]
        return Component("tab", "Tab", "carbon_dash", available_props, wild_props; kwargs...)
end

tab(children::Any; kwargs...) = tab(;kwargs..., children = children)
tab(children_maker::Function; kwargs...) = tab(children_maker(); kwargs...)

