# AUTO GENERATED FILE - DO NOT EDIT

export tabletoolbarmenu

"""
    tabletoolbarmenu(;kwargs...)
    tabletoolbarmenu(children::Any;kwargs...)
    tabletoolbarmenu(children_maker::Function;kwargs...)


A TableToolbarMenu component.
TableToolbarMenu is a wrapper for the Carbon TableToolbarMenu component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `iconDescription` (Bool | Real | String | Dict | Array; optional): iconDescription
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `menuOptionsClass` (Bool | Real | String | Dict | Array; optional): menuOptionsClass
- `renderIcon` (Bool | Real | String | Dict | Array; optional): renderIcon
- `style` (Dict; optional): style
"""
function tabletoolbarmenu(; kwargs...)
        available_props = Symbol[:children, :id, :className, :iconDescription, :loading_state, :menuOptionsClass, :renderIcon, :style]
        wild_props = Symbol[]
        return Component("tabletoolbarmenu", "TableToolbarMenu", "carbon_dash", available_props, wild_props; kwargs...)
end

tabletoolbarmenu(children::Any; kwargs...) = tabletoolbarmenu(;kwargs..., children = children)
tabletoolbarmenu(children_maker::Function; kwargs...) = tabletoolbarmenu(children_maker(); kwargs...)

