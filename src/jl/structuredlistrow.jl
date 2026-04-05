# AUTO GENERATED FILE - DO NOT EDIT

export structuredlistrow

"""
    structuredlistrow(;kwargs...)
    structuredlistrow(children::Any;kwargs...)
    structuredlistrow(children_maker::Function;kwargs...)


A StructuredListRow component.
StructuredListRow is a wrapper for the Carbon StructuredListRow component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `head` (Bool | Real | String | Dict | Array; optional): head
- `label` (Bool | Real | String | Dict | Array; optional): label
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `onClick` (Bool | Real | String | Dict | Array; optional): onClick
- `onKeyDown` (Bool | Real | String | Dict | Array; optional): onKeyDown
- `selection` (Bool | Real | String | Dict | Array; optional): selection
- `style` (Dict; optional): style
"""
function structuredlistrow(; kwargs...)
        available_props = Symbol[:children, :id, :className, :head, :label, :loading_state, :onClick, :onKeyDown, :selection, :style]
        wild_props = Symbol[]
        return Component("structuredlistrow", "StructuredListRow", "carbon_dash", available_props, wild_props; kwargs...)
end

structuredlistrow(children::Any; kwargs...) = structuredlistrow(;kwargs..., children = children)
structuredlistrow(children_maker::Function; kwargs...) = structuredlistrow(children_maker(); kwargs...)

