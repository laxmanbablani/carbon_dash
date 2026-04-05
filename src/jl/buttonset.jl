# AUTO GENERATED FILE - DO NOT EDIT

export buttonset

"""
    buttonset(;kwargs...)
    buttonset(children::Any;kwargs...)
    buttonset(children_maker::Function;kwargs...)


A ButtonSet component.
ButtonSet is a wrapper for the Carbon ButtonSet component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `fluid` (Bool | Real | String | Dict | Array; optional): fluid
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `stacked` (Bool | Real | String | Dict | Array; optional): stacked
- `style` (Dict; optional): style
"""
function buttonset(; kwargs...)
        available_props = Symbol[:children, :id, :className, :fluid, :loading_state, :stacked, :style]
        wild_props = Symbol[]
        return Component("buttonset", "ButtonSet", "carbon_dash", available_props, wild_props; kwargs...)
end

buttonset(children::Any; kwargs...) = buttonset(;kwargs..., children = children)
buttonset(children_maker::Function; kwargs...) = buttonset(children_maker(); kwargs...)

