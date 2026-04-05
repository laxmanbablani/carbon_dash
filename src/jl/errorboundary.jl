# AUTO GENERATED FILE - DO NOT EDIT

export errorboundary

"""
    errorboundary(;kwargs...)
    errorboundary(children::Any;kwargs...)
    errorboundary(children_maker::Function;kwargs...)


An ErrorBoundary component.
ErrorBoundary is a wrapper for the Carbon ErrorBoundary component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `fallback` (Bool | Real | String | Dict | Array; optional): fallback
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `style` (Dict; optional): style
"""
function errorboundary(; kwargs...)
        available_props = Symbol[:children, :id, :className, :fallback, :loading_state, :style]
        wild_props = Symbol[]
        return Component("errorboundary", "ErrorBoundary", "carbon_dash", available_props, wild_props; kwargs...)
end

errorboundary(children::Any; kwargs...) = errorboundary(;kwargs..., children = children)
errorboundary(children_maker::Function; kwargs...) = errorboundary(children_maker(); kwargs...)

