# AUTO GENERATED FILE - DO NOT EDIT

export headermenubutton

"""
    headermenubutton(;kwargs...)
    headermenubutton(children::Any;kwargs...)
    headermenubutton(children_maker::Function;kwargs...)


A HeaderMenuButton component.
HeaderMenuButton is a wrapper for the Carbon HeaderMenuButton component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `isActive` (Bool | Real | String | Dict | Array; optional): isActive
- `isCollapsible` (Bool | Real | String | Dict | Array; optional): isCollapsible
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `onClick` (Bool | Real | String | Dict | Array; optional): onClick
- `style` (Dict; optional): style
"""
function headermenubutton(; kwargs...)
        available_props = Symbol[:children, :id, :className, :isActive, :isCollapsible, :loading_state, :onClick, :style]
        wild_props = Symbol[]
        return Component("headermenubutton", "HeaderMenuButton", "carbon_dash", available_props, wild_props; kwargs...)
end

headermenubutton(children::Any; kwargs...) = headermenubutton(;kwargs..., children = children)
headermenubutton(children_maker::Function; kwargs...) = headermenubutton(children_maker(); kwargs...)

