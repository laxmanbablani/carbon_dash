# AUTO GENERATED FILE - DO NOT EDIT

export switch

"""
    switch(;kwargs...)
    switch(children::Any;kwargs...)
    switch(children_maker::Function;kwargs...)


A Switch component.
Switch is a wrapper for the Carbon Switch component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `index` (Bool | Real | String | Dict | Array; optional): index
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `name` (Bool | Real | String | Dict | Array; optional): name
- `onClick` (Bool | Real | String | Dict | Array; optional): onClick
- `onKeyDown` (Bool | Real | String | Dict | Array; optional): onKeyDown
- `selected` (Bool | Real | String | Dict | Array; optional): selected
- `style` (Dict; optional): style
- `text` (Bool | Real | String | Dict | Array; optional): text
"""
function switch(; kwargs...)
        available_props = Symbol[:children, :id, :className, :disabled, :index, :loading_state, :name, :onClick, :onKeyDown, :selected, :style, :text]
        wild_props = Symbol[]
        return Component("switch", "Switch", "carbon_dash", available_props, wild_props; kwargs...)
end

switch(children::Any; kwargs...) = switch(;kwargs..., children = children)
switch(children_maker::Function; kwargs...) = switch(children_maker(); kwargs...)

