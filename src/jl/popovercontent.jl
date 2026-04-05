# AUTO GENERATED FILE - DO NOT EDIT

export popovercontent

"""
    popovercontent(;kwargs...)
    popovercontent(children::Any;kwargs...)
    popovercontent(children_maker::Function;kwargs...)


A PopoverContent component.
PopoverContent is a wrapper for the Carbon PopoverContent component.
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
function popovercontent(; kwargs...)
        available_props = Symbol[:children, :id, :className, :loading_state, :style]
        wild_props = Symbol[]
        return Component("popovercontent", "PopoverContent", "carbon_dash", available_props, wild_props; kwargs...)
end

popovercontent(children::Any; kwargs...) = popovercontent(;kwargs..., children = children)
popovercontent(children_maker::Function; kwargs...) = popovercontent(children_maker(); kwargs...)

