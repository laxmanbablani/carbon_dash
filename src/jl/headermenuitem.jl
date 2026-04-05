# AUTO GENERATED FILE - DO NOT EDIT

export headermenuitem

"""
    headermenuitem(;kwargs...)
    headermenuitem(children::Any;kwargs...)
    headermenuitem(children_maker::Function;kwargs...)


A HeaderMenuItem component.
HeaderMenuItem is a wrapper for the Carbon HeaderMenuItem component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `as_` (Bool | Real | String | Dict | Array; optional): as
- `className` (String; optional): className
- `element` (Bool | Real | String | Dict | Array; optional): element
- `isActive` (Bool | Real | String | Dict | Array; optional): isActive
- `isCurrentPage` (Bool | Real | String | Dict | Array; optional): isCurrentPage
- `isSideNavExpanded` (Bool | Real | String | Dict | Array; optional): isSideNavExpanded
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `role` (Bool | Real | String | Dict | Array; optional): role
- `style` (Dict; optional): style
- `tabIndex` (Bool | Real | String | Dict | Array; optional): tabIndex
"""
function headermenuitem(; kwargs...)
        available_props = Symbol[:children, :id, :as_, :className, :element, :isActive, :isCurrentPage, :isSideNavExpanded, :loading_state, :role, :style, :tabIndex]
        wild_props = Symbol[]
        return Component("headermenuitem", "HeaderMenuItem", "carbon_dash", available_props, wild_props; kwargs...)
end

headermenuitem(children::Any; kwargs...) = headermenuitem(;kwargs..., children = children)
headermenuitem(children_maker::Function; kwargs...) = headermenuitem(children_maker(); kwargs...)

