# AUTO GENERATED FILE - DO NOT EDIT

export progressindicator

"""
    progressindicator(;kwargs...)
    progressindicator(children::Any;kwargs...)
    progressindicator(children_maker::Function;kwargs...)


A ProgressIndicator component.
ProgressIndicator is a wrapper for the Carbon ProgressIndicator component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `currentIndex` (Real; optional): currentIndex
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `onChange` (Bool | Real | String | Dict | Array; optional): onChange
- `spaceEqually` (Bool; optional): spaceEqually
- `style` (Dict; optional): style
- `vertical` (Bool; optional): vertical
"""
function progressindicator(; kwargs...)
        available_props = Symbol[:children, :id, :className, :currentIndex, :loading_state, :onChange, :spaceEqually, :style, :vertical]
        wild_props = Symbol[]
        return Component("progressindicator", "ProgressIndicator", "carbon_dash", available_props, wild_props; kwargs...)
end

progressindicator(children::Any; kwargs...) = progressindicator(;kwargs..., children = children)
progressindicator(children_maker::Function; kwargs...) = progressindicator(children_maker(); kwargs...)

