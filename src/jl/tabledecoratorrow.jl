# AUTO GENERATED FILE - DO NOT EDIT

export tabledecoratorrow

"""
    tabledecoratorrow(;kwargs...)
    tabledecoratorrow(children::Any;kwargs...)
    tabledecoratorrow(children_maker::Function;kwargs...)


A TableDecoratorRow component.
TableDecoratorRow is a wrapper for the Carbon TableDecoratorRow component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `decorator` (Bool | Real | String | Dict | Array; optional): decorator
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `style` (Dict; optional): style
"""
function tabledecoratorrow(; kwargs...)
        available_props = Symbol[:children, :id, :className, :decorator, :loading_state, :style]
        wild_props = Symbol[]
        return Component("tabledecoratorrow", "TableDecoratorRow", "carbon_dash", available_props, wild_props; kwargs...)
end

tabledecoratorrow(children::Any; kwargs...) = tabledecoratorrow(;kwargs..., children = children)
tabledecoratorrow(children_maker::Function; kwargs...) = tabledecoratorrow(children_maker(); kwargs...)

