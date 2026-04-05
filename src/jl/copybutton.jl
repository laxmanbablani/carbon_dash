# AUTO GENERATED FILE - DO NOT EDIT

export copybutton

"""
    copybutton(;kwargs...)
    copybutton(children::Any;kwargs...)
    copybutton(children_maker::Function;kwargs...)


A CopyButton component.
CopyButton is a wrapper for the Carbon CopyButton component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `align` (Bool | Real | String | Dict | Array; optional): align
- `autoAlign` (Bool | Real | String | Dict | Array; optional): autoAlign
- `className` (String; optional): className
- `feedback` (Bool | Real | String | Dict | Array; optional): feedback
- `feedbackTimeout` (Bool | Real | String | Dict | Array; optional): feedbackTimeout
- `iconDescription` (Bool | Real | String | Dict | Array; optional): iconDescription
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `onClick` (Bool | Real | String | Dict | Array; optional): onClick
- `style` (Dict; optional): style
"""
function copybutton(; kwargs...)
        available_props = Symbol[:children, :id, :align, :autoAlign, :className, :feedback, :feedbackTimeout, :iconDescription, :loading_state, :onClick, :style]
        wild_props = Symbol[]
        return Component("copybutton", "CopyButton", "carbon_dash", available_props, wild_props; kwargs...)
end

copybutton(children::Any; kwargs...) = copybutton(;kwargs..., children = children)
copybutton(children_maker::Function; kwargs...) = copybutton(children_maker(); kwargs...)

