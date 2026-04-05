# AUTO GENERATED FILE - DO NOT EDIT

export notificationbutton

"""
    notificationbutton(;kwargs...)
    notificationbutton(children::Any;kwargs...)
    notificationbutton(children_maker::Function;kwargs...)


A NotificationButton component.
NotificationButton is a wrapper for the Carbon NotificationButton component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `ariaLabel` (Bool | Real | String | Dict | Array; optional): ariaLabel
- `className` (String; optional): className
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `name` (Bool | Real | String | Dict | Array; optional): name
- `notificationType` (Bool | Real | String | Dict | Array; optional): notificationType
- `renderIcon` (Bool | Real | String | Dict | Array; optional): renderIcon
- `style` (Dict; optional): style
- `type` (Bool | Real | String | Dict | Array; optional): type
"""
function notificationbutton(; kwargs...)
        available_props = Symbol[:children, :id, :ariaLabel, :className, :loading_state, :name, :notificationType, :renderIcon, :style, :type]
        wild_props = Symbol[]
        return Component("notificationbutton", "NotificationButton", "carbon_dash", available_props, wild_props; kwargs...)
end

notificationbutton(children::Any; kwargs...) = notificationbutton(;kwargs..., children = children)
notificationbutton(children_maker::Function; kwargs...) = notificationbutton(children_maker(); kwargs...)

