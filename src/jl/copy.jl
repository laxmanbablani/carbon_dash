# AUTO GENERATED FILE - DO NOT EDIT

export copy

"""
    copy(;kwargs...)
    copy(children::Any;kwargs...)
    copy(children_maker::Function;kwargs...)


A Copy component.
Copy is a wrapper for the Carbon Copy component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `align` (Bool | Real | String | Dict | Array; optional): align
- `autoAlign` (Bool | Real | String | Dict | Array; optional): autoAlign
- `className` (String; optional): className
- `feedback` (Bool | Real | String | Dict | Array; optional): feedback
- `feedbackTimeout` (Bool | Real | String | Dict | Array; optional): feedbackTimeout
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `onAnimationEnd` (Bool | Real | String | Dict | Array; optional): onAnimationEnd
- `onClick` (Bool | Real | String | Dict | Array; optional): onClick
- `style` (Dict; optional): style
"""
function copy(; kwargs...)
        available_props = Symbol[:children, :id, :align, :autoAlign, :className, :feedback, :feedbackTimeout, :loading_state, :onAnimationEnd, :onClick, :style]
        wild_props = Symbol[]
        return Component("copy", "Copy", "carbon_dash", available_props, wild_props; kwargs...)
end

copy(children::Any; kwargs...) = copy(;kwargs..., children = children)
copy(children_maker::Function; kwargs...) = copy(children_maker(); kwargs...)

