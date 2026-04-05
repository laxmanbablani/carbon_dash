# AUTO GENERATED FILE - DO NOT EDIT

export tabsskeleton

"""
    tabsskeleton(;kwargs...)
    tabsskeleton(children::Any;kwargs...)
    tabsskeleton(children_maker::Function;kwargs...)


A TabsSkeleton component.
TabsSkeleton is a wrapper for the Carbon TabsSkeleton component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `contained` (Bool | Real | String | Dict | Array; optional): contained
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `style` (Dict; optional): style
"""
function tabsskeleton(; kwargs...)
        available_props = Symbol[:children, :id, :className, :contained, :loading_state, :style]
        wild_props = Symbol[]
        return Component("tabsskeleton", "TabsSkeleton", "carbon_dash", available_props, wild_props; kwargs...)
end

tabsskeleton(children::Any; kwargs...) = tabsskeleton(;kwargs..., children = children)
tabsskeleton(children_maker::Function; kwargs...) = tabsskeleton(children_maker(); kwargs...)

