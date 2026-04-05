# AUTO GENERATED FILE - DO NOT EDIT

export checkboxgroup

"""
    checkboxgroup(;kwargs...)
    checkboxgroup(children::Any;kwargs...)
    checkboxgroup(children_maker::Function;kwargs...)


A CheckboxGroup component.
CheckboxGroup is a wrapper for the Carbon CheckboxGroup component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `decorator` (Bool | Real | String | Dict | Array; optional): decorator
- `helperText` (Bool | Real | String | Dict | Array; optional): helperText
- `invalid` (Bool | Real | String | Dict | Array; optional): invalid
- `invalidText` (Bool | Real | String | Dict | Array; optional): invalidText
- `legendId` (Bool | Real | String | Dict | Array; optional): legendId
- `legendText` (Bool | Real | String | Dict | Array; optional): legendText
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `orientation` (Bool | Real | String | Dict | Array; optional): orientation
- `readOnly` (Bool | Real | String | Dict | Array; optional): readOnly
- `slug` (Bool | Real | String | Dict | Array; optional): slug
- `style` (Dict; optional): style
- `warn` (Bool | Real | String | Dict | Array; optional): warn
- `warnText` (Bool | Real | String | Dict | Array; optional): warnText
"""
function checkboxgroup(; kwargs...)
        available_props = Symbol[:children, :id, :className, :decorator, :helperText, :invalid, :invalidText, :legendId, :legendText, :loading_state, :orientation, :readOnly, :slug, :style, :warn, :warnText]
        wild_props = Symbol[]
        return Component("checkboxgroup", "CheckboxGroup", "carbon_dash", available_props, wild_props; kwargs...)
end

checkboxgroup(children::Any; kwargs...) = checkboxgroup(;kwargs..., children = children)
checkboxgroup(children_maker::Function; kwargs...) = checkboxgroup(children_maker(); kwargs...)

