# AUTO GENERATED FILE - DO NOT EDIT

export fileuploader

"""
    fileuploader(;kwargs...)
    fileuploader(children::Any;kwargs...)
    fileuploader(children_maker::Function;kwargs...)


A FileUploader component.
FileUploader is a wrapper for the Carbon FileUploader component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `accept` (Bool | Real | String | Dict | Array; optional): accept
- `buttonKind` (Bool | Real | String | Dict | Array; optional): buttonKind
- `buttonLabel` (Bool | Real | String | Dict | Array; optional): buttonLabel
- `className` (String; optional): className
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `filenameStatus` (Bool | Real | String | Dict | Array; optional): filenameStatus
- `iconDescription` (Bool | Real | String | Dict | Array; optional): iconDescription
- `labelDescription` (Bool | Real | String | Dict | Array; optional): labelDescription
- `labelTitle` (Bool | Real | String | Dict | Array; optional): labelTitle
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `maxFileSize` (Bool | Real | String | Dict | Array; optional): maxFileSize
- `multiple` (Bool | Real | String | Dict | Array; optional): multiple
- `name` (Bool | Real | String | Dict | Array; optional): name
- `onAddFiles` (Bool | Real | String | Dict | Array; optional): onAddFiles
- `onChange` (Bool | Real | String | Dict | Array; optional): onChange
- `onClick` (Bool | Real | String | Dict | Array; optional): onClick
- `onDelete` (Bool | Real | String | Dict | Array; optional): onDelete
- `size` (Bool | Real | String | Dict | Array; optional): size
- `style` (Dict; optional): style
"""
function fileuploader(; kwargs...)
        available_props = Symbol[:children, :id, :accept, :buttonKind, :buttonLabel, :className, :disabled, :filenameStatus, :iconDescription, :labelDescription, :labelTitle, :loading_state, :maxFileSize, :multiple, :name, :onAddFiles, :onChange, :onClick, :onDelete, :size, :style]
        wild_props = Symbol[]
        return Component("fileuploader", "FileUploader", "carbon_dash", available_props, wild_props; kwargs...)
end

fileuploader(children::Any; kwargs...) = fileuploader(;kwargs..., children = children)
fileuploader(children_maker::Function; kwargs...) = fileuploader(children_maker(); kwargs...)

