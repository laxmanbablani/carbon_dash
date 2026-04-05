# AUTO GENERATED FILE - DO NOT EDIT

export structuredlistbody

"""
    structuredlistbody(;kwargs...)
    structuredlistbody(children::Any;kwargs...)
    structuredlistbody(children_maker::Function;kwargs...)


A StructuredListBody component.
StructuredListBody is a wrapper for the Carbon StructuredListBody component.
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
- `onKeyDown` (Bool | Real | String | Dict | Array; optional): onKeyDown
- `style` (Dict; optional): style
"""
function structuredlistbody(; kwargs...)
        available_props = Symbol[:children, :id, :className, :head, :loading_state, :onKeyDown, :style]
        wild_props = Symbol[]
        return Component("structuredlistbody", "StructuredListBody", "carbon_dash", available_props, wild_props; kwargs...)
end

structuredlistbody(children::Any; kwargs...) = structuredlistbody(;kwargs..., children = children)
structuredlistbody(children_maker::Function; kwargs...) = structuredlistbody(children_maker(); kwargs...)

