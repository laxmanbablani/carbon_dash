# AUTO GENERATED FILE - DO NOT EDIT

export inlinenotification

"""
    inlinenotification(;kwargs...)
    inlinenotification(children::Any;kwargs...)
    inlinenotification(children_maker::Function;kwargs...)


An InlineNotification component.
InlineNotification is a wrapper for the Carbon InlineNotification component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
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
- `title` (Bool | Real | String | Dict | Array; optional): title
"""
function inlinenotification(; kwargs...)
        available_props = Symbol[:children, :id, :className, :hideCloseButton, :kind, :loading_state, :lowContrast, :onClose, :onCloseButtonClick, :role, :statusIconDescription, :style, :subtitle, :title]
        wild_props = Symbol[]
        return Component("inlinenotification", "InlineNotification", "carbon_dash", available_props, wild_props; kwargs...)
end

inlinenotification(children::Any; kwargs...) = inlinenotification(;kwargs..., children = children)
inlinenotification(children_maker::Function; kwargs...) = inlinenotification(children_maker(); kwargs...)

