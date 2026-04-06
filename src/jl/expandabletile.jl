# AUTO GENERATED FILE - DO NOT EDIT

export expandabletile

"""
    expandabletile(;kwargs...)
    expandabletile(children::Any;kwargs...)
    expandabletile(children_maker::Function;kwargs...)


An ExpandableTile component.
ExpandableTile is a wrapper for the Carbon ExpandableTile component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `decorator` (Bool | Real | String | Dict | Array; optional): decorator
- `expanded` (Bool; optional): expanded
- `hasRoundedCorners` (Bool | Real | String | Dict | Array; optional): hasRoundedCorners
- `light` (Bool | Real | String | Dict | Array; optional): light
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `onClick` (Bool | Real | String | Dict | Array; optional): onClick
- `onKeyUp` (Bool | Real | String | Dict | Array; optional): onKeyUp
- `slug` (Bool | Real | String | Dict | Array; optional): slug
- `style` (Dict; optional): style
- `tabIndex` (Bool | Real | String | Dict | Array; optional): tabIndex
- `tileCollapsedIconText` (a list of or a singular dash component, string or number; optional): tileCollapsedIconText
- `tileCollapsedLabel` (Bool | Real | String | Dict | Array; optional): tileCollapsedLabel
- `tileExpandedIconText` (a list of or a singular dash component, string or number; optional): tileExpandedIconText
- `tileExpandedLabel` (Bool | Real | String | Dict | Array; optional): tileExpandedLabel
"""
function expandabletile(; kwargs...)
        available_props = Symbol[:children, :id, :className, :decorator, :expanded, :hasRoundedCorners, :light, :loading_state, :onClick, :onKeyUp, :slug, :style, :tabIndex, :tileCollapsedIconText, :tileCollapsedLabel, :tileExpandedIconText, :tileExpandedLabel]
        wild_props = Symbol[]
        return Component("expandabletile", "ExpandableTile", "carbon_dash", available_props, wild_props; kwargs...)
end

expandabletile(children::Any; kwargs...) = expandabletile(;kwargs..., children = children)
expandabletile(children_maker::Function; kwargs...) = expandabletile(children_maker(); kwargs...)

