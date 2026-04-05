# AUTO GENERATED FILE - DO NOT EDIT

export fileuploaderskeleton

"""
    fileuploaderskeleton(;kwargs...)
    fileuploaderskeleton(children::Any;kwargs...)
    fileuploaderskeleton(children_maker::Function;kwargs...)


A FileUploaderSkeleton component.
FileUploaderSkeleton is a wrapper for the Carbon FileUploaderSkeleton component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `style` (Dict; optional): style
"""
function fileuploaderskeleton(; kwargs...)
        available_props = Symbol[:children, :id, :className, :loading_state, :style]
        wild_props = Symbol[]
        return Component("fileuploaderskeleton", "FileUploaderSkeleton", "carbon_dash", available_props, wild_props; kwargs...)
end

fileuploaderskeleton(children::Any; kwargs...) = fileuploaderskeleton(;kwargs..., children = children)
fileuploaderskeleton(children_maker::Function; kwargs...) = fileuploaderskeleton(children_maker(); kwargs...)

