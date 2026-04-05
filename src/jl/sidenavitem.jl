# AUTO GENERATED FILE - DO NOT EDIT

export sidenavitem

"""
    sidenavitem(;kwargs...)
    sidenavitem(children::Any;kwargs...)
    sidenavitem(children_maker::Function;kwargs...)


A SideNavItem component.
SideNavItem is a wrapper for the Carbon SideNavItem component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `large` (Bool | Real | String | Dict | Array; optional): large
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `style` (Dict; optional): style
"""
function sidenavitem(; kwargs...)
        available_props = Symbol[:children, :id, :className, :large, :loading_state, :style]
        wild_props = Symbol[]
        return Component("sidenavitem", "SideNavItem", "carbon_dash", available_props, wild_props; kwargs...)
end

sidenavitem(children::Any; kwargs...) = sidenavitem(;kwargs..., children = children)
sidenavitem(children_maker::Function; kwargs...) = sidenavitem(children_maker(); kwargs...)

