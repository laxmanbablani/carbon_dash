# AUTO GENERATED FILE - DO NOT EDIT

export modalpresence

"""
    modalpresence(;kwargs...)
    modalpresence(children::Any;kwargs...)
    modalpresence(children_maker::Function;kwargs...)


A ModalPresence component.
ModalPresence is a wrapper for the Carbon ModalPresence component.
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
"""
function modalpresence(; kwargs...)
        available_props = Symbol[:children, :id, :className, :loading_state, :style]
        wild_props = Symbol[]
        return Component("modalpresence", "ModalPresence", "carbon_dash", available_props, wild_props; kwargs...)
end

modalpresence(children::Any; kwargs...) = modalpresence(;kwargs..., children = children)
modalpresence(children_maker::Function; kwargs...) = modalpresence(children_maker(); kwargs...)

