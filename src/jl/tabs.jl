# AUTO GENERATED FILE - DO NOT EDIT

export tabs

"""
    tabs(;kwargs...)
    tabs(children::Any;kwargs...)
    tabs(children_maker::Function;kwargs...)


A Tabs component.
Tabs is a wrapper for the Carbon Tabs component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `defaultSelectedIndex` (Bool | Real | String | Dict | Array; optional): defaultSelectedIndex
- `dismissable` (Bool | Real | String | Dict | Array; optional): dismissable
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `onChange` (Bool | Real | String | Dict | Array; optional): onChange
- `onTabCloseRequest` (Bool | Real | String | Dict | Array; optional): onTabCloseRequest
- `persisted_props` (Array of Strings; optional): persisted_props
- `persistence` (Bool | String | Real; optional): persistence
- `persistence_type` (a value equal to: 'local', 'session', 'memory'; optional): persistence_type
- `selectedIndex` (Real; optional): selectedIndex
- `style` (Dict; optional): style
"""
function tabs(; kwargs...)
        available_props = Symbol[:children, :id, :className, :defaultSelectedIndex, :dismissable, :loading_state, :onChange, :onTabCloseRequest, :persisted_props, :persistence, :persistence_type, :selectedIndex, :style]
        wild_props = Symbol[]
        return Component("tabs", "Tabs", "carbon_dash", available_props, wild_props; kwargs...)
end

tabs(children::Any; kwargs...) = tabs(;kwargs..., children = children)
tabs(children_maker::Function; kwargs...) = tabs(children_maker(); kwargs...)

