# AUTO GENERATED FILE - DO NOT EDIT

export theme

"""
    theme(;kwargs...)
    theme(children::Any;kwargs...)
    theme(children_maker::Function;kwargs...)


A Theme component.
Theme is a wrapper for the Carbon Theme component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `as_` (Bool | Real | String | Dict | Array; optional): as
- `className` (String; optional): className
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `style` (Dict; optional): style
- `theme` (Bool | Real | String | Dict | Array; optional): theme
"""
function theme(; kwargs...)
        available_props = Symbol[:children, :id, :as_, :className, :loading_state, :style, :theme]
        wild_props = Symbol[]
        return Component("theme", "Theme", "carbon_dash", available_props, wild_props; kwargs...)
end

theme(children::Any; kwargs...) = theme(;kwargs..., children = children)
theme(children_maker::Function; kwargs...) = theme(children_maker(); kwargs...)

