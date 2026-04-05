# AUTO GENERATED FILE - DO NOT EDIT

export shapeindicator

"""
    shapeindicator(;kwargs...)
    shapeindicator(children::Any;kwargs...)
    shapeindicator(children_maker::Function;kwargs...)


A ShapeIndicator component.
ShapeIndicator is a wrapper for the Carbon ShapeIndicator component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `kind` (Bool | Real | String | Dict | Array; optional): kind
- `label` (Bool | Real | String | Dict | Array; optional): label
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `style` (Dict; optional): style
- `textSize` (Bool | Real | String | Dict | Array; optional): textSize
"""
function shapeindicator(; kwargs...)
        available_props = Symbol[:children, :id, :className, :kind, :label, :loading_state, :style, :textSize]
        wild_props = Symbol[]
        return Component("shapeindicator", "ShapeIndicator", "carbon_dash", available_props, wild_props; kwargs...)
end

shapeindicator(children::Any; kwargs...) = shapeindicator(;kwargs..., children = children)
shapeindicator(children_maker::Function; kwargs...) = shapeindicator(children_maker(); kwargs...)

