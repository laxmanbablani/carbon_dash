# AUTO GENERATED FILE - DO NOT EDIT

export stack

"""
    stack(;kwargs...)
    stack(children::Any;kwargs...)
    stack(children_maker::Function;kwargs...)


A Stack component.
Stack is a wrapper for the Carbon Stack component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `as_` (Bool | Real | String | Dict | Array; optional): as
- `className` (String; optional): className
- `gap` (Bool | Real | String | Dict | Array; optional): gap
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `orientation` (Bool | Real | String | Dict | Array; optional): orientation
- `style` (Dict; optional): style
"""
function stack(; kwargs...)
        available_props = Symbol[:children, :id, :as_, :className, :gap, :loading_state, :orientation, :style]
        wild_props = Symbol[]
        return Component("stack", "Stack", "carbon_dash", available_props, wild_props; kwargs...)
end

stack(children::Any; kwargs...) = stack(;kwargs..., children = children)
stack(children_maker::Function; kwargs...) = stack(children_maker(); kwargs...)

