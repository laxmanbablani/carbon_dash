# AUTO GENERATED FILE - DO NOT EDIT

export heading

"""
    heading(;kwargs...)
    heading(children::Any;kwargs...)
    heading(children_maker::Function;kwargs...)


A Heading component.
Heading is a wrapper for the Carbon Heading component.
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
function heading(; kwargs...)
        available_props = Symbol[:children, :id, :className, :loading_state, :style]
        wild_props = Symbol[]
        return Component("heading", "Heading", "carbon_dash", available_props, wild_props; kwargs...)
end

heading(children::Any; kwargs...) = heading(;kwargs..., children = children)
heading(children_maker::Function; kwargs...) = heading(children_maker(); kwargs...)

