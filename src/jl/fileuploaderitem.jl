# AUTO GENERATED FILE - DO NOT EDIT

export fileuploaderitem

"""
    fileuploaderitem(;kwargs...)
    fileuploaderitem(children::Any;kwargs...)
    fileuploaderitem(children_maker::Function;kwargs...)


A FileUploaderItem component.
FileUploaderItem is a wrapper for the Carbon FileUploaderItem component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `errorBody` (Bool | Real | String | Dict | Array; optional): errorBody
- `errorSubject` (Bool | Real | String | Dict | Array; optional): errorSubject
- `iconDescription` (Bool | Real | String | Dict | Array; optional): iconDescription
- `invalid` (Bool | Real | String | Dict | Array; optional): invalid
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `name` (Bool | Real | String | Dict | Array; optional): name
- `onDelete` (Bool | Real | String | Dict | Array; optional): onDelete
- `size` (Bool | Real | String | Dict | Array; optional): size
- `status` (Bool | Real | String | Dict | Array; optional): status
- `style` (Dict; optional): style
- `uuid` (Bool | Real | String | Dict | Array; optional): uuid
"""
function fileuploaderitem(; kwargs...)
        available_props = Symbol[:children, :id, :className, :errorBody, :errorSubject, :iconDescription, :invalid, :loading_state, :name, :onDelete, :size, :status, :style, :uuid]
        wild_props = Symbol[]
        return Component("fileuploaderitem", "FileUploaderItem", "carbon_dash", available_props, wild_props; kwargs...)
end

fileuploaderitem(children::Any; kwargs...) = fileuploaderitem(;kwargs..., children = children)
fileuploaderitem(children_maker::Function; kwargs...) = fileuploaderitem(children_maker(); kwargs...)

