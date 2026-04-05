# AUTO GENERATED FILE - DO NOT EDIT

export headercontainer

"""
    headercontainer(;kwargs...)
    headercontainer(children::Any;kwargs...)
    headercontainer(children_maker::Function;kwargs...)


A HeaderContainer component.
HeaderContainer is a wrapper for the Carbon HeaderContainer component.
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
- `render` (Bool | Real | String | Dict | Array; optional): render
- `style` (Dict; optional): style
"""
function headercontainer(; kwargs...)
        available_props = Symbol[:children, :id, :className, :isSideNavExpanded, :loading_state, :render, :style]
        wild_props = Symbol[]
        return Component("headercontainer", "HeaderContainer", "carbon_dash", available_props, wild_props; kwargs...)
end

headercontainer(children::Any; kwargs...) = headercontainer(;kwargs..., children = children)
headercontainer(children_maker::Function; kwargs...) = headercontainer(children_maker(); kwargs...)

