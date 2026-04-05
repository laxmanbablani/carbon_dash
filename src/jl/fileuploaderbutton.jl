# AUTO GENERATED FILE - DO NOT EDIT

export fileuploaderbutton

"""
    fileuploaderbutton(;kwargs...)
    fileuploaderbutton(children::Any;kwargs...)
    fileuploaderbutton(children_maker::Function;kwargs...)


A FileUploaderButton component.
FileUploaderButton is a wrapper for the Carbon FileUploaderButton component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `accept` (Bool | Real | String | Dict | Array; optional): accept
- `buttonKind` (Bool | Real | String | Dict | Array; optional): buttonKind
- `className` (String; optional): className
- `disableLabelChanges` (Bool | Real | String | Dict | Array; optional): disableLabelChanges
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `labelText` (Bool | Real | String | Dict | Array; optional): labelText
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `multiple` (Bool | Real | String | Dict | Array; optional): multiple
- `name` (Bool | Real | String | Dict | Array; optional): name
- `onChange` (Bool | Real | String | Dict | Array; optional): onChange
- `onClick` (Bool | Real | String | Dict | Array; optional): onClick
- `role` (Bool | Real | String | Dict | Array; optional): role
- `size` (Bool | Real | String | Dict | Array; optional): size
- `style` (Dict; optional): style
- `tabIndex` (Bool | Real | String | Dict | Array; optional): tabIndex
"""
function fileuploaderbutton(; kwargs...)
        available_props = Symbol[:children, :id, :accept, :buttonKind, :className, :disableLabelChanges, :disabled, :labelText, :loading_state, :multiple, :name, :onChange, :onClick, :role, :size, :style, :tabIndex]
        wild_props = Symbol[]
        return Component("fileuploaderbutton", "FileUploaderButton", "carbon_dash", available_props, wild_props; kwargs...)
end

fileuploaderbutton(children::Any; kwargs...) = fileuploaderbutton(;kwargs..., children = children)
fileuploaderbutton(children_maker::Function; kwargs...) = fileuploaderbutton(children_maker(); kwargs...)

