# AUTO GENERATED FILE - DO NOT EDIT

export actionablenotification

"""
    actionablenotification(;kwargs...)
    actionablenotification(children::Any;kwargs...)
    actionablenotification(children_maker::Function;kwargs...)


An ActionableNotification component.
ActionableNotification is a wrapper for the Carbon ActionableNotification component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `actionButtonLabel` (Bool | Real | String | Dict | Array; optional): actionButtonLabel
- `ariaLabel` (Bool | Real | String | Dict | Array; optional): ariaLabel
- `caption` (Bool | Real | String | Dict | Array; optional): caption
- `className` (String; optional): className
- `closeOnEscape` (Bool | Real | String | Dict | Array; optional): closeOnEscape
- `hasFocus` (Bool | Real | String | Dict | Array; optional): hasFocus
- `hideCloseButton` (Bool | Real | String | Dict | Array; optional): hideCloseButton
- `inline` (Bool | Real | String | Dict | Array; optional): inline
- `kind` (Bool | Real | String | Dict | Array; optional): kind
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `lowContrast` (Bool | Real | String | Dict | Array; optional): lowContrast
- `onActionButtonClick` (Bool | Real | String | Dict | Array; optional): onActionButtonClick
- `onClose` (Bool | Real | String | Dict | Array; optional): onClose
- `onCloseButtonClick` (Bool | Real | String | Dict | Array; optional): onCloseButtonClick
- `role` (Bool | Real | String | Dict | Array; optional): role
- `statusIconDescription` (Bool | Real | String | Dict | Array; optional): statusIconDescription
- `style` (Dict; optional): style
- `subtitle` (Bool | Real | String | Dict | Array; optional): subtitle
- `title` (Bool | Real | String | Dict | Array; optional): title
"""
function actionablenotification(; kwargs...)
        available_props = Symbol[:children, :id, :actionButtonLabel, :ariaLabel, :caption, :className, :closeOnEscape, :hasFocus, :hideCloseButton, :inline, :kind, :loading_state, :lowContrast, :onActionButtonClick, :onClose, :onCloseButtonClick, :role, :statusIconDescription, :style, :subtitle, :title]
        wild_props = Symbol[]
        return Component("actionablenotification", "ActionableNotification", "carbon_dash", available_props, wild_props; kwargs...)
end

actionablenotification(children::Any; kwargs...) = actionablenotification(;kwargs..., children = children)
actionablenotification(children_maker::Function; kwargs...) = actionablenotification(children_maker(); kwargs...)

