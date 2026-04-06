# AUTO GENERATED FILE - DO NOT EDIT

export link

"""
    link(;kwargs...)
    link(children::Any;kwargs...)
    link(children_maker::Function;kwargs...)


A Link component.
Link is a wrapper for the Carbon Link component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `as_` (Bool | Real | String | Dict | Array; optional): as
- `className` (String; optional): className
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `href` (Bool | Real | String | Dict | Array; optional): href
- `inline` (Bool | Real | String | Dict | Array; optional): inline
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `renderIcon` (a list of or a singular dash component, string or number; optional): renderIcon
- `size` (Bool | Real | String | Dict | Array; optional): size
- `style` (Dict; optional): style
- `visited` (Bool | Real | String | Dict | Array; optional): visited
"""
function link(; kwargs...)
        available_props = Symbol[:children, :id, :as_, :className, :disabled, :href, :inline, :loading_state, :renderIcon, :size, :style, :visited]
        wild_props = Symbol[]
        return Component("link", "Link", "carbon_dash", available_props, wild_props; kwargs...)
end

link(children::Any; kwargs...) = link(;kwargs..., children = children)
link(children_maker::Function; kwargs...) = link(children_maker(); kwargs...)

