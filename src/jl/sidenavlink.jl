# AUTO GENERATED FILE - DO NOT EDIT

export sidenavlink

"""
    sidenavlink(;kwargs...)
    sidenavlink(children::Any;kwargs...)
    sidenavlink(children_maker::Function;kwargs...)


A SideNavLink component.
SideNavLink is a wrapper for the Carbon SideNavLink component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `as_` (Bool | Real | String | Dict | Array; optional): as
- `className` (String; optional): className
- `element` (Bool | Real | String | Dict | Array; optional): element
- `isActive` (Bool | Real | String | Dict | Array; optional): isActive
- `isSideNavExpanded` (Bool | Real | String | Dict | Array; optional): isSideNavExpanded
- `large` (Bool | Real | String | Dict | Array; optional): large
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `renderIcon` (a list of or a singular dash component, string or number; optional): renderIcon
- `style` (Dict; optional): style
- `tabIndex` (Bool | Real | String | Dict | Array; optional): tabIndex
"""
function sidenavlink(; kwargs...)
        available_props = Symbol[:children, :id, :as_, :className, :element, :isActive, :isSideNavExpanded, :large, :loading_state, :renderIcon, :style, :tabIndex]
        wild_props = Symbol[]
        return Component("sidenavlink", "SideNavLink", "carbon_dash", available_props, wild_props; kwargs...)
end

sidenavlink(children::Any; kwargs...) = sidenavlink(;kwargs..., children = children)
sidenavlink(children_maker::Function; kwargs...) = sidenavlink(children_maker(); kwargs...)

