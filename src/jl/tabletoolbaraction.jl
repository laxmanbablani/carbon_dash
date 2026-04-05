# AUTO GENERATED FILE - DO NOT EDIT

export tabletoolbaraction

"""
    tabletoolbaraction(;kwargs...)
    tabletoolbaraction(children::Any;kwargs...)
    tabletoolbaraction(children_maker::Function;kwargs...)


A TableToolbarAction component.
TableToolbarAction is a wrapper for the Carbon TableToolbarAction component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `onClick` (Bool | Real | String | Dict | Array; optional): onClick
- `style` (Dict; optional): style
"""
function tabletoolbaraction(; kwargs...)
        available_props = Symbol[:children, :id, :className, :loading_state, :onClick, :style]
        wild_props = Symbol[]
        return Component("tabletoolbaraction", "TableToolbarAction", "carbon_dash", available_props, wild_props; kwargs...)
end

tabletoolbaraction(children::Any; kwargs...) = tabletoolbaraction(;kwargs..., children = children)
tabletoolbaraction(children_maker::Function; kwargs...) = tabletoolbaraction(children_maker(); kwargs...)

