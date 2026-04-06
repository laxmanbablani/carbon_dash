# AUTO GENERATED FILE - DO NOT EDIT

export tag

"""
    tag(;kwargs...)
    tag(children::Any;kwargs...)
    tag(children_maker::Function;kwargs...)


A Tag component.
Tag is a wrapper for the Carbon Tag component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `as_` (Bool | Real | String | Dict | Array; optional): as
- `className` (String; optional): className
- `decorator` (Bool | Real | String | Dict | Array; optional): decorator
- `disabled` (Bool; optional): disabled
- `filter` (Bool | Real | String | Dict | Array; optional): filter
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `onClose` (Bool | Real | String | Dict | Array; optional): onClose
- `renderIcon` (a list of or a singular dash component, string or number; optional): renderIcon
- `size` (String; optional): size
- `slug` (Bool | Real | String | Dict | Array; optional): slug
- `style` (Dict; optional): style
- `title` (Bool | Real | String | Dict | Array; optional): title
- `type` (String; optional): type
"""
function tag(; kwargs...)
        available_props = Symbol[:children, :id, :as_, :className, :decorator, :disabled, :filter, :loading_state, :onClose, :renderIcon, :size, :slug, :style, :title, :type]
        wild_props = Symbol[]
        return Component("tag", "Tag", "carbon_dash", available_props, wild_props; kwargs...)
end

tag(children::Any; kwargs...) = tag(;kwargs..., children = children)
tag(children_maker::Function; kwargs...) = tag(children_maker(); kwargs...)

