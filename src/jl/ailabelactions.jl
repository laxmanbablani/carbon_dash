# AUTO GENERATED FILE - DO NOT EDIT

export ailabelactions

"""
    ailabelactions(;kwargs...)
    ailabelactions(children::Any;kwargs...)
    ailabelactions(children_maker::Function;kwargs...)


An AILabelActions component.
AILabelActions is a wrapper for the Carbon AILabelActions component.
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
function ailabelactions(; kwargs...)
        available_props = Symbol[:children, :id, :className, :loading_state, :style]
        wild_props = Symbol[]
        return Component("ailabelactions", "AILabelActions", "carbon_dash", available_props, wild_props; kwargs...)
end

ailabelactions(children::Any; kwargs...) = ailabelactions(;kwargs..., children = children)
ailabelactions(children_maker::Function; kwargs...) = ailabelactions(children_maker(); kwargs...)

