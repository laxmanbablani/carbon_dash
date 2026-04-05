# AUTO GENERATED FILE - DO NOT EDIT

export content

"""
    content(;kwargs...)
    content(children::Any;kwargs...)
    content(children_maker::Function;kwargs...)


A Content component.
Content is a wrapper for the Carbon Content component.
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
- `tagName` (Bool | Real | String | Dict | Array; optional): tagName
"""
function content(; kwargs...)
        available_props = Symbol[:children, :id, :className, :loading_state, :style, :tagName]
        wild_props = Symbol[]
        return Component("content", "Content", "carbon_dash", available_props, wild_props; kwargs...)
end

content(children::Any; kwargs...) = content(;kwargs..., children = children)
content(children_maker::Function; kwargs...) = content(children_maker(); kwargs...)

