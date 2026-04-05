# AUTO GENERATED FILE - DO NOT EDIT

export formgroup

"""
    formgroup(;kwargs...)
    formgroup(children::Any;kwargs...)
    formgroup(children_maker::Function;kwargs...)


A FormGroup component.
FormGroup is a wrapper for the Carbon FormGroup component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `invalid` (Bool | Real | String | Dict | Array; optional): invalid
- `legendId` (Bool | Real | String | Dict | Array; optional): legendId
- `legendText` (Bool | Real | String | Dict | Array; optional): legendText
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `message` (Bool | Real | String | Dict | Array; optional): message
- `messageText` (Bool | Real | String | Dict | Array; optional): messageText
- `style` (Dict; optional): style
"""
function formgroup(; kwargs...)
        available_props = Symbol[:children, :id, :className, :disabled, :invalid, :legendId, :legendText, :loading_state, :message, :messageText, :style]
        wild_props = Symbol[]
        return Component("formgroup", "FormGroup", "carbon_dash", available_props, wild_props; kwargs...)
end

formgroup(children::Any; kwargs...) = formgroup(;kwargs..., children = children)
formgroup(children_maker::Function; kwargs...) = formgroup(children_maker(); kwargs...)

