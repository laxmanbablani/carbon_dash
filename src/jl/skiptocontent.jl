# AUTO GENERATED FILE - DO NOT EDIT

export skiptocontent

"""
    skiptocontent(;kwargs...)
    skiptocontent(children::Any;kwargs...)
    skiptocontent(children_maker::Function;kwargs...)


A SkipToContent component.
SkipToContent is a wrapper for the Carbon SkipToContent component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `href` (Bool | Real | String | Dict | Array; optional): href
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `style` (Dict; optional): style
- `tabIndex` (Bool | Real | String | Dict | Array; optional): tabIndex
"""
function skiptocontent(; kwargs...)
        available_props = Symbol[:children, :id, :className, :href, :loading_state, :style, :tabIndex]
        wild_props = Symbol[]
        return Component("skiptocontent", "SkipToContent", "carbon_dash", available_props, wild_props; kwargs...)
end

skiptocontent(children::Any; kwargs...) = skiptocontent(;kwargs..., children = children)
skiptocontent(children_maker::Function; kwargs...) = skiptocontent(children_maker(); kwargs...)

