# AUTO GENERATED FILE - DO NOT EDIT

export inlineloading

"""
    inlineloading(;kwargs...)
    inlineloading(children::Any;kwargs...)
    inlineloading(children_maker::Function;kwargs...)


An InlineLoading component.
InlineLoading is a wrapper for the Carbon InlineLoading component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `description` (Bool | Real | String | Dict | Array; optional): description
- `iconDescription` (Bool | Real | String | Dict | Array; optional): iconDescription
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `onSuccess` (Bool | Real | String | Dict | Array; optional): onSuccess
- `status` (Bool | Real | String | Dict | Array; optional): status
- `style` (Dict; optional): style
- `successDelay` (Bool | Real | String | Dict | Array; optional): successDelay
"""
function inlineloading(; kwargs...)
        available_props = Symbol[:children, :id, :className, :description, :iconDescription, :loading_state, :onSuccess, :status, :style, :successDelay]
        wild_props = Symbol[]
        return Component("inlineloading", "InlineLoading", "carbon_dash", available_props, wild_props; kwargs...)
end

inlineloading(children::Any; kwargs...) = inlineloading(;kwargs..., children = children)
inlineloading(children_maker::Function; kwargs...) = inlineloading(children_maker(); kwargs...)

