# AUTO GENERATED FILE - DO NOT EDIT

export orderedlist

"""
    orderedlist(;kwargs...)
    orderedlist(children::Any;kwargs...)
    orderedlist(children_maker::Function;kwargs...)


An OrderedList component.
OrderedList is a wrapper for the Carbon OrderedList component.
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
- `native` (Bool | Real | String | Dict | Array; optional): native
- `nested` (Bool | Real | String | Dict | Array; optional): nested
- `style` (Dict; optional): style
"""
function orderedlist(; kwargs...)
        available_props = Symbol[:children, :id, :className, :isExpressive, :loading_state, :native, :nested, :style]
        wild_props = Symbol[]
        return Component("orderedlist", "OrderedList", "carbon_dash", available_props, wild_props; kwargs...)
end

orderedlist(children::Any; kwargs...) = orderedlist(;kwargs..., children = children)
orderedlist(children_maker::Function; kwargs...) = orderedlist(children_maker(); kwargs...)

