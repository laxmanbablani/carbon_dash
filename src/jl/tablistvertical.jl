# AUTO GENERATED FILE - DO NOT EDIT

export tablistvertical

"""
    tablistvertical(;kwargs...)
    tablistvertical(children::Any;kwargs...)
    tablistvertical(children_maker::Function;kwargs...)


A TabListVertical component.
TabListVertical is a wrapper for the Carbon TabListVertical component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `activation` (Bool | Real | String | Dict | Array; optional): activation
- `className` (String; optional): className
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `style` (Dict; optional): style
"""
function tablistvertical(; kwargs...)
        available_props = Symbol[:children, :id, :activation, :className, :loading_state, :style]
        wild_props = Symbol[]
        return Component("tablistvertical", "TabListVertical", "carbon_dash", available_props, wild_props; kwargs...)
end

tablistvertical(children::Any; kwargs...) = tablistvertical(;kwargs..., children = children)
tablistvertical(children_maker::Function; kwargs...) = tablistvertical(children_maker(); kwargs...)

