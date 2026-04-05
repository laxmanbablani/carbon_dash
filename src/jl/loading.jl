# AUTO GENERATED FILE - DO NOT EDIT

export loading

"""
    loading(;kwargs...)
    loading(children::Any;kwargs...)
    loading(children_maker::Function;kwargs...)


A Loading component.
Loading is a wrapper for the Carbon Loading component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `active` (Bool; optional): active
- `className` (String; optional): className
- `description` (Bool | Real | String | Dict | Array; optional): description
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `small` (Bool; optional): small
- `style` (Dict; optional): style
- `withOverlay` (Bool; optional): withOverlay
"""
function loading(; kwargs...)
        available_props = Symbol[:children, :id, :active, :className, :description, :loading_state, :small, :style, :withOverlay]
        wild_props = Symbol[]
        return Component("loading", "Loading", "carbon_dash", available_props, wild_props; kwargs...)
end

loading(children::Any; kwargs...) = loading(;kwargs..., children = children)
loading(children_maker::Function; kwargs...) = loading(children_maker(); kwargs...)

