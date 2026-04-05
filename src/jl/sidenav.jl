# AUTO GENERATED FILE - DO NOT EDIT

export sidenav

"""
    sidenav(;kwargs...)
    sidenav(children::Any;kwargs...)
    sidenav(children_maker::Function;kwargs...)


A SideNav component.
SideNav is a wrapper for the Carbon SideNav component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `addFocusListeners` (Bool | Real | String | Dict | Array; optional): addFocusListeners
- `addMouseListeners` (Bool | Real | String | Dict | Array; optional): addMouseListeners
- `className` (String; optional): className
- `defaultExpanded` (Bool | Real | String | Dict | Array; optional): defaultExpanded
- `enterDelayMs` (Bool | Real | String | Dict | Array; optional): enterDelayMs
- `expanded` (Bool | Real | String | Dict | Array; optional): expanded
- `href` (Bool | Real | String | Dict | Array; optional): href
- `isChildOfHeader` (Bool | Real | String | Dict | Array; optional): isChildOfHeader
- `isFixedNav` (Bool | Real | String | Dict | Array; optional): isFixedNav
- `isPersistent` (Bool | Real | String | Dict | Array; optional): isPersistent
- `isRail` (Bool | Real | String | Dict | Array; optional): isRail
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `onOverlayClick` (Bool | Real | String | Dict | Array; optional): onOverlayClick
- `onSideNavBlur` (Bool | Real | String | Dict | Array; optional): onSideNavBlur
- `onToggle` (Bool | Real | String | Dict | Array; optional): onToggle
- `style` (Dict; optional): style
"""
function sidenav(; kwargs...)
        available_props = Symbol[:children, :id, :addFocusListeners, :addMouseListeners, :className, :defaultExpanded, :enterDelayMs, :expanded, :href, :isChildOfHeader, :isFixedNav, :isPersistent, :isRail, :loading_state, :onOverlayClick, :onSideNavBlur, :onToggle, :style]
        wild_props = Symbol[]
        return Component("sidenav", "SideNav", "carbon_dash", available_props, wild_props; kwargs...)
end

sidenav(children::Any; kwargs...) = sidenav(;kwargs..., children = children)
sidenav(children_maker::Function; kwargs...) = sidenav(children_maker(); kwargs...)

