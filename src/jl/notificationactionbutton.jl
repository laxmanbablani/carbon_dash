# AUTO GENERATED FILE - DO NOT EDIT

export notificationactionbutton

"""
    notificationactionbutton(;kwargs...)
    notificationactionbutton(children::Any;kwargs...)
    notificationactionbutton(children_maker::Function;kwargs...)


A NotificationActionButton component.
NotificationActionButton is a wrapper for the Carbon NotificationActionButton component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `inline` (Bool | Real | String | Dict | Array; optional): inline
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `onClick` (Bool | Real | String | Dict | Array; optional): onClick
- `style` (Dict; optional): style
"""
function notificationactionbutton(; kwargs...)
        available_props = Symbol[:children, :id, :className, :inline, :loading_state, :onClick, :style]
        wild_props = Symbol[]
        return Component("notificationactionbutton", "NotificationActionButton", "carbon_dash", available_props, wild_props; kwargs...)
end

notificationactionbutton(children::Any; kwargs...) = notificationactionbutton(;kwargs..., children = children)
notificationactionbutton(children_maker::Function; kwargs...) = notificationactionbutton(children_maker(); kwargs...)

