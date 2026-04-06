# AUTO GENERATED FILE - DO NOT EDIT

export tabsvertical

"""
    tabsvertical(;kwargs...)
    tabsvertical(children::Any;kwargs...)
    tabsvertical(children_maker::Function;kwargs...)


A TabsVertical component.
TabsVertical is a wrapper for the Carbon TabsVertical component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `defaultSelectedIndex` (Bool | Real | String | Dict | Array; optional): defaultSelectedIndex
- `height` (Bool | Real | String | Dict | Array; optional): height
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `onChange` (Bool | Real | String | Dict | Array; optional): onChange
- `selectedIndex` (Real; optional): selectedIndex
- `style` (Dict; optional): style
"""
function tabsvertical(; kwargs...)
        available_props = Symbol[:children, :id, :className, :defaultSelectedIndex, :height, :loading_state, :onChange, :selectedIndex, :style]
        wild_props = Symbol[]
        return Component("tabsvertical", "TabsVertical", "carbon_dash", available_props, wild_props; kwargs...)
end

tabsvertical(children::Any; kwargs...) = tabsvertical(;kwargs..., children = children)
tabsvertical(children_maker::Function; kwargs...) = tabsvertical(children_maker(); kwargs...)

