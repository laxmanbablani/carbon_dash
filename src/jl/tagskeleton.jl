# AUTO GENERATED FILE - DO NOT EDIT

export tagskeleton

"""
    tagskeleton(;kwargs...)
    tagskeleton(children::Any;kwargs...)
    tagskeleton(children_maker::Function;kwargs...)


A TagSkeleton component.
TagSkeleton is a wrapper for the Carbon TagSkeleton component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `size` (Bool | Real | String | Dict | Array; optional): size
- `style` (Dict; optional): style
"""
function tagskeleton(; kwargs...)
        available_props = Symbol[:children, :id, :className, :loading_state, :size, :style]
        wild_props = Symbol[]
        return Component("tagskeleton", "TagSkeleton", "carbon_dash", available_props, wild_props; kwargs...)
end

tagskeleton(children::Any; kwargs...) = tagskeleton(;kwargs..., children = children)
tagskeleton(children_maker::Function; kwargs...) = tagskeleton(children_maker(); kwargs...)

