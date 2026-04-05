# AUTO GENERATED FILE - DO NOT EDIT

export classprefix

"""
    classprefix(;kwargs...)
    classprefix(children::Any;kwargs...)
    classprefix(children_maker::Function;kwargs...)


A ClassPrefix component.
ClassPrefix is a wrapper for the Carbon ClassPrefix component.
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
function classprefix(; kwargs...)
        available_props = Symbol[:children, :id, :className, :loading_state, :prefix, :style]
        wild_props = Symbol[]
        return Component("classprefix", "ClassPrefix", "carbon_dash", available_props, wild_props; kwargs...)
end

classprefix(children::Any; kwargs...) = classprefix(;kwargs..., children = children)
classprefix(children_maker::Function; kwargs...) = classprefix(children_maker(); kwargs...)

