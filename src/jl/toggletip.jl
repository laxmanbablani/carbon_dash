# AUTO GENERATED FILE - DO NOT EDIT

export toggletip

"""
    toggletip(;kwargs...)
    toggletip(children::Any;kwargs...)
    toggletip(children_maker::Function;kwargs...)


A Toggletip component.
Toggletip is a wrapper for the Carbon Toggletip component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `align` (Bool | Real | String | Dict | Array; optional): align
- `alignmentAxisOffset` (Bool | Real | String | Dict | Array; optional): alignmentAxisOffset
- `as_` (Bool | Real | String | Dict | Array; optional): as
- `autoAlign` (Bool | Real | String | Dict | Array; optional): autoAlign
- `autoAlignBoundary` (Bool | Real | String | Dict | Array; optional): autoAlignBoundary
- `backgroundToken` (Bool | Real | String | Dict | Array; optional): backgroundToken
- `border` (Bool | Real | String | Dict | Array; optional): border
- `caret` (Bool | Real | String | Dict | Array; optional): caret
- `className` (String; optional): className
- `defaultOpen` (Bool | Real | String | Dict | Array; optional): defaultOpen
- `dropShadow` (Bool | Real | String | Dict | Array; optional): dropShadow
- `highContrast` (Bool | Real | String | Dict | Array; optional): highContrast
- `isTabTip` (Bool | Real | String | Dict | Array; optional): isTabTip
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `onRequestClose` (Bool | Real | String | Dict | Array; optional): onRequestClose
- `style` (Dict; optional): style
"""
function toggletip(; kwargs...)
        available_props = Symbol[:children, :id, :align, :alignmentAxisOffset, :as_, :autoAlign, :autoAlignBoundary, :backgroundToken, :border, :caret, :className, :defaultOpen, :dropShadow, :highContrast, :isTabTip, :loading_state, :onRequestClose, :style]
        wild_props = Symbol[]
        return Component("toggletip", "Toggletip", "carbon_dash", available_props, wild_props; kwargs...)
end

toggletip(children::Any; kwargs...) = toggletip(;kwargs..., children = children)
toggletip(children_maker::Function; kwargs...) = toggletip(children_maker(); kwargs...)

