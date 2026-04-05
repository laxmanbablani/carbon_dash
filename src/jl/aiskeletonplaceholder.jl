# AUTO GENERATED FILE - DO NOT EDIT

export aiskeletonplaceholder

"""
    aiskeletonplaceholder(;kwargs...)
    aiskeletonplaceholder(children::Any;kwargs...)
    aiskeletonplaceholder(children_maker::Function;kwargs...)


An AISkeletonPlaceholder component.
AISkeletonPlaceholder is a wrapper for the Carbon AISkeletonPlaceholder component.
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
function aiskeletonplaceholder(; kwargs...)
        available_props = Symbol[:children, :id, :className, :loading_state, :style]
        wild_props = Symbol[]
        return Component("aiskeletonplaceholder", "AISkeletonPlaceholder", "carbon_dash", available_props, wild_props; kwargs...)
end

aiskeletonplaceholder(children::Any; kwargs...) = aiskeletonplaceholder(;kwargs..., children = children)
aiskeletonplaceholder(children_maker::Function; kwargs...) = aiskeletonplaceholder(children_maker(); kwargs...)

