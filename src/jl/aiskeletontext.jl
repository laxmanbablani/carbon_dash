# AUTO GENERATED FILE - DO NOT EDIT

export aiskeletontext

"""
    aiskeletontext(;kwargs...)
    aiskeletontext(children::Any;kwargs...)
    aiskeletontext(children_maker::Function;kwargs...)


An AISkeletonText component.
AISkeletonText is a wrapper for the Carbon AISkeletonText component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `heading` (Bool | Real | String | Dict | Array; optional): heading
- `lineCount` (Bool | Real | String | Dict | Array; optional): lineCount
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `paragraph` (Bool | Real | String | Dict | Array; optional): paragraph
- `style` (Dict; optional): style
- `width` (Bool | Real | String | Dict | Array; optional): width
"""
function aiskeletontext(; kwargs...)
        available_props = Symbol[:children, :id, :className, :heading, :lineCount, :loading_state, :paragraph, :style, :width]
        wild_props = Symbol[]
        return Component("aiskeletontext", "AISkeletonText", "carbon_dash", available_props, wild_props; kwargs...)
end

aiskeletontext(children::Any; kwargs...) = aiskeletontext(;kwargs..., children = children)
aiskeletontext(children_maker::Function; kwargs...) = aiskeletontext(children_maker(); kwargs...)

