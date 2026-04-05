# AUTO GENERATED FILE - DO NOT EDIT

export paginationnav

"""
    paginationnav(;kwargs...)
    paginationnav(children::Any;kwargs...)
    paginationnav(children_maker::Function;kwargs...)


A PaginationNav component.
PaginationNav is a wrapper for the Carbon PaginationNav component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `disableOverflow` (Bool | Real | String | Dict | Array; optional): disableOverflow
- `itemsShown` (Bool | Real | String | Dict | Array; optional): itemsShown
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `loop` (Bool | Real | String | Dict | Array; optional): loop
- `onChange` (Bool | Real | String | Dict | Array; optional): onChange
- `page` (Bool | Real | String | Dict | Array; optional): page
- `size` (Bool | Real | String | Dict | Array; optional): size
- `style` (Dict; optional): style
- `tooltipAlignment` (Bool | Real | String | Dict | Array; optional): tooltipAlignment
- `tooltipPosition` (Bool | Real | String | Dict | Array; optional): tooltipPosition
- `totalItems` (Bool | Real | String | Dict | Array; optional): totalItems
- `translateWithId` (Bool | Real | String | Dict | Array; optional): translateWithId
"""
function paginationnav(; kwargs...)
        available_props = Symbol[:children, :id, :className, :disableOverflow, :itemsShown, :loading_state, :loop, :onChange, :page, :size, :style, :tooltipAlignment, :tooltipPosition, :totalItems, :translateWithId]
        wild_props = Symbol[]
        return Component("paginationnav", "PaginationNav", "carbon_dash", available_props, wild_props; kwargs...)
end

paginationnav(children::Any; kwargs...) = paginationnav(;kwargs..., children = children)
paginationnav(children_maker::Function; kwargs...) = paginationnav(children_maker(); kwargs...)

