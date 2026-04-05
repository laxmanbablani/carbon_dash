# AUTO GENERATED FILE - DO NOT EDIT

export gridsettings

"""
    gridsettings(;kwargs...)
    gridsettings(children::Any;kwargs...)
    gridsettings(children_maker::Function;kwargs...)


A GridSettings component.
GridSettings is a wrapper for the Carbon GridSettings component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `mode` (Bool | Real | String | Dict | Array; optional): mode
- `style` (Dict; optional): style
- `subgrid` (Bool | Real | String | Dict | Array; optional): subgrid
"""
function gridsettings(; kwargs...)
        available_props = Symbol[:children, :id, :className, :loading_state, :mode, :style, :subgrid]
        wild_props = Symbol[]
        return Component("gridsettings", "GridSettings", "carbon_dash", available_props, wild_props; kwargs...)
end

gridsettings(children::Any; kwargs...) = gridsettings(;kwargs..., children = children)
gridsettings(children_maker::Function; kwargs...) = gridsettings(children_maker(); kwargs...)

