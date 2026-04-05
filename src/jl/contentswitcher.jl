# AUTO GENERATED FILE - DO NOT EDIT

export contentswitcher

"""
    contentswitcher(;kwargs...)
    contentswitcher(children::Any;kwargs...)
    contentswitcher(children_maker::Function;kwargs...)


A ContentSwitcher component.
ContentSwitcher is a wrapper for the Carbon ContentSwitcher component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `light` (Bool | Real | String | Dict | Array; optional): light
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `lowContrast` (Bool | Real | String | Dict | Array; optional): lowContrast
- `onChange` (Bool | Real | String | Dict | Array; optional): onChange
- `selectedIndex` (Bool | Real | String | Dict | Array; optional): selectedIndex
- `selectionMode` (Bool | Real | String | Dict | Array; optional): selectionMode
- `size` (Bool | Real | String | Dict | Array; optional): size
- `style` (Dict; optional): style
"""
function contentswitcher(; kwargs...)
        available_props = Symbol[:children, :id, :className, :light, :loading_state, :lowContrast, :onChange, :selectedIndex, :selectionMode, :size, :style]
        wild_props = Symbol[]
        return Component("contentswitcher", "ContentSwitcher", "carbon_dash", available_props, wild_props; kwargs...)
end

contentswitcher(children::Any; kwargs...) = contentswitcher(;kwargs..., children = children)
contentswitcher(children_maker::Function; kwargs...) = contentswitcher(children_maker(); kwargs...)

