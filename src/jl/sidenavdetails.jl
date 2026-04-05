# AUTO GENERATED FILE - DO NOT EDIT

export sidenavdetails

"""
    sidenavdetails(;kwargs...)
    sidenavdetails(children::Any;kwargs...)
    sidenavdetails(children_maker::Function;kwargs...)


A SideNavDetails component.
SideNavDetails is a wrapper for the Carbon SideNavDetails component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `style` (Dict; optional): style
- `title` (Bool | Real | String | Dict | Array; optional): title
"""
function sidenavdetails(; kwargs...)
        available_props = Symbol[:children, :id, :className, :loading_state, :style, :title]
        wild_props = Symbol[]
        return Component("sidenavdetails", "SideNavDetails", "carbon_dash", available_props, wild_props; kwargs...)
end

sidenavdetails(children::Any; kwargs...) = sidenavdetails(;kwargs..., children = children)
sidenavdetails(children_maker::Function; kwargs...) = sidenavdetails(children_maker(); kwargs...)

