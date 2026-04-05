# AUTO GENERATED FILE - DO NOT EDIT

export structuredlistcell

"""
    structuredlistcell(;kwargs...)
    structuredlistcell(children::Any;kwargs...)
    structuredlistcell(children_maker::Function;kwargs...)


A StructuredListCell component.
StructuredListCell is a wrapper for the Carbon StructuredListCell component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `head` (Bool | Real | String | Dict | Array; optional): head
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `noWrap` (Bool | Real | String | Dict | Array; optional): noWrap
- `style` (Dict; optional): style
"""
function structuredlistcell(; kwargs...)
        available_props = Symbol[:children, :id, :className, :head, :loading_state, :noWrap, :style]
        wild_props = Symbol[]
        return Component("structuredlistcell", "StructuredListCell", "carbon_dash", available_props, wild_props; kwargs...)
end

structuredlistcell(children::Any; kwargs...) = structuredlistcell(;kwargs..., children = children)
structuredlistcell(children_maker::Function; kwargs...) = structuredlistcell(children_maker(); kwargs...)

