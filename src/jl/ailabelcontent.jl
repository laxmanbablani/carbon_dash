# AUTO GENERATED FILE - DO NOT EDIT

export ailabelcontent

"""
    ailabelcontent(;kwargs...)
    ailabelcontent(children::Any;kwargs...)
    ailabelcontent(children_maker::Function;kwargs...)


An AILabelContent component.
AILabelContent is a wrapper for the Carbon AILabelContent component.
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
function ailabelcontent(; kwargs...)
        available_props = Symbol[:children, :id, :className, :loading_state, :style]
        wild_props = Symbol[]
        return Component("ailabelcontent", "AILabelContent", "carbon_dash", available_props, wild_props; kwargs...)
end

ailabelcontent(children::Any; kwargs...) = ailabelcontent(;kwargs..., children = children)
ailabelcontent(children_maker::Function; kwargs...) = ailabelcontent(children_maker(); kwargs...)

