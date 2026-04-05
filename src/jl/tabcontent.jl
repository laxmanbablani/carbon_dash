# AUTO GENERATED FILE - DO NOT EDIT

export tabcontent

"""
    tabcontent(;kwargs...)
    tabcontent(children::Any;kwargs...)
    tabcontent(children_maker::Function;kwargs...)


A TabContent component.
TabContent is a wrapper for the Carbon TabContent component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `selected` (Bool | Real | String | Dict | Array; optional): selected
- `style` (Dict; optional): style
"""
function tabcontent(; kwargs...)
        available_props = Symbol[:children, :id, :className, :loading_state, :selected, :style]
        wild_props = Symbol[]
        return Component("tabcontent", "TabContent", "carbon_dash", available_props, wild_props; kwargs...)
end

tabcontent(children::Any; kwargs...) = tabcontent(;kwargs..., children = children)
tabcontent(children_maker::Function; kwargs...) = tabcontent(children_maker(); kwargs...)

