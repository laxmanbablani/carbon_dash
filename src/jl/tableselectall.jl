# AUTO GENERATED FILE - DO NOT EDIT

export tableselectall

"""
    tableselectall(;kwargs...)
    tableselectall(children::Any;kwargs...)
    tableselectall(children_maker::Function;kwargs...)


A TableSelectAll component.
TableSelectAll is a wrapper for the Carbon TableSelectAll component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `ariaLabel` (Bool | Real | String | Dict | Array; optional): ariaLabel
- `checked` (Bool; optional): checked
- `className` (String; optional): className
- `debounce` (Bool | Real; optional): debounce
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `indeterminate` (Bool | Real | String | Dict | Array; optional): indeterminate
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `n_blur` (Real; optional): n_blur
- `n_submit` (Real; optional): n_submit
- `name` (Bool | Real | String | Dict | Array; optional): name
- `onSelect` (Bool | Real | String | Dict | Array; optional): onSelect
- `persisted_props` (Array of Strings; optional): persisted_props
- `persistence` (Bool | String | Real; optional): persistence
- `persistence_type` (a value equal to: 'local', 'session', 'memory'; optional): persistence_type
- `style` (Dict; optional): style
"""
function tableselectall(; kwargs...)
        available_props = Symbol[:children, :id, :ariaLabel, :checked, :className, :debounce, :disabled, :indeterminate, :loading_state, :n_blur, :n_submit, :name, :onSelect, :persisted_props, :persistence, :persistence_type, :style]
        wild_props = Symbol[]
        return Component("tableselectall", "TableSelectAll", "carbon_dash", available_props, wild_props; kwargs...)
end

tableselectall(children::Any; kwargs...) = tableselectall(;kwargs..., children = children)
tableselectall(children_maker::Function; kwargs...) = tableselectall(children_maker(); kwargs...)

