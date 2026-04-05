# AUTO GENERATED FILE - DO NOT EDIT

export datatableskeleton

"""
    datatableskeleton(;kwargs...)
    datatableskeleton(children::Any;kwargs...)
    datatableskeleton(children_maker::Function;kwargs...)


A DataTableSkeleton component.
DataTableSkeleton is a wrapper for the Carbon DataTableSkeleton component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `columnCount` (Bool | Real | String | Dict | Array; optional): columnCount
- `headers` (Bool | Real | String | Dict | Array; optional): headers
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `rowCount` (Bool | Real | String | Dict | Array; optional): rowCount
- `showHeader` (Bool | Real | String | Dict | Array; optional): showHeader
- `showToolbar` (Bool | Real | String | Dict | Array; optional): showToolbar
- `size` (Bool | Real | String | Dict | Array; optional): size
- `style` (Dict; optional): style
- `zebra` (Bool | Real | String | Dict | Array; optional): zebra
"""
function datatableskeleton(; kwargs...)
        available_props = Symbol[:children, :id, :className, :columnCount, :headers, :loading_state, :rowCount, :showHeader, :showToolbar, :size, :style, :zebra]
        wild_props = Symbol[]
        return Component("datatableskeleton", "DataTableSkeleton", "carbon_dash", available_props, wild_props; kwargs...)
end

datatableskeleton(children::Any; kwargs...) = datatableskeleton(;kwargs..., children = children)
datatableskeleton(children_maker::Function; kwargs...) = datatableskeleton(children_maker(); kwargs...)

