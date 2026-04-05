# AUTO GENERATED FILE - DO NOT EDIT

export idprefix

"""
    idprefix(;kwargs...)
    idprefix(children::Any;kwargs...)
    idprefix(children_maker::Function;kwargs...)


An IdPrefix component.
IdPrefix is a wrapper for the Carbon IdPrefix component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `prefix` (Bool | Real | String | Dict | Array; optional): prefix
- `style` (Dict; optional): style
"""
function idprefix(; kwargs...)
        available_props = Symbol[:children, :id, :className, :loading_state, :prefix, :style]
        wild_props = Symbol[]
        return Component("idprefix", "IdPrefix", "carbon_dash", available_props, wild_props; kwargs...)
end

idprefix(children::Any; kwargs...) = idprefix(;kwargs..., children = children)
idprefix(children_maker::Function; kwargs...) = idprefix(children_maker(); kwargs...)

