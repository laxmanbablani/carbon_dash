# AUTO GENERATED FILE - DO NOT EDIT

export ailabel

"""
    ailabel(;kwargs...)
    ailabel(children::Any;kwargs...)
    ailabel(children_maker::Function;kwargs...)


An AILabel component.
AILabel is a wrapper for the Carbon AILabel component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `AILabelContent` (Bool | Real | String | Dict | Array; optional): AILabelContent
- `aiText` (Bool | Real | String | Dict | Array; optional): aiText
- `aiTextLabel` (Bool | Real | String | Dict | Array; optional): aiTextLabel
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
- `kind` (Bool | Real | String | Dict | Array; optional): kind
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `onRequestClose` (Bool | Real | String | Dict | Array; optional): onRequestClose
- `onRevertClick` (Bool | Real | String | Dict | Array; optional): onRevertClick
- `revertActive` (Bool | Real | String | Dict | Array; optional): revertActive
- `revertLabel` (Bool | Real | String | Dict | Array; optional): revertLabel
- `size` (Bool | Real | String | Dict | Array; optional): size
- `slugLabel` (Bool | Real | String | Dict | Array; optional): slugLabel
- `style` (Dict; optional): style
- `textLabel` (Bool | Real | String | Dict | Array; optional): textLabel
"""
function ailabel(; kwargs...)
        available_props = Symbol[:children, :id, :AILabelContent, :aiText, :aiTextLabel, :align, :alignmentAxisOffset, :as_, :autoAlign, :autoAlignBoundary, :backgroundToken, :border, :caret, :className, :defaultOpen, :dropShadow, :highContrast, :isTabTip, :kind, :loading_state, :onRequestClose, :onRevertClick, :revertActive, :revertLabel, :size, :slugLabel, :style, :textLabel]
        wild_props = Symbol[]
        return Component("ailabel", "AILabel", "carbon_dash", available_props, wild_props; kwargs...)
end

ailabel(children::Any; kwargs...) = ailabel(;kwargs..., children = children)
ailabel(children_maker::Function; kwargs...) = ailabel(children_maker(); kwargs...)

