# AUTO GENERATED FILE - DO NOT EDIT

export headermenu

"""
    headermenu(;kwargs...)
    headermenu(children::Any;kwargs...)
    headermenu(children_maker::Function;kwargs...)


A HeaderMenu component.
HeaderMenu is a wrapper for the Carbon HeaderMenu component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `focusRef` (Bool | Real | String | Dict | Array; optional): focusRef
- `isActive` (Bool | Real | String | Dict | Array; optional): isActive
- `isCurrentPage` (Bool | Real | String | Dict | Array; optional): isCurrentPage
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `menuLinkName` (Bool | Real | String | Dict | Array; optional): menuLinkName
- `onBlur` (Bool | Real | String | Dict | Array; optional): onBlur
- `onClick` (Bool | Real | String | Dict | Array; optional): onClick
- `onKeyDown` (Bool | Real | String | Dict | Array; optional): onKeyDown
- `renderMenuContent` (Bool | Real | String | Dict | Array; optional): renderMenuContent
- `style` (Dict; optional): style
- `tabIndex` (Bool | Real | String | Dict | Array; optional): tabIndex
"""
function headermenu(; kwargs...)
        available_props = Symbol[:children, :id, :className, :focusRef, :isActive, :isCurrentPage, :loading_state, :menuLinkName, :onBlur, :onClick, :onKeyDown, :renderMenuContent, :style, :tabIndex]
        wild_props = Symbol[]
        return Component("headermenu", "HeaderMenu", "carbon_dash", available_props, wild_props; kwargs...)
end

headermenu(children::Any; kwargs...) = headermenu(;kwargs..., children = children)
headermenu(children_maker::Function; kwargs...) = headermenu(children_maker(); kwargs...)

