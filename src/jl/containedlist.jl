# AUTO GENERATED FILE - DO NOT EDIT

export containedlist

"""
    containedlist(;kwargs...)
    containedlist(children::Any;kwargs...)
    containedlist(children_maker::Function;kwargs...)


A ContainedList component.
ContainedList is a wrapper for the Carbon ContainedList component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `action` (Bool | Real | String | Dict | Array; optional): action
- `className` (String; optional): className
- `isInset` (Bool | Real | String | Dict | Array; optional): isInset
- `kind` (Bool | Real | String | Dict | Array; optional): kind
- `label` (Bool | Real | String | Dict | Array; optional): label
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `size` (Bool | Real | String | Dict | Array; optional): size
- `style` (Dict; optional): style
"""
function containedlist(; kwargs...)
        available_props = Symbol[:children, :id, :action, :className, :isInset, :kind, :label, :loading_state, :size, :style]
        wild_props = Symbol[]
        return Component("containedlist", "ContainedList", "carbon_dash", available_props, wild_props; kwargs...)
end

containedlist(children::Any; kwargs...) = containedlist(;kwargs..., children = children)
containedlist(children_maker::Function; kwargs...) = containedlist(children_maker(); kwargs...)

