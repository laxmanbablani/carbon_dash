# AUTO GENERATED FILE - DO NOT EDIT

export treeview

"""
    treeview(;kwargs...)
    treeview(children::Any;kwargs...)
    treeview(children_maker::Function;kwargs...)


A TreeView component.
TreeView is a wrapper for the Carbon TreeView component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `active` (Bool | Real | String | Dict | Array; optional): active
- `className` (String; optional): className
- `hideLabel` (Bool | Real | String | Dict | Array; optional): hideLabel
- `label` (Bool | Real | String | Dict | Array; optional): label
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `multiselect` (Bool | Real | String | Dict | Array; optional): multiselect
- `onActivate` (Bool | Real | String | Dict | Array; optional): onActivate
- `onSelect` (Bool | Real | String | Dict | Array; optional): onSelect
- `persisted_props` (Array of Strings; optional): persisted_props
- `persistence` (Bool | String | Real; optional): persistence
- `persistence_type` (a value equal to: 'local', 'session', 'memory'; optional): persistence_type
- `selected` (Bool | Real | String | Dict | Array; optional): selected
- `size` (Bool | Real | String | Dict | Array; optional): size
- `style` (Dict; optional): style
"""
function treeview(; kwargs...)
        available_props = Symbol[:children, :id, :active, :className, :hideLabel, :label, :loading_state, :multiselect, :onActivate, :onSelect, :persisted_props, :persistence, :persistence_type, :selected, :size, :style]
        wild_props = Symbol[]
        return Component("treeview", "TreeView", "carbon_dash", available_props, wild_props; kwargs...)
end

treeview(children::Any; kwargs...) = treeview(;kwargs..., children = children)
treeview(children_maker::Function; kwargs...) = treeview(children_maker(); kwargs...)

