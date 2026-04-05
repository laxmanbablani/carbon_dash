# AUTO GENERATED FILE - DO NOT EDIT

export tablebody

"""
    tablebody(;kwargs...)
    tablebody(children::Any;kwargs...)
    tablebody(children_maker::Function;kwargs...)


A TableBody component.
TableBody is a wrapper for the Carbon TableBody component.
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
function tablebody(; kwargs...)
        available_props = Symbol[:children, :id, :className, :loading_state, :style]
        wild_props = Symbol[]
        return Component("tablebody", "TableBody", "carbon_dash", available_props, wild_props; kwargs...)
end

tablebody(children::Any; kwargs...) = tablebody(;kwargs..., children = children)
tablebody(children_maker::Function; kwargs...) = tablebody(children_maker(); kwargs...)

