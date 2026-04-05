# AUTO GENERATED FILE - DO NOT EDIT

export unorderedlist

"""
    unorderedlist(;kwargs...)
    unorderedlist(children::Any;kwargs...)
    unorderedlist(children_maker::Function;kwargs...)


An UnorderedList component.
UnorderedList is a wrapper for the Carbon UnorderedList component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `isExpressive` (Bool | Real | String | Dict | Array; optional): isExpressive
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `nested` (Bool | Real | String | Dict | Array; optional): nested
- `style` (Dict; optional): style
"""
function unorderedlist(; kwargs...)
        available_props = Symbol[:children, :id, :className, :isExpressive, :loading_state, :nested, :style]
        wild_props = Symbol[]
        return Component("unorderedlist", "UnorderedList", "carbon_dash", available_props, wild_props; kwargs...)
end

unorderedlist(children::Any; kwargs...) = unorderedlist(;kwargs..., children = children)
unorderedlist(children_maker::Function; kwargs...) = unorderedlist(children_maker(); kwargs...)

