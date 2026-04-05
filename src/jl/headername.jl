# AUTO GENERATED FILE - DO NOT EDIT

export headername

"""
    headername(;kwargs...)
    headername(children::Any;kwargs...)
    headername(children_maker::Function;kwargs...)


A HeaderName component.
HeaderName is a wrapper for the Carbon HeaderName component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `as_` (Bool | Real | String | Dict | Array; optional): as
- `className` (String; optional): className
- `element` (Bool | Real | String | Dict | Array; optional): element
- `href` (Bool | Real | String | Dict | Array; optional): href
- `isSideNavExpanded` (Bool | Real | String | Dict | Array; optional): isSideNavExpanded
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `prefix` (Bool | Real | String | Dict | Array; optional): prefix
- `style` (Dict; optional): style
"""
function headername(; kwargs...)
        available_props = Symbol[:children, :id, :as_, :className, :element, :href, :isSideNavExpanded, :loading_state, :prefix, :style]
        wild_props = Symbol[]
        return Component("headername", "HeaderName", "carbon_dash", available_props, wild_props; kwargs...)
end

headername(children::Any; kwargs...) = headername(;kwargs..., children = children)
headername(children_maker::Function; kwargs...) = headername(children_maker(); kwargs...)

