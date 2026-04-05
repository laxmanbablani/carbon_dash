# AUTO GENERATED FILE - DO NOT EDIT

export codesnippet

"""
    codesnippet(;kwargs...)
    codesnippet(children::Any;kwargs...)
    codesnippet(children_maker::Function;kwargs...)


A CodeSnippet component.
CodeSnippet is a wrapper for the Carbon CodeSnippet component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `align` (Bool | Real | String | Dict | Array; optional): align
- `ariaLabel` (Bool | Real | String | Dict | Array; optional): ariaLabel
- `autoAlign` (Bool | Real | String | Dict | Array; optional): autoAlign
- `className` (String; optional): className
- `copyButtonDescription` (Bool | Real | String | Dict | Array; optional): copyButtonDescription
- `copyText` (Bool | Real | String | Dict | Array; optional): copyText
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `feedback` (Bool | Real | String | Dict | Array; optional): feedback
- `feedbackTimeout` (Bool | Real | String | Dict | Array; optional): feedbackTimeout
- `hideCopyButton` (Bool | Real | String | Dict | Array; optional): hideCopyButton
- `light` (Bool | Real | String | Dict | Array; optional): light
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `maxCollapsedNumberOfRows` (Bool | Real | String | Dict | Array; optional): maxCollapsedNumberOfRows
- `maxExpandedNumberOfRows` (Bool | Real | String | Dict | Array; optional): maxExpandedNumberOfRows
- `minCollapsedNumberOfRows` (Bool | Real | String | Dict | Array; optional): minCollapsedNumberOfRows
- `minExpandedNumberOfRows` (Bool | Real | String | Dict | Array; optional): minExpandedNumberOfRows
- `onClick` (Bool | Real | String | Dict | Array; optional): onClick
- `showLessText` (Bool | Real | String | Dict | Array; optional): showLessText
- `showMoreText` (Bool | Real | String | Dict | Array; optional): showMoreText
- `style` (Dict; optional): style
- `type` (Bool | Real | String | Dict | Array; optional): type
- `wrapText` (Bool | Real | String | Dict | Array; optional): wrapText
"""
function codesnippet(; kwargs...)
        available_props = Symbol[:children, :id, :align, :ariaLabel, :autoAlign, :className, :copyButtonDescription, :copyText, :disabled, :feedback, :feedbackTimeout, :hideCopyButton, :light, :loading_state, :maxCollapsedNumberOfRows, :maxExpandedNumberOfRows, :minCollapsedNumberOfRows, :minExpandedNumberOfRows, :onClick, :showLessText, :showMoreText, :style, :type, :wrapText]
        wild_props = Symbol[]
        return Component("codesnippet", "CodeSnippet", "carbon_dash", available_props, wild_props; kwargs...)
end

codesnippet(children::Any; kwargs...) = codesnippet(;kwargs..., children = children)
codesnippet(children_maker::Function; kwargs...) = codesnippet(children_maker(); kwargs...)

