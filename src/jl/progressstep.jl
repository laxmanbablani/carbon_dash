# AUTO GENERATED FILE - DO NOT EDIT

export progressstep

"""
    progressstep(;kwargs...)
    progressstep(children::Any;kwargs...)
    progressstep(children_maker::Function;kwargs...)


A ProgressStep component.
ProgressStep is a wrapper for the Carbon ProgressStep component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `complete` (Bool | Real | String | Dict | Array; optional): complete
- `current` (Bool | Real | String | Dict | Array; optional): current
- `description` (String; optional): description
- `disabled` (Bool; optional): disabled
- `index` (Bool | Real | String | Dict | Array; optional): index
- `invalid` (Bool | Real | String | Dict | Array; optional): invalid
- `label` (a list of or a singular dash component, string or number; optional): label
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `onClick` (Bool | Real | String | Dict | Array; optional): onClick
- `overflowTooltipProps` (Bool | Real | String | Dict | Array; optional): overflowTooltipProps
- `secondaryLabel` (String; optional): secondaryLabel
- `style` (Dict; optional): style
- `tooltipId` (Bool | Real | String | Dict | Array; optional): tooltipId
- `translateWithId` (Bool | Real | String | Dict | Array; optional): translateWithId
"""
function progressstep(; kwargs...)
        available_props = Symbol[:children, :id, :className, :complete, :current, :description, :disabled, :index, :invalid, :label, :loading_state, :onClick, :overflowTooltipProps, :secondaryLabel, :style, :tooltipId, :translateWithId]
        wild_props = Symbol[]
        return Component("progressstep", "ProgressStep", "carbon_dash", available_props, wild_props; kwargs...)
end

progressstep(children::Any; kwargs...) = progressstep(;kwargs..., children = children)
progressstep(children_maker::Function; kwargs...) = progressstep(children_maker(); kwargs...)

