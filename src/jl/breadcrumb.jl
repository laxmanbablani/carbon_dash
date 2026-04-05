# AUTO GENERATED FILE - DO NOT EDIT

export breadcrumb

"""
    breadcrumb(;kwargs...)
    breadcrumb(children::Any;kwargs...)
    breadcrumb(children_maker::Function;kwargs...)


A Breadcrumb component.
Breadcrumb is a wrapper for the Carbon Breadcrumb component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `noTrailingSlash` (Bool; optional): noTrailingSlash
- `size` (Bool | Real | String | Dict | Array; optional): size
- `style` (Dict; optional): style
"""
function breadcrumb(; kwargs...)
        available_props = Symbol[:children, :id, :className, :loading_state, :noTrailingSlash, :size, :style]
        wild_props = Symbol[]
        return Component("breadcrumb", "Breadcrumb", "carbon_dash", available_props, wild_props; kwargs...)
end

breadcrumb(children::Any; kwargs...) = breadcrumb(;kwargs..., children = children)
breadcrumb(children_maker::Function; kwargs...) = breadcrumb(children_maker(); kwargs...)

