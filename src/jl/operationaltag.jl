# AUTO GENERATED FILE - DO NOT EDIT

export operationaltag

"""
    operationaltag(;kwargs...)
    operationaltag(children::Any;kwargs...)
    operationaltag(children_maker::Function;kwargs...)


An OperationalTag component.
OperationalTag is a wrapper for the Carbon OperationalTag component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `renderIcon` (Bool | Real | String | Dict | Array; optional): renderIcon
- `size` (Bool | Real | String | Dict | Array; optional): size
- `style` (Dict; optional): style
- `text` (Bool | Real | String | Dict | Array; optional): text
- `type` (Bool | Real | String | Dict | Array; optional): type
"""
function operationaltag(; kwargs...)
        available_props = Symbol[:children, :id, :className, :disabled, :loading_state, :renderIcon, :size, :style, :text, :type]
        wild_props = Symbol[]
        return Component("operationaltag", "OperationalTag", "carbon_dash", available_props, wild_props; kwargs...)
end

operationaltag(children::Any; kwargs...) = operationaltag(;kwargs..., children = children)
operationaltag(children_maker::Function; kwargs...) = operationaltag(children_maker(); kwargs...)

