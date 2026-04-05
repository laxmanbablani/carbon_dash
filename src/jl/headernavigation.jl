# AUTO GENERATED FILE - DO NOT EDIT

export headernavigation

"""
    headernavigation(;kwargs...)
    headernavigation(children::Any;kwargs...)
    headernavigation(children_maker::Function;kwargs...)


A HeaderNavigation component.
HeaderNavigation is a wrapper for the Carbon HeaderNavigation component.
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
"""
function headernavigation(; kwargs...)
        available_props = Symbol[:children, :id, :className, :loading_state, :style]
        wild_props = Symbol[]
        return Component("headernavigation", "HeaderNavigation", "carbon_dash", available_props, wild_props; kwargs...)
end

headernavigation(children::Any; kwargs...) = headernavigation(;kwargs..., children = children)
headernavigation(children_maker::Function; kwargs...) = headernavigation(children_maker(); kwargs...)

