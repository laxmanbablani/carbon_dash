# AUTO GENERATED FILE - DO NOT EDIT

export tableselectrow

"""
    tableselectrow(;kwargs...)
    tableselectrow(children::Any;kwargs...)
    tableselectrow(children_maker::Function;kwargs...)


A TableSelectRow component.
TableSelectRow is a wrapper for the Carbon TableSelectRow component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `ariaLabel` (Bool | Real | String | Dict | Array; optional): ariaLabel
- `checked` (Bool; optional): checked
- `className` (String; optional): className
- `debounce` (Bool | Real; optional): debounce
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `n_blur` (Real; optional): n_blur
- `n_submit` (Real; optional): n_submit
- `name` (Bool | Real | String | Dict | Array; optional): name
- `onChange` (Bool | Real | String | Dict | Array; optional): onChange
- `onSelect` (Bool | Real | String | Dict | Array; optional): onSelect
- `persisted_props` (Array of Strings; optional): persisted_props
- `persistence` (Bool | String | Real; optional): persistence
- `persistence_type` (a value equal to: 'local', 'session', 'memory'; optional): persistence_type
- `radio` (Bool | Real | String | Dict | Array; optional): radio
- `style` (Dict; optional): style
"""
function tableselectrow(; kwargs...)
        available_props = Symbol[:children, :id, :ariaLabel, :checked, :className, :debounce, :disabled, :loading_state, :n_blur, :n_submit, :name, :onChange, :onSelect, :persisted_props, :persistence, :persistence_type, :radio, :style]
        wild_props = Symbol[]
        return Component("tableselectrow", "TableSelectRow", "carbon_dash", available_props, wild_props; kwargs...)
end

tableselectrow(children::Any; kwargs...) = tableselectrow(;kwargs..., children = children)
tableselectrow(children_maker::Function; kwargs...) = tableselectrow(children_maker(); kwargs...)

