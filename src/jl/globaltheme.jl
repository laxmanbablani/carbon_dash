# AUTO GENERATED FILE - DO NOT EDIT

export globaltheme

"""
    globaltheme(;kwargs...)
    globaltheme(children::Any;kwargs...)
    globaltheme(children_maker::Function;kwargs...)


A GlobalTheme component.
GlobalTheme is a wrapper for the Carbon GlobalTheme component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `style` (Dict; optional): style
- `theme` (Bool | Real | String | Dict | Array; optional): theme
"""
function globaltheme(; kwargs...)
        available_props = Symbol[:children, :id, :className, :loading_state, :style, :theme]
        wild_props = Symbol[]
        return Component("globaltheme", "GlobalTheme", "carbon_dash", available_props, wild_props; kwargs...)
end

globaltheme(children::Any; kwargs...) = globaltheme(;kwargs..., children = children)
globaltheme(children_maker::Function; kwargs...) = globaltheme(children_maker(); kwargs...)

