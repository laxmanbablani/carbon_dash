# AUTO GENERATED FILE - DO NOT EDIT

export tilegroup

"""
    tilegroup(;kwargs...)
    tilegroup(children::Any;kwargs...)
    tilegroup(children_maker::Function;kwargs...)


A TileGroup component.
TileGroup is a wrapper for the Carbon TileGroup component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `defaultSelected` (Bool | Real | String | Dict | Array; optional): defaultSelected
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `legend` (Bool | Real | String | Dict | Array; optional): legend
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `name` (Bool | Real | String | Dict | Array; optional): name
- `onChange` (Bool | Real | String | Dict | Array; optional): onChange
- `required` (Bool | Real | String | Dict | Array; optional): required
- `style` (Dict; optional): style
- `valueSelected` (Bool | Real | String | Dict | Array; optional): valueSelected
"""
function tilegroup(; kwargs...)
        available_props = Symbol[:children, :id, :className, :defaultSelected, :disabled, :legend, :loading_state, :name, :onChange, :required, :style, :valueSelected]
        wild_props = Symbol[]
        return Component("tilegroup", "TileGroup", "carbon_dash", available_props, wild_props; kwargs...)
end

tilegroup(children::Any; kwargs...) = tilegroup(;kwargs..., children = children)
tilegroup(children_maker::Function; kwargs...) = tilegroup(children_maker(); kwargs...)

