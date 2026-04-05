# AUTO GENERATED FILE - DO NOT EDIT

export menuitem

"""
    menuitem(;kwargs...)
    menuitem(children::Any;kwargs...)
    menuitem(children_maker::Function;kwargs...)


A MenuItem component.
MenuItem is a wrapper for the Carbon MenuItem component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `dangerDescription` (Bool | Real | String | Dict | Array; optional): dangerDescription
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `kind` (Bool | Real | String | Dict | Array; optional): kind
- `label` (Bool | Real | String | Dict | Array; optional): label
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `onClick` (Bool | Real | String | Dict | Array; optional): onClick
- `renderIcon` (Bool | Real | String | Dict | Array; optional): renderIcon
- `shortcut` (Bool | Real | String | Dict | Array; optional): shortcut
- `style` (Dict; optional): style
"""
function menuitem(; kwargs...)
        available_props = Symbol[:children, :id, :className, :dangerDescription, :disabled, :kind, :label, :loading_state, :onClick, :renderIcon, :shortcut, :style]
        wild_props = Symbol[]
        return Component("menuitem", "MenuItem", "carbon_dash", available_props, wild_props; kwargs...)
end

menuitem(children::Any; kwargs...) = menuitem(;kwargs..., children = children)
menuitem(children_maker::Function; kwargs...) = menuitem(children_maker(); kwargs...)

