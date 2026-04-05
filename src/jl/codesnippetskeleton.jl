# AUTO GENERATED FILE - DO NOT EDIT

export codesnippetskeleton

"""
    codesnippetskeleton(;kwargs...)
    codesnippetskeleton(children::Any;kwargs...)
    codesnippetskeleton(children_maker::Function;kwargs...)


A CodeSnippetSkeleton component.
CodeSnippetSkeleton is a wrapper for the Carbon CodeSnippetSkeleton component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `style` (Dict; optional): style
- `type` (Bool | Real | String | Dict | Array; optional): type
"""
function codesnippetskeleton(; kwargs...)
        available_props = Symbol[:children, :id, :className, :loading_state, :style, :type]
        wild_props = Symbol[]
        return Component("codesnippetskeleton", "CodeSnippetSkeleton", "carbon_dash", available_props, wild_props; kwargs...)
end

codesnippetskeleton(children::Any; kwargs...) = codesnippetskeleton(;kwargs..., children = children)
codesnippetskeleton(children_maker::Function; kwargs...) = codesnippetskeleton(children_maker(); kwargs...)

