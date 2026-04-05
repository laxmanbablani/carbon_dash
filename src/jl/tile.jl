# AUTO GENERATED FILE - DO NOT EDIT

export tile

"""
    tile(;kwargs...)
    tile(children::Any;kwargs...)
    tile(children_maker::Function;kwargs...)


A Tile component.
Tile is a wrapper for the Carbon Tile component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `decorator` (Bool | Real | String | Dict | Array; optional): decorator
- `hasRoundedCorners` (Bool | Real | String | Dict | Array; optional): hasRoundedCorners
- `light` (Bool | Real | String | Dict | Array; optional): light
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `slug` (Bool | Real | String | Dict | Array; optional): slug
- `style` (Dict; optional): style
"""
function tile(; kwargs...)
        available_props = Symbol[:children, :id, :className, :decorator, :hasRoundedCorners, :light, :loading_state, :slug, :style]
        wild_props = Symbol[]
        return Component("tile", "Tile", "carbon_dash", available_props, wild_props; kwargs...)
end

tile(children::Any; kwargs...) = tile(;kwargs..., children = children)
tile(children_maker::Function; kwargs...) = tile(children_maker(); kwargs...)

