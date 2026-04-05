# AUTO GENERATED FILE - DO NOT EDIT

export table

"""
    table(;kwargs...)
    table(children::Any;kwargs...)
    table(children_maker::Function;kwargs...)


A Table component.
Table is a wrapper for the Carbon Table component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `experimentalAutoAlign` (Bool | Real | String | Dict | Array; optional): experimentalAutoAlign
- `isSortable` (Bool | Real | String | Dict | Array; optional): isSortable
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `overflowMenuOnHover` (Bool | Real | String | Dict | Array; optional): overflowMenuOnHover
- `size` (Bool | Real | String | Dict | Array; optional): size
- `stickyHeader` (Bool | Real | String | Dict | Array; optional): stickyHeader
- `style` (Dict; optional): style
- `tabIndex` (Bool | Real | String | Dict | Array; optional): tabIndex
- `useStaticWidth` (Bool | Real | String | Dict | Array; optional): useStaticWidth
- `useZebraStyles` (Bool | Real | String | Dict | Array; optional): useZebraStyles
"""
function table(; kwargs...)
        available_props = Symbol[:children, :id, :className, :experimentalAutoAlign, :isSortable, :loading_state, :overflowMenuOnHover, :size, :stickyHeader, :style, :tabIndex, :useStaticWidth, :useZebraStyles]
        wild_props = Symbol[]
        return Component("table", "Table", "carbon_dash", available_props, wild_props; kwargs...)
end

table(children::Any; kwargs...) = table(;kwargs..., children = children)
table(children_maker::Function; kwargs...) = table(children_maker(); kwargs...)

