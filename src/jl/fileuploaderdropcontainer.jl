# AUTO GENERATED FILE - DO NOT EDIT

export fileuploaderdropcontainer

"""
    fileuploaderdropcontainer(;kwargs...)
    fileuploaderdropcontainer(children::Any;kwargs...)
    fileuploaderdropcontainer(children_maker::Function;kwargs...)


A FileUploaderDropContainer component.
FileUploaderDropContainer is a wrapper for the Carbon FileUploaderDropContainer component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `accept` (Bool | Real | String | Dict | Array; optional): accept
- `className` (String; optional): className
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `labelText` (Bool | Real | String | Dict | Array; optional): labelText
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `maxFileSize` (Bool | Real | String | Dict | Array; optional): maxFileSize
- `multiple` (Bool | Real | String | Dict | Array; optional): multiple
- `name` (Bool | Real | String | Dict | Array; optional): name
- `onAddFiles` (Bool | Real | String | Dict | Array; optional): onAddFiles
- `onClick` (Bool | Real | String | Dict | Array; optional): onClick
- `pattern` (Bool | Real | String | Dict | Array; optional): pattern
- `role` (Bool | Real | String | Dict | Array; optional): role
- `style` (Dict; optional): style
- `tabIndex` (Bool | Real | String | Dict | Array; optional): tabIndex
"""
function fileuploaderdropcontainer(; kwargs...)
        available_props = Symbol[:children, :id, :accept, :className, :disabled, :labelText, :loading_state, :maxFileSize, :multiple, :name, :onAddFiles, :onClick, :pattern, :role, :style, :tabIndex]
        wild_props = Symbol[]
        return Component("fileuploaderdropcontainer", "FileUploaderDropContainer", "carbon_dash", available_props, wild_props; kwargs...)
end

fileuploaderdropcontainer(children::Any; kwargs...) = fileuploaderdropcontainer(;kwargs..., children = children)
fileuploaderdropcontainer(children_maker::Function; kwargs...) = fileuploaderdropcontainer(children_maker(); kwargs...)

