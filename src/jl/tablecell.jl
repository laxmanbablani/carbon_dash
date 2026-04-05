# AUTO GENERATED FILE - DO NOT EDIT

export tablecell

"""
    tablecell(;kwargs...)
    tablecell(children::Any;kwargs...)
    tablecell(children_maker::Function;kwargs...)


A TableCell component.
TableCell is a wrapper for the Carbon TableCell component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `colSpan` (Bool | Real | String | Dict | Array; optional): colSpan
- `hasAILabelHeader` (Bool | Real | String | Dict | Array; optional): hasAILabelHeader
- `headers` (Bool | Real | String | Dict | Array; optional): headers
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `style` (Dict; optional): style
"""
function tablecell(; kwargs...)
        available_props = Symbol[:children, :id, :className, :colSpan, :hasAILabelHeader, :headers, :loading_state, :style]
        wild_props = Symbol[]
        return Component("tablecell", "TableCell", "carbon_dash", available_props, wild_props; kwargs...)
end

tablecell(children::Any; kwargs...) = tablecell(;kwargs..., children = children)
tablecell(children_maker::Function; kwargs...) = tablecell(children_maker(); kwargs...)

