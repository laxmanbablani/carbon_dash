# AUTO GENERATED FILE - DO NOT EDIT

export containedlistitem

"""
    containedlistitem(;kwargs...)
    containedlistitem(children::Any;kwargs...)
    containedlistitem(children_maker::Function;kwargs...)


A ContainedListItem component.
ContainedListItem is a wrapper for the Carbon ContainedListItem component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `action` (Bool | Real | String | Dict | Array; optional): action
- `className` (String; optional): className
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `onClick` (Bool | Real | String | Dict | Array; optional): onClick
- `renderIcon` (Bool | Real | String | Dict | Array; optional): renderIcon
- `style` (Dict; optional): style
"""
function containedlistitem(; kwargs...)
        available_props = Symbol[:children, :id, :action, :className, :disabled, :loading_state, :onClick, :renderIcon, :style]
        wild_props = Symbol[]
        return Component("containedlistitem", "ContainedListItem", "carbon_dash", available_props, wild_props; kwargs...)
end

containedlistitem(children::Any; kwargs...) = containedlistitem(;kwargs..., children = children)
containedlistitem(children_maker::Function; kwargs...) = containedlistitem(children_maker(); kwargs...)

