# AUTO GENERATED FILE - DO NOT EDIT

export structuredlistskeleton

"""
    structuredlistskeleton(;kwargs...)
    structuredlistskeleton(children::Any;kwargs...)
    structuredlistskeleton(children_maker::Function;kwargs...)


A StructuredListSkeleton component.
StructuredListSkeleton is a wrapper for the Carbon StructuredListSkeleton component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `rowCount` (Bool | Real | String | Dict | Array; optional): rowCount
- `style` (Dict; optional): style
"""
function structuredlistskeleton(; kwargs...)
        available_props = Symbol[:children, :id, :className, :loading_state, :rowCount, :style]
        wild_props = Symbol[]
        return Component("structuredlistskeleton", "StructuredListSkeleton", "carbon_dash", available_props, wild_props; kwargs...)
end

structuredlistskeleton(children::Any; kwargs...) = structuredlistskeleton(;kwargs..., children = children)
structuredlistskeleton(children_maker::Function; kwargs...) = structuredlistskeleton(children_maker(); kwargs...)

