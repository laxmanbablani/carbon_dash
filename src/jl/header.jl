# AUTO GENERATED FILE - DO NOT EDIT

export header

"""
    header(;kwargs...)
    header(children::Any;kwargs...)
    header(children_maker::Function;kwargs...)


A Header component.
Header is a wrapper for the Carbon Header component.
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
function header(; kwargs...)
        available_props = Symbol[:children, :id, :className, :loading_state, :style]
        wild_props = Symbol[]
        return Component("header", "Header", "carbon_dash", available_props, wild_props; kwargs...)
end

header(children::Any; kwargs...) = header(;kwargs..., children = children)
header(children_maker::Function; kwargs...) = header(children_maker(); kwargs...)

