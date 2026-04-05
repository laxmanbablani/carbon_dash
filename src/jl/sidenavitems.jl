# AUTO GENERATED FILE - DO NOT EDIT

export sidenavitems

"""
    sidenavitems(;kwargs...)
    sidenavitems(children::Any;kwargs...)
    sidenavitems(children_maker::Function;kwargs...)


A SideNavItems component.
SideNavItems is a wrapper for the Carbon SideNavItems component.
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
- `style` (Dict; optional): style
"""
function sidenavitems(; kwargs...)
        available_props = Symbol[:children, :id, :className, :isSideNavExpanded, :loading_state, :style]
        wild_props = Symbol[]
        return Component("sidenavitems", "SideNavItems", "carbon_dash", available_props, wild_props; kwargs...)
end

sidenavitems(children::Any; kwargs...) = sidenavitems(;kwargs..., children = children)
sidenavitems(children_maker::Function; kwargs...) = sidenavitems(children_maker(); kwargs...)

