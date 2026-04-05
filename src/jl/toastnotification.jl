# AUTO GENERATED FILE - DO NOT EDIT

export toastnotification

"""
    toastnotification(;kwargs...)
    toastnotification(children::Any;kwargs...)
    toastnotification(children_maker::Function;kwargs...)


A ToastNotification component.
ToastNotification is a wrapper for the Carbon ToastNotification component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `ariaLabel` (Bool | Real | String | Dict | Array; optional): ariaLabel
- `caption` (Bool | Real | String | Dict | Array; optional): caption
- `className` (String; optional): className
- `hideCloseButton` (Bool | Real | String | Dict | Array; optional): hideCloseButton
- `kind` (Bool | Real | String | Dict | Array; optional): kind
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `lowContrast` (Bool | Real | String | Dict | Array; optional): lowContrast
- `onClose` (Bool | Real | String | Dict | Array; optional): onClose
- `onCloseButtonClick` (Bool | Real | String | Dict | Array; optional): onCloseButtonClick
- `role` (Bool | Real | String | Dict | Array; optional): role
- `statusIconDescription` (Bool | Real | String | Dict | Array; optional): statusIconDescription
- `style` (Dict; optional): style
- `subtitle` (Bool | Real | String | Dict | Array; optional): subtitle
- `timeout` (Bool | Real | String | Dict | Array; optional): timeout
- `title` (Bool | Real | String | Dict | Array; optional): title
"""
function toastnotification(; kwargs...)
        available_props = Symbol[:children, :id, :ariaLabel, :caption, :className, :hideCloseButton, :kind, :loading_state, :lowContrast, :onClose, :onCloseButtonClick, :role, :statusIconDescription, :style, :subtitle, :timeout, :title]
        wild_props = Symbol[]
        return Component("toastnotification", "ToastNotification", "carbon_dash", available_props, wild_props; kwargs...)
end

toastnotification(children::Any; kwargs...) = toastnotification(;kwargs..., children = children)
toastnotification(children_maker::Function; kwargs...) = toastnotification(children_maker(); kwargs...)

