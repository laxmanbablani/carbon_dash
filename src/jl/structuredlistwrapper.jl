# AUTO GENERATED FILE - DO NOT EDIT

export structuredlistwrapper

"""
    structuredlistwrapper(;kwargs...)
    structuredlistwrapper(children::Any;kwargs...)
    structuredlistwrapper(children_maker::Function;kwargs...)


A StructuredListWrapper component.
StructuredListWrapper is a wrapper for the Carbon StructuredListWrapper component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `ariaLabel` (Bool | Real | String | Dict | Array; optional): ariaLabel
- `className` (String; optional): className
- `isCondensed` (Bool | Real | String | Dict | Array; optional): isCondensed
- `isFlush` (Bool | Real | String | Dict | Array; optional): isFlush
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `selectedInitialRow` (Bool | Real | String | Dict | Array; optional): selectedInitialRow
- `selection` (Bool | Real | String | Dict | Array; optional): selection
- `style` (Dict; optional): style
"""
function structuredlistwrapper(; kwargs...)
        available_props = Symbol[:children, :id, :ariaLabel, :className, :isCondensed, :isFlush, :loading_state, :selectedInitialRow, :selection, :style]
        wild_props = Symbol[]
        return Component("structuredlistwrapper", "StructuredListWrapper", "carbon_dash", available_props, wild_props; kwargs...)
end

structuredlistwrapper(children::Any; kwargs...) = structuredlistwrapper(;kwargs..., children = children)
structuredlistwrapper(children_maker::Function; kwargs...) = structuredlistwrapper(children_maker(); kwargs...)

