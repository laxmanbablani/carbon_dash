# AUTO GENERATED FILE - DO NOT EDIT

export selectitem

"""
    selectitem(;kwargs...)
    selectitem(children::Any;kwargs...)
    selectitem(children_maker::Function;kwargs...)


A SelectItem component.
SelectItem is a wrapper for the Carbon SelectItem component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `debounce` (Bool | Real; optional): debounce
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `hidden` (Bool | Real | String | Dict | Array; optional): hidden
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `n_blur` (Real; optional): n_blur
- `n_submit` (Real; optional): n_submit
- `persisted_props` (Array of Strings; optional): persisted_props
- `persistence` (Bool | String | Real; optional): persistence
- `persistence_type` (a value equal to: 'local', 'session', 'memory'; optional): persistence_type
- `style` (Dict; optional): style
- `text` (String; optional): text
- `value` (Bool | Real | String | Dict | Array; optional): value
"""
function selectitem(; kwargs...)
        available_props = Symbol[:children, :id, :className, :debounce, :disabled, :hidden, :loading_state, :n_blur, :n_submit, :persisted_props, :persistence, :persistence_type, :style, :text, :value]
        wild_props = Symbol[]
        return Component("selectitem", "SelectItem", "carbon_dash", available_props, wild_props; kwargs...)
end

selectitem(children::Any; kwargs...) = selectitem(;kwargs..., children = children)
selectitem(children_maker::Function; kwargs...) = selectitem(children_maker(); kwargs...)

