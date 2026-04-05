# AUTO GENERATED FILE - DO NOT EDIT

export tablist

"""
    tablist(;kwargs...)
    tablist(children::Any;kwargs...)
    tablist(children_maker::Function;kwargs...)


A TabList component.
TabList is a wrapper for the Carbon TabList component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `activation` (Bool | Real | String | Dict | Array; optional): activation
- `className` (String; optional): className
- `contained` (Bool; optional): contained
- `fullWidth` (Bool | Real | String | Dict | Array; optional): fullWidth
- `iconSize` (Bool | Real | String | Dict | Array; optional): iconSize
- `leftOverflowButtonProps` (Bool | Real | String | Dict | Array; optional): leftOverflowButtonProps
- `light` (Bool | Real | String | Dict | Array; optional): light
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `rightOverflowButtonProps` (Bool | Real | String | Dict | Array; optional): rightOverflowButtonProps
- `scrollDebounceWait` (Bool | Real | String | Dict | Array; optional): scrollDebounceWait
- `scrollIntoView` (Bool | Real | String | Dict | Array; optional): scrollIntoView
- `style` (Dict; optional): style
"""
function tablist(; kwargs...)
        available_props = Symbol[:children, :id, :activation, :className, :contained, :fullWidth, :iconSize, :leftOverflowButtonProps, :light, :loading_state, :rightOverflowButtonProps, :scrollDebounceWait, :scrollIntoView, :style]
        wild_props = Symbol[]
        return Component("tablist", "TabList", "carbon_dash", available_props, wild_props; kwargs...)
end

tablist(children::Any; kwargs...) = tablist(;kwargs..., children = children)
tablist(children_maker::Function; kwargs...) = tablist(children_maker(); kwargs...)

