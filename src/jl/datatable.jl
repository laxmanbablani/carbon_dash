# AUTO GENERATED FILE - DO NOT EDIT

export datatable

"""
    datatable(;kwargs...)
    datatable(children::Any;kwargs...)
    datatable(children_maker::Function;kwargs...)


A DataTable component.
DataTable is a wrapper for the Carbon DataTable component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `description` (String; optional): description
- `experimentalAutoAlign` (Bool | Real | String | Dict | Array; optional): experimentalAutoAlign
- `filterRows` (Bool | Real | String | Dict | Array; optional): filterRows
- `header` (Bool | Real | String | Dict | Array; optional): header
- `headers` (Array; optional): headers
- `isSortable` (Bool; optional): isSortable
- `key` (Bool | Real | String | Dict | Array; optional): key
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `locale` (Bool | Real | String | Dict | Array; optional): locale
- `overflowMenuOnHover` (Bool | Real | String | Dict | Array; optional): overflowMenuOnHover
- `radio` (Bool | Real | String | Dict | Array; optional): radio
- `render` (Bool | Real | String | Dict | Array; optional): render
- `rows` (Array; optional): rows
- `size` (String; optional): size
- `sortRow` (Bool | Real | String | Dict | Array; optional): sortRow
- `stickyHeader` (Bool | Real | String | Dict | Array; optional): stickyHeader
- `style` (Dict; optional): style
- `title` (String; optional): title
- `translateWithId` (Bool | Real | String | Dict | Array; optional): translateWithId
- `useStaticWidth` (Bool | Real | String | Dict | Array; optional): useStaticWidth
- `useZebraStyles` (Bool; optional): useZebraStyles
- `withExpansion` (Bool; optional): withExpansion
- `withSelection` (Bool; optional): withSelection
"""
function datatable(; kwargs...)
        available_props = Symbol[:children, :id, :className, :description, :experimentalAutoAlign, :filterRows, :header, :headers, :isSortable, :key, :loading_state, :locale, :overflowMenuOnHover, :radio, :render, :rows, :size, :sortRow, :stickyHeader, :style, :title, :translateWithId, :useStaticWidth, :useZebraStyles, :withExpansion, :withSelection]
        wild_props = Symbol[]
        return Component("datatable", "DataTable", "carbon_dash", available_props, wild_props; kwargs...)
end

datatable(children::Any; kwargs...) = datatable(;kwargs..., children = children)
datatable(children_maker::Function; kwargs...) = datatable(children_maker(); kwargs...)

