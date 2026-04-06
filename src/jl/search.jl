# AUTO GENERATED FILE - DO NOT EDIT

export search

"""
    search(;kwargs...)
    search(children::Any;kwargs...)
    search(children_maker::Function;kwargs...)


A Search component.
Search is a wrapper for the Carbon Search component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `autoComplete` (Bool | Real | String | Dict | Array; optional): autoComplete
- `className` (String; optional): className
- `closeButtonLabelText` (Bool | Real | String | Dict | Array; optional): closeButtonLabelText
- `debounce` (Bool | Real; optional): debounce
- `defaultValue` (Bool | Real | String | Dict | Array; optional): defaultValue
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `isExpanded` (Bool | Real | String | Dict | Array; optional): isExpanded
- `labelText` (Bool | Real | String | Dict | Array; optional): labelText
- `light` (Bool | Real | String | Dict | Array; optional): light
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `n_blur` (Real; optional): n_blur
- `n_submit` (Real; optional): n_submit
- `onChange` (Bool | Real | String | Dict | Array; optional): onChange
- `onClear` (Bool | Real | String | Dict | Array; optional): onClear
- `onExpand` (Bool | Real | String | Dict | Array; optional): onExpand
- `onKeyDown` (Bool | Real | String | Dict | Array; optional): onKeyDown
- `persisted_props` (Array of Strings; optional): persisted_props
- `persistence` (Bool | String | Real; optional): persistence
- `persistence_type` (a value equal to: 'local', 'session', 'memory'; optional): persistence_type
- `placeholder` (Bool | Real | String | Dict | Array; optional): placeholder
- `renderIcon` (a list of or a singular dash component, string or number; optional): renderIcon
- `role` (Bool | Real | String | Dict | Array; optional): role
- `size` (Bool | Real | String | Dict | Array; optional): size
- `style` (Dict; optional): style
- `type` (Bool | Real | String | Dict | Array; optional): type
- `value` (String; optional): value
"""
function search(; kwargs...)
        available_props = Symbol[:children, :id, :autoComplete, :className, :closeButtonLabelText, :debounce, :defaultValue, :disabled, :isExpanded, :labelText, :light, :loading_state, :n_blur, :n_submit, :onChange, :onClear, :onExpand, :onKeyDown, :persisted_props, :persistence, :persistence_type, :placeholder, :renderIcon, :role, :size, :style, :type, :value]
        wild_props = Symbol[]
        return Component("search", "Search", "carbon_dash", available_props, wild_props; kwargs...)
end

search(children::Any; kwargs...) = search(;kwargs..., children = children)
search(children_maker::Function; kwargs...) = search(children_maker(); kwargs...)

