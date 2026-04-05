# AUTO GENERATED FILE - DO NOT EDIT

export formlabel

"""
    formlabel(;kwargs...)
    formlabel(children::Any;kwargs...)
    formlabel(children_maker::Function;kwargs...)


A FormLabel component.
FormLabel is a wrapper for the Carbon FormLabel component.
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
function formlabel(; kwargs...)
        available_props = Symbol[:children, :id, :className, :loading_state, :style]
        wild_props = Symbol[]
        return Component("formlabel", "FormLabel", "carbon_dash", available_props, wild_props; kwargs...)
end

formlabel(children::Any; kwargs...) = formlabel(;kwargs..., children = children)
formlabel(children_maker::Function; kwargs...) = formlabel(children_maker(); kwargs...)

