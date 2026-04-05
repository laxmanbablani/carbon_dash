# AUTO GENERATED FILE - DO NOT EDIT

export sidenavheader

"""
    sidenavheader(;kwargs...)
    sidenavheader(children::Any;kwargs...)
    sidenavheader(children_maker::Function;kwargs...)


A SideNavHeader component.
SideNavHeader is a wrapper for the Carbon SideNavHeader component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `isSideNavExpanded` (Bool | Real | String | Dict | Array; optional): isSideNavExpanded
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `renderIcon` (Bool | Real | String | Dict | Array; optional): renderIcon
- `style` (Dict; optional): style
"""
function sidenavheader(; kwargs...)
        available_props = Symbol[:children, :id, :className, :isSideNavExpanded, :loading_state, :renderIcon, :style]
        wild_props = Symbol[]
        return Component("sidenavheader", "SideNavHeader", "carbon_dash", available_props, wild_props; kwargs...)
end

sidenavheader(children::Any; kwargs...) = sidenavheader(;kwargs..., children = children)
sidenavheader(children_maker::Function; kwargs...) = sidenavheader(children_maker(); kwargs...)

