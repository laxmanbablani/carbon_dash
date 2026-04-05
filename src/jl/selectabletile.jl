# AUTO GENERATED FILE - DO NOT EDIT

export selectabletile

"""
    selectabletile(;kwargs...)
    selectabletile(children::Any;kwargs...)
    selectabletile(children_maker::Function;kwargs...)


A SelectableTile component.
SelectableTile is a wrapper for the Carbon SelectableTile component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `debounce` (Bool | Real; optional): debounce
- `decorator` (Bool | Real | String | Dict | Array; optional): decorator
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `hasRoundedCorners` (Bool | Real | String | Dict | Array; optional): hasRoundedCorners
- `light` (Bool | Real | String | Dict | Array; optional): light
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `n_blur` (Real; optional): n_blur
- `n_submit` (Real; optional): n_submit
- `name` (Bool | Real | String | Dict | Array; optional): name
- `onChange` (Bool | Real | String | Dict | Array; optional): onChange
- `onClick` (Bool | Real | String | Dict | Array; optional): onClick
- `onKeyDown` (Bool | Real | String | Dict | Array; optional): onKeyDown
- `persisted_props` (Array of Strings; optional): persisted_props
- `persistence` (Bool | String | Real; optional): persistence
- `persistence_type` (a value equal to: 'local', 'session', 'memory'; optional): persistence_type
- `selected` (Bool | Real | String | Dict | Array; optional): selected
- `slug` (Bool | Real | String | Dict | Array; optional): slug
- `style` (Dict; optional): style
- `tabIndex` (Bool | Real | String | Dict | Array; optional): tabIndex
- `title` (Bool | Real | String | Dict | Array; optional): title
- `value` (Bool | Real | String | Dict | Array; optional): value
"""
function selectabletile(; kwargs...)
        available_props = Symbol[:children, :id, :className, :debounce, :decorator, :disabled, :hasRoundedCorners, :light, :loading_state, :n_blur, :n_submit, :name, :onChange, :onClick, :onKeyDown, :persisted_props, :persistence, :persistence_type, :selected, :slug, :style, :tabIndex, :title, :value]
        wild_props = Symbol[]
        return Component("selectabletile", "SelectableTile", "carbon_dash", available_props, wild_props; kwargs...)
end

selectabletile(children::Any; kwargs...) = selectabletile(;kwargs..., children = children)
selectabletile(children_maker::Function; kwargs...) = selectabletile(children_maker(); kwargs...)

