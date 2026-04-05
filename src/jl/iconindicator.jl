# AUTO GENERATED FILE - DO NOT EDIT

export iconindicator

"""
    iconindicator(;kwargs...)
    iconindicator(children::Any;kwargs...)
    iconindicator(children_maker::Function;kwargs...)


An IconIndicator component.
IconIndicator is a wrapper for the Carbon IconIndicator component.
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
- `size` (Bool | Real | String | Dict | Array; optional): size
- `style` (Dict; optional): style
"""
function iconindicator(; kwargs...)
        available_props = Symbol[:children, :id, :className, :kind, :label, :loading_state, :size, :style]
        wild_props = Symbol[]
        return Component("iconindicator", "IconIndicator", "carbon_dash", available_props, wild_props; kwargs...)
end

iconindicator(children::Any; kwargs...) = iconindicator(;kwargs..., children = children)
iconindicator(children_maker::Function; kwargs...) = iconindicator(children_maker(); kwargs...)

