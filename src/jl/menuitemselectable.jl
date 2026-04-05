# AUTO GENERATED FILE - DO NOT EDIT

export menuitemselectable

"""
    menuitemselectable(;kwargs...)
    menuitemselectable(children::Any;kwargs...)
    menuitemselectable(children_maker::Function;kwargs...)


A MenuItemSelectable component.
MenuItemSelectable is a wrapper for the Carbon MenuItemSelectable component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `defaultSelected` (Bool | Real | String | Dict | Array; optional): defaultSelected
- `label` (Bool | Real | String | Dict | Array; optional): label
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `onChange` (Bool | Real | String | Dict | Array; optional): onChange
- `selected` (Bool | Real | String | Dict | Array; optional): selected
- `style` (Dict; optional): style
"""
function menuitemselectable(; kwargs...)
        available_props = Symbol[:children, :id, :className, :defaultSelected, :label, :loading_state, :onChange, :selected, :style]
        wild_props = Symbol[]
        return Component("menuitemselectable", "MenuItemSelectable", "carbon_dash", available_props, wild_props; kwargs...)
end

menuitemselectable(children::Any; kwargs...) = menuitemselectable(;kwargs..., children = children)
menuitemselectable(children_maker::Function; kwargs...) = menuitemselectable(children_maker(); kwargs...)

