# AUTO GENERATED FILE - DO NOT EDIT

export sidenavmenuitem

"""
    sidenavmenuitem(;kwargs...)
    sidenavmenuitem(children::Any;kwargs...)
    sidenavmenuitem(children_maker::Function;kwargs...)


A SideNavMenuItem component.
SideNavMenuItem is a wrapper for the Carbon SideNavMenuItem component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `as_` (Bool | Real | String | Dict | Array; optional): as
- `className` (String; optional): className
- `href` (Bool | Real | String | Dict | Array; optional): href
- `isActive` (Bool | Real | String | Dict | Array; optional): isActive
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `style` (Dict; optional): style
"""
function sidenavmenuitem(; kwargs...)
        available_props = Symbol[:children, :id, :as_, :className, :href, :isActive, :loading_state, :style]
        wild_props = Symbol[]
        return Component("sidenavmenuitem", "SideNavMenuItem", "carbon_dash", available_props, wild_props; kwargs...)
end

sidenavmenuitem(children::Any; kwargs...) = sidenavmenuitem(;kwargs..., children = children)
sidenavmenuitem(children_maker::Function; kwargs...) = sidenavmenuitem(children_maker(); kwargs...)

