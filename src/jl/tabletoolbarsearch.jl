# AUTO GENERATED FILE - DO NOT EDIT

export tabletoolbarsearch

"""
    tabletoolbarsearch(;kwargs...)
    tabletoolbarsearch(children::Any;kwargs...)
    tabletoolbarsearch(children_maker::Function;kwargs...)


A TableToolbarSearch component.
TableToolbarSearch is a wrapper for the Carbon TableToolbarSearch component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `defaultExpanded` (Bool | Real | String | Dict | Array; optional): defaultExpanded
- `defaultValue` (Bool | Real | String | Dict | Array; optional): defaultValue
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `expanded` (Bool | Real | String | Dict | Array; optional): expanded
- `labelText` (Bool | Real | String | Dict | Array; optional): labelText
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `onBlur` (Bool | Real | String | Dict | Array; optional): onBlur
- `onChange` (Bool | Real | String | Dict | Array; optional): onChange
- `onClear` (Bool | Real | String | Dict | Array; optional): onClear
- `onExpand` (Bool | Real | String | Dict | Array; optional): onExpand
- `onFocus` (Bool | Real | String | Dict | Array; optional): onFocus
- `persistent` (Bool | Real | String | Dict | Array; optional): persistent
- `placeholder` (Bool | Real | String | Dict | Array; optional): placeholder
- `searchContainerClass` (Bool | Real | String | Dict | Array; optional): searchContainerClass
- `size` (Bool | Real | String | Dict | Array; optional): size
- `style` (Dict; optional): style
- `tabIndex` (Bool | Real | String | Dict | Array; optional): tabIndex
- `translateWithId` (Bool | Real | String | Dict | Array; optional): translateWithId
"""
function tabletoolbarsearch(; kwargs...)
        available_props = Symbol[:children, :id, :className, :defaultExpanded, :defaultValue, :disabled, :expanded, :labelText, :loading_state, :onBlur, :onChange, :onClear, :onExpand, :onFocus, :persistent, :placeholder, :searchContainerClass, :size, :style, :tabIndex, :translateWithId]
        wild_props = Symbol[]
        return Component("tabletoolbarsearch", "TableToolbarSearch", "carbon_dash", available_props, wild_props; kwargs...)
end

tabletoolbarsearch(children::Any; kwargs...) = tabletoolbarsearch(;kwargs..., children = children)
tabletoolbarsearch(children_maker::Function; kwargs...) = tabletoolbarsearch(children_maker(); kwargs...)

