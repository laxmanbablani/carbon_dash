# AUTO GENERATED FILE - DO NOT EDIT

export clickabletile

"""
    clickabletile(;kwargs...)
    clickabletile(children::Any;kwargs...)
    clickabletile(children_maker::Function;kwargs...)


A ClickableTile component.
ClickableTile is a wrapper for the Carbon ClickableTile component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `clicked` (Bool | Real | String | Dict | Array; optional): clicked
- `decorator` (Bool | Real | String | Dict | Array; optional): decorator
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `hasRoundedCorners` (Bool | Real | String | Dict | Array; optional): hasRoundedCorners
- `href` (Bool | Real | String | Dict | Array; optional): href
- `light` (Bool | Real | String | Dict | Array; optional): light
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `onClick` (Bool | Real | String | Dict | Array; optional): onClick
- `onKeyDown` (Bool | Real | String | Dict | Array; optional): onKeyDown
- `rel` (Bool | Real | String | Dict | Array; optional): rel
- `renderIcon` (a list of or a singular dash component, string or number; optional): renderIcon
- `style` (Dict; optional): style
"""
function clickabletile(; kwargs...)
        available_props = Symbol[:children, :id, :className, :clicked, :decorator, :disabled, :hasRoundedCorners, :href, :light, :loading_state, :onClick, :onKeyDown, :rel, :renderIcon, :style]
        wild_props = Symbol[]
        return Component("clickabletile", "ClickableTile", "carbon_dash", available_props, wild_props; kwargs...)
end

clickabletile(children::Any; kwargs...) = clickabletile(;kwargs..., children = children)
clickabletile(children_maker::Function; kwargs...) = clickabletile(children_maker(); kwargs...)

