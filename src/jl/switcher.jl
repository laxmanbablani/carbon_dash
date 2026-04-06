# AUTO GENERATED FILE - DO NOT EDIT

export switcher

"""
    switcher(;kwargs...)
    switcher(children::Any;kwargs...)
    switcher(children_maker::Function;kwargs...)


A Switcher component.
Switcher is a wrapper for the Carbon Switcher component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `expanded` (Bool; optional): expanded
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `style` (Dict; optional): style
"""
function switcher(; kwargs...)
        available_props = Symbol[:children, :id, :className, :expanded, :loading_state, :style]
        wild_props = Symbol[]
        return Component("switcher", "Switcher", "carbon_dash", available_props, wild_props; kwargs...)
end

switcher(children::Any; kwargs...) = switcher(;kwargs..., children = children)
switcher(children_maker::Function; kwargs...) = switcher(children_maker(); kwargs...)

