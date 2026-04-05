# AUTO GENERATED FILE - DO NOT EDIT

export skeletontext

"""
    skeletontext(;kwargs...)
    skeletontext(children::Any;kwargs...)
    skeletontext(children_maker::Function;kwargs...)


A SkeletonText component.
SkeletonText is a wrapper for the Carbon SkeletonText component.
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
function skeletontext(; kwargs...)
        available_props = Symbol[:children, :id, :className, :heading, :lineCount, :loading_state, :paragraph, :style, :width]
        wild_props = Symbol[]
        return Component("skeletontext", "SkeletonText", "carbon_dash", available_props, wild_props; kwargs...)
end

skeletontext(children::Any; kwargs...) = skeletontext(;kwargs..., children = children)
skeletontext(children_maker::Function; kwargs...) = skeletontext(children_maker(); kwargs...)

