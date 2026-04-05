# AUTO GENERATED FILE - DO NOT EDIT

export tablecontainer

"""
    tablecontainer(;kwargs...)
    tablecontainer(children::Any;kwargs...)
    tablecontainer(children_maker::Function;kwargs...)


A TableContainer component.
TableContainer is a wrapper for the Carbon TableContainer component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `aiEnabled` (Bool | Real | String | Dict | Array; optional): aiEnabled
- `className` (String; optional): className
- `decorator` (Bool | Real | String | Dict | Array; optional): decorator
- `description` (Bool | Real | String | Dict | Array; optional): description
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `stickyHeader` (Bool | Real | String | Dict | Array; optional): stickyHeader
- `style` (Dict; optional): style
- `title` (Bool | Real | String | Dict | Array; optional): title
- `useStaticWidth` (Bool | Real | String | Dict | Array; optional): useStaticWidth
"""
function tablecontainer(; kwargs...)
        available_props = Symbol[:children, :id, :aiEnabled, :className, :decorator, :description, :loading_state, :stickyHeader, :style, :title, :useStaticWidth]
        wild_props = Symbol[]
        return Component("tablecontainer", "TableContainer", "carbon_dash", available_props, wild_props; kwargs...)
end

tablecontainer(children::Any; kwargs...) = tablecontainer(;kwargs..., children = children)
tablecontainer(children_maker::Function; kwargs...) = tablecontainer(children_maker(); kwargs...)

