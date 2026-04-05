# AUTO GENERATED FILE - DO NOT EDIT

export breadcrumbskeleton

"""
    breadcrumbskeleton(;kwargs...)
    breadcrumbskeleton(children::Any;kwargs...)
    breadcrumbskeleton(children_maker::Function;kwargs...)


A BreadcrumbSkeleton component.
BreadcrumbSkeleton is a wrapper for the Carbon BreadcrumbSkeleton component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `items` (Bool | Real | String | Dict | Array; optional): items
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `noTrailingSlash` (Bool | Real | String | Dict | Array; optional): noTrailingSlash
- `size` (Bool | Real | String | Dict | Array; optional): size
- `style` (Dict; optional): style
"""
function breadcrumbskeleton(; kwargs...)
        available_props = Symbol[:children, :id, :className, :items, :loading_state, :noTrailingSlash, :size, :style]
        wild_props = Symbol[]
        return Component("breadcrumbskeleton", "BreadcrumbSkeleton", "carbon_dash", available_props, wild_props; kwargs...)
end

breadcrumbskeleton(children::Any; kwargs...) = breadcrumbskeleton(;kwargs..., children = children)
breadcrumbskeleton(children_maker::Function; kwargs...) = breadcrumbskeleton(children_maker(); kwargs...)

