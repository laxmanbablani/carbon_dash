# AUTO GENERATED FILE - DO NOT EDIT

export searchskeleton

"""
    searchskeleton(;kwargs...)
    searchskeleton(children::Any;kwargs...)
    searchskeleton(children_maker::Function;kwargs...)


A SearchSkeleton component.
SearchSkeleton is a wrapper for the Carbon SearchSkeleton component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `small` (Bool | Real | String | Dict | Array; optional): small
- `style` (Dict; optional): style
"""
function searchskeleton(; kwargs...)
        available_props = Symbol[:children, :id, :className, :loading_state, :small, :style]
        wild_props = Symbol[]
        return Component("searchskeleton", "SearchSkeleton", "carbon_dash", available_props, wild_props; kwargs...)
end

searchskeleton(children::Any; kwargs...) = searchskeleton(;kwargs..., children = children)
searchskeleton(children_maker::Function; kwargs...) = searchskeleton(children_maker(); kwargs...)

