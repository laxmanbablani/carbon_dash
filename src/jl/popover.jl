# AUTO GENERATED FILE - DO NOT EDIT

export popover

"""
    popover(;kwargs...)
    popover(children::Any;kwargs...)
    popover(children_maker::Function;kwargs...)


A Popover component.
Popover is a wrapper for the Carbon Popover component.
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
- `dropShadow` (Bool | Real | String | Dict | Array; optional): dropShadow
- `height` (Bool | Real | String | Dict | Array; optional): height
- `highContrast` (Bool | Real | String | Dict | Array; optional): highContrast
- `isTabTip` (Bool | Real | String | Dict | Array; optional): isTabTip
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `onRequestClose` (Bool | Real | String | Dict | Array; optional): onRequestClose
- `open` (Bool | Real | String | Dict | Array; optional): open
- `style` (Dict; optional): style
- `width` (Bool | Real | String | Dict | Array; optional): width
- `x` (Bool | Real | String | Dict | Array; optional): x
- `y` (Bool | Real | String | Dict | Array; optional): y
"""
function popover(; kwargs...)
        available_props = Symbol[:children, :id, :align, :alignmentAxisOffset, :as_, :autoAlign, :autoAlignBoundary, :backgroundToken, :border, :caret, :className, :dropShadow, :height, :highContrast, :isTabTip, :loading_state, :onRequestClose, :open, :style, :width, :x, :y]
        wild_props = Symbol[]
        return Component("popover", "Popover", "carbon_dash", available_props, wild_props; kwargs...)
end

popover(children::Any; kwargs...) = popover(;kwargs..., children = children)
popover(children_maker::Function; kwargs...) = popover(children_maker(); kwargs...)

