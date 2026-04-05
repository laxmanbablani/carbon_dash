# AUTO GENERATED FILE - DO NOT EDIT

export iconbutton

"""
    iconbutton(;kwargs...)
    iconbutton(children::Any;kwargs...)
    iconbutton(children_maker::Function;kwargs...)


An IconButton component.
IconButton is a wrapper for the Carbon IconButton component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `align` (Bool | Real | String | Dict | Array; optional): align
- `autoAlign` (Bool | Real | String | Dict | Array; optional): autoAlign
- `badgeCount` (Bool | Real | String | Dict | Array; optional): badgeCount
- `className` (String; optional): className
- `closeOnActivation` (Bool | Real | String | Dict | Array; optional): closeOnActivation
- `defaultOpen` (Bool | Real | String | Dict | Array; optional): defaultOpen
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `dropShadow` (Bool | Real | String | Dict | Array; optional): dropShadow
- `enterDelayMs` (Bool | Real | String | Dict | Array; optional): enterDelayMs
- `highContrast` (Bool | Real | String | Dict | Array; optional): highContrast
- `href` (Bool | Real | String | Dict | Array; optional): href
- `isSelected` (Bool | Real | String | Dict | Array; optional): isSelected
- `kind` (Bool | Real | String | Dict | Array; optional): kind
- `label` (Bool | Real | String | Dict | Array; optional): label
- `leaveDelayMs` (Bool | Real | String | Dict | Array; optional): leaveDelayMs
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `rel` (Bool | Real | String | Dict | Array; optional): rel
- `size` (Bool | Real | String | Dict | Array; optional): size
- `style` (Dict; optional): style
- `target` (Bool | Real | String | Dict | Array; optional): target
- `wrapperClasses` (Bool | Real | String | Dict | Array; optional): wrapperClasses
"""
function iconbutton(; kwargs...)
        available_props = Symbol[:children, :id, :align, :autoAlign, :badgeCount, :className, :closeOnActivation, :defaultOpen, :disabled, :dropShadow, :enterDelayMs, :highContrast, :href, :isSelected, :kind, :label, :leaveDelayMs, :loading_state, :rel, :size, :style, :target, :wrapperClasses]
        wild_props = Symbol[]
        return Component("iconbutton", "IconButton", "carbon_dash", available_props, wild_props; kwargs...)
end

iconbutton(children::Any; kwargs...) = iconbutton(;kwargs..., children = children)
iconbutton(children_maker::Function; kwargs...) = iconbutton(children_maker(); kwargs...)

