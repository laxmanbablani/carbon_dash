# AUTO GENERATED FILE - DO NOT EDIT

export errorboundarycontext

"""
    errorboundarycontext(;kwargs...)
    errorboundarycontext(children::Any;kwargs...)
    errorboundarycontext(children_maker::Function;kwargs...)


An ErrorBoundaryContext component.
ErrorBoundaryContext is a wrapper for the Carbon ErrorBoundaryContext component.
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
"""
function errorboundarycontext(; kwargs...)
        available_props = Symbol[:children, :id, :className, :loading_state, :style]
        wild_props = Symbol[]
        return Component("errorboundarycontext", "ErrorBoundaryContext", "carbon_dash", available_props, wild_props; kwargs...)
end

errorboundarycontext(children::Any; kwargs...) = errorboundarycontext(;kwargs..., children = children)
errorboundarycontext(children_maker::Function; kwargs...) = errorboundarycontext(children_maker(); kwargs...)

