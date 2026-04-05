# AUTO GENERATED FILE - DO NOT EDIT

export section

"""
    section(;kwargs...)
    section(children::Any;kwargs...)
    section(children_maker::Function;kwargs...)


A Section component.
Section is a wrapper for the Carbon Section component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `as_` (Bool | Real | String | Dict | Array; optional): as
- `className` (String; optional): className
- `level` (Bool | Real | String | Dict | Array; optional): level
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `style` (Dict; optional): style
"""
function section(; kwargs...)
        available_props = Symbol[:children, :id, :as_, :className, :level, :loading_state, :style]
        wild_props = Symbol[]
        return Component("section", "Section", "carbon_dash", available_props, wild_props; kwargs...)
end

section(children::Any; kwargs...) = section(;kwargs..., children = children)
section(children_maker::Function; kwargs...) = section(children_maker(); kwargs...)

