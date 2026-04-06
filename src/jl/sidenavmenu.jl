# AUTO GENERATED FILE - DO NOT EDIT

export sidenavmenu

"""
    sidenavmenu(;kwargs...)
    sidenavmenu(children::Any;kwargs...)
    sidenavmenu(children_maker::Function;kwargs...)


A SideNavMenu component.
SideNavMenu is a wrapper for the Carbon SideNavMenu component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `defaultExpanded` (Bool | Real | String | Dict | Array; optional): defaultExpanded
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
- `title` (Bool | Real | String | Dict | Array; optional): title
"""
function sidenavmenu(; kwargs...)
        available_props = Symbol[:children, :id, :className, :defaultExpanded, :isActive, :isSideNavExpanded, :large, :loading_state, :renderIcon, :style, :tabIndex, :title]
        wild_props = Symbol[]
        return Component("sidenavmenu", "SideNavMenu", "carbon_dash", available_props, wild_props; kwargs...)
end

sidenavmenu(children::Any; kwargs...) = sidenavmenu(;kwargs..., children = children)
sidenavmenu(children_maker::Function; kwargs...) = sidenavmenu(children_maker(); kwargs...)

