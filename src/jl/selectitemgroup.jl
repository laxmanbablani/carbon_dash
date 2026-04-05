# AUTO GENERATED FILE - DO NOT EDIT

export selectitemgroup

"""
    selectitemgroup(;kwargs...)
    selectitemgroup(children::Any;kwargs...)
    selectitemgroup(children_maker::Function;kwargs...)


A SelectItemGroup component.
SelectItemGroup is a wrapper for the Carbon SelectItemGroup component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `label` (Bool | Real | String | Dict | Array; optional): label
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `style` (Dict; optional): style
"""
function selectitemgroup(; kwargs...)
        available_props = Symbol[:children, :id, :className, :disabled, :label, :loading_state, :style]
        wild_props = Symbol[]
        return Component("selectitemgroup", "SelectItemGroup", "carbon_dash", available_props, wild_props; kwargs...)
end

selectitemgroup(children::Any; kwargs...) = selectitemgroup(;kwargs..., children = children)
selectitemgroup(children_maker::Function; kwargs...) = selectitemgroup(children_maker(); kwargs...)

