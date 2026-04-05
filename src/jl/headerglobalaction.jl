# AUTO GENERATED FILE - DO NOT EDIT

export headerglobalaction

"""
    headerglobalaction(;kwargs...)
    headerglobalaction(children::Any;kwargs...)
    headerglobalaction(children_maker::Function;kwargs...)


A HeaderGlobalAction component.
HeaderGlobalAction is a wrapper for the Carbon HeaderGlobalAction component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `isActive` (Bool | Real | String | Dict | Array; optional): isActive
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `onClick` (Bool | Real | String | Dict | Array; optional): onClick
- `style` (Dict; optional): style
- `tooltipAlignment` (Bool | Real | String | Dict | Array; optional): tooltipAlignment
- `tooltipDropShadow` (Bool | Real | String | Dict | Array; optional): tooltipDropShadow
- `tooltipHighContrast` (Bool | Real | String | Dict | Array; optional): tooltipHighContrast
"""
function headerglobalaction(; kwargs...)
        available_props = Symbol[:children, :id, :className, :isActive, :loading_state, :onClick, :style, :tooltipAlignment, :tooltipDropShadow, :tooltipHighContrast]
        wild_props = Symbol[]
        return Component("headerglobalaction", "HeaderGlobalAction", "carbon_dash", available_props, wild_props; kwargs...)
end

headerglobalaction(children::Any; kwargs...) = headerglobalaction(;kwargs..., children = children)
headerglobalaction(children_maker::Function; kwargs...) = headerglobalaction(children_maker(); kwargs...)

