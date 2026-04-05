# AUTO GENERATED FILE - DO NOT EDIT

export tabletoolbar

"""
    tabletoolbar(;kwargs...)
    tabletoolbar(children::Any;kwargs...)
    tabletoolbar(children_maker::Function;kwargs...)


A TableToolbar component.
TableToolbar is a wrapper for the Carbon TableToolbar component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `ariaLabel` (Bool | Real | String | Dict | Array; optional): ariaLabel
- `className` (String; optional): className
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `size` (Bool | Real | String | Dict | Array; optional): size
- `style` (Dict; optional): style
"""
function tabletoolbar(; kwargs...)
        available_props = Symbol[:children, :id, :ariaLabel, :className, :loading_state, :size, :style]
        wild_props = Symbol[]
        return Component("tabletoolbar", "TableToolbar", "carbon_dash", available_props, wild_props; kwargs...)
end

tabletoolbar(children::Any; kwargs...) = tabletoolbar(;kwargs..., children = children)
tabletoolbar(children_maker::Function; kwargs...) = tabletoolbar(children_maker(); kwargs...)

