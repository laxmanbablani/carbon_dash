# AUTO GENERATED FILE - DO NOT EDIT

export filename

"""
    filename(;kwargs...)
    filename(children::Any;kwargs...)
    filename(children_maker::Function;kwargs...)


A Filename component.
Filename is a wrapper for the Carbon Filename component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `iconDescription` (Bool | Real | String | Dict | Array; optional): iconDescription
- `invalid` (Bool | Real | String | Dict | Array; optional): invalid
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `name` (Bool | Real | String | Dict | Array; optional): name
- `status` (Bool | Real | String | Dict | Array; optional): status
- `style` (Dict; optional): style
- `tabIndex` (Bool | Real | String | Dict | Array; optional): tabIndex
"""
function filename(; kwargs...)
        available_props = Symbol[:children, :id, :className, :iconDescription, :invalid, :loading_state, :name, :status, :style, :tabIndex]
        wild_props = Symbol[]
        return Component("filename", "Filename", "carbon_dash", available_props, wild_props; kwargs...)
end

filename(children::Any; kwargs...) = filename(;kwargs..., children = children)
filename(children_maker::Function; kwargs...) = filename(children_maker(); kwargs...)

