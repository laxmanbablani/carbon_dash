# AUTO GENERATED FILE - DO NOT EDIT

export column

"""
    column(;kwargs...)
    column(children::Any;kwargs...)
    column(children_maker::Function;kwargs...)


A Column component.
Column is a wrapper for the Carbon Column component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `as_` (Bool | Real | String | Dict | Array; optional): as
- `className` (String; optional): className
- `lg` (Bool | Real | String | Dict | Array; optional): lg
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `max` (Bool | Real | String | Dict | Array; optional): max
- `md` (Bool | Real | String | Dict | Array; optional): md
- `sm` (Bool | Real | String | Dict | Array; optional): sm
- `span` (Bool | Real | String | Dict | Array; optional): span
- `style` (Dict; optional): style
- `xlg` (Bool | Real | String | Dict | Array; optional): xlg
"""
function column(; kwargs...)
        available_props = Symbol[:children, :id, :as_, :className, :lg, :loading_state, :max, :md, :sm, :span, :style, :xlg]
        wild_props = Symbol[]
        return Component("column", "Column", "carbon_dash", available_props, wild_props; kwargs...)
end

column(children::Any; kwargs...) = column(;kwargs..., children = children)
column(children_maker::Function; kwargs...) = column(children_maker(); kwargs...)

