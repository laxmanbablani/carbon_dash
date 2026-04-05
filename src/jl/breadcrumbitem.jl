# AUTO GENERATED FILE - DO NOT EDIT

export breadcrumbitem

"""
    breadcrumbitem(;kwargs...)
    breadcrumbitem(children::Any;kwargs...)
    breadcrumbitem(children_maker::Function;kwargs...)


A BreadcrumbItem component.
BreadcrumbItem is a wrapper for the Carbon BreadcrumbItem component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `href` (String; optional): href
- `isCurrentPage` (Bool; optional): isCurrentPage
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `style` (Dict; optional): style
"""
function breadcrumbitem(; kwargs...)
        available_props = Symbol[:children, :id, :className, :href, :isCurrentPage, :loading_state, :style]
        wild_props = Symbol[]
        return Component("breadcrumbitem", "BreadcrumbItem", "carbon_dash", available_props, wild_props; kwargs...)
end

breadcrumbitem(children::Any; kwargs...) = breadcrumbitem(;kwargs..., children = children)
breadcrumbitem(children_maker::Function; kwargs...) = breadcrumbitem(children_maker(); kwargs...)

