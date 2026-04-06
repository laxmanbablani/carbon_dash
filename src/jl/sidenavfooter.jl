# AUTO GENERATED FILE - DO NOT EDIT

export sidenavfooter

"""
    sidenavfooter(;kwargs...)
    sidenavfooter(children::Any;kwargs...)
    sidenavfooter(children_maker::Function;kwargs...)


A SideNavFooter component.
SideNavFooter is a wrapper for the Carbon SideNavFooter component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `assistiveText` (Bool | Real | String | Dict | Array; optional): assistiveText
- `className` (String; optional): className
- `expanded` (Bool; optional): expanded
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `onToggle` (Bool | Real | String | Dict | Array; optional): onToggle
- `style` (Dict; optional): style
"""
function sidenavfooter(; kwargs...)
        available_props = Symbol[:children, :id, :assistiveText, :className, :expanded, :loading_state, :onToggle, :style]
        wild_props = Symbol[]
        return Component("sidenavfooter", "SideNavFooter", "carbon_dash", available_props, wild_props; kwargs...)
end

sidenavfooter(children::Any; kwargs...) = sidenavfooter(;kwargs..., children = children)
sidenavfooter(children_maker::Function; kwargs...) = sidenavfooter(children_maker(); kwargs...)

