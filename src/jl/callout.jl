# AUTO GENERATED FILE - DO NOT EDIT

export callout

"""
    callout(;kwargs...)
    callout(children::Any;kwargs...)
    callout(children_maker::Function;kwargs...)


A Callout component.
Callout is a wrapper for the Carbon Callout component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `actionButtonLabel` (Bool | Real | String | Dict | Array; optional): actionButtonLabel
- `className` (String; optional): className
- `kind` (Bool | Real | String | Dict | Array; optional): kind
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `lowContrast` (Bool | Real | String | Dict | Array; optional): lowContrast
- `onActionButtonClick` (Bool | Real | String | Dict | Array; optional): onActionButtonClick
- `statusIconDescription` (Bool | Real | String | Dict | Array; optional): statusIconDescription
- `style` (Dict; optional): style
- `subtitle` (Bool | Real | String | Dict | Array; optional): subtitle
- `title` (Bool | Real | String | Dict | Array; optional): title
- `titleId` (Bool | Real | String | Dict | Array; optional): titleId
"""
function callout(; kwargs...)
        available_props = Symbol[:children, :id, :actionButtonLabel, :className, :kind, :loading_state, :lowContrast, :onActionButtonClick, :statusIconDescription, :style, :subtitle, :title, :titleId]
        wild_props = Symbol[]
        return Component("callout", "Callout", "carbon_dash", available_props, wild_props; kwargs...)
end

callout(children::Any; kwargs...) = callout(;kwargs..., children = children)
callout(children_maker::Function; kwargs...) = callout(children_maker(); kwargs...)

