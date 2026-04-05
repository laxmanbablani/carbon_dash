# AUTO GENERATED FILE - DO NOT EDIT

export menuitemradiogroup

"""
    menuitemradiogroup(;kwargs...)
    menuitemradiogroup(children::Any;kwargs...)
    menuitemradiogroup(children_maker::Function;kwargs...)


A MenuItemRadioGroup component.
MenuItemRadioGroup is a wrapper for the Carbon MenuItemRadioGroup component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `defaultSelectedItem` (Bool | Real | String | Dict | Array; optional): defaultSelectedItem
- `itemToString` (Bool | Real | String | Dict | Array; optional): itemToString
- `items` (Bool | Real | String | Dict | Array; optional): items
- `label` (Bool | Real | String | Dict | Array; optional): label
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `onChange` (Bool | Real | String | Dict | Array; optional): onChange
- `selectedItem` (Bool | Real | String | Dict | Array; optional): selectedItem
- `style` (Dict; optional): style
"""
function menuitemradiogroup(; kwargs...)
        available_props = Symbol[:children, :id, :className, :defaultSelectedItem, :itemToString, :items, :label, :loading_state, :onChange, :selectedItem, :style]
        wild_props = Symbol[]
        return Component("menuitemradiogroup", "MenuItemRadioGroup", "carbon_dash", available_props, wild_props; kwargs...)
end

menuitemradiogroup(children::Any; kwargs...) = menuitemradiogroup(;kwargs..., children = children)
menuitemradiogroup(children_maker::Function; kwargs...) = menuitemradiogroup(children_maker(); kwargs...)

