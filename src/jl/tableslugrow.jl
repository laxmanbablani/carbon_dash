# AUTO GENERATED FILE - DO NOT EDIT

export tableslugrow

"""
    tableslugrow(;kwargs...)
    tableslugrow(children::Any;kwargs...)
    tableslugrow(children_maker::Function;kwargs...)


A TableSlugRow component.
TableSlugRow is a wrapper for the Carbon TableSlugRow component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `slug` (Bool | Real | String | Dict | Array; optional): slug
- `style` (Dict; optional): style
"""
function tableslugrow(; kwargs...)
        available_props = Symbol[:children, :id, :className, :loading_state, :slug, :style]
        wild_props = Symbol[]
        return Component("tableslugrow", "TableSlugRow", "carbon_dash", available_props, wild_props; kwargs...)
end

tableslugrow(children::Any; kwargs...) = tableslugrow(;kwargs..., children = children)
tableslugrow(children_maker::Function; kwargs...) = tableslugrow(children_maker(); kwargs...)

