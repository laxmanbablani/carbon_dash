# AUTO GENERATED FILE - DO NOT EDIT

export sidenavswitcher

"""
    sidenavswitcher(;kwargs...)
    sidenavswitcher(children::Any;kwargs...)
    sidenavswitcher(children_maker::Function;kwargs...)


A SideNavSwitcher component.
SideNavSwitcher is a wrapper for the Carbon SideNavSwitcher component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `labelText` (Bool | Real | String | Dict | Array; optional): labelText
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `onChange` (Bool | Real | String | Dict | Array; optional): onChange
- `options` (Bool | Real | String | Dict | Array; optional): options
- `style` (Dict; optional): style
"""
function sidenavswitcher(; kwargs...)
        available_props = Symbol[:children, :id, :className, :labelText, :loading_state, :onChange, :options, :style]
        wild_props = Symbol[]
        return Component("sidenavswitcher", "SideNavSwitcher", "carbon_dash", available_props, wild_props; kwargs...)
end

sidenavswitcher(children::Any; kwargs...) = sidenavswitcher(;kwargs..., children = children)
sidenavswitcher(children_maker::Function; kwargs...) = sidenavswitcher(children_maker(); kwargs...)

