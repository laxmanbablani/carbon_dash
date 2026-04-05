# AUTO GENERATED FILE - DO NOT EDIT

export expandablesearch

"""
    expandablesearch(;kwargs...)
    expandablesearch(children::Any;kwargs...)
    expandablesearch(children_maker::Function;kwargs...)


An ExpandableSearch component.
ExpandableSearch is a wrapper for the Carbon ExpandableSearch component.
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
- `renderIcon` (Bool | Real | String | Dict | Array; optional): renderIcon
- `role` (Bool | Real | String | Dict | Array; optional): role
- `size` (Bool | Real | String | Dict | Array; optional): size
- `style` (Dict; optional): style
- `type` (Bool | Real | String | Dict | Array; optional): type
- `value` (Bool | Real | String | Dict | Array; optional): value
"""
function expandablesearch(; kwargs...)
        available_props = Symbol[:children, :id, :autoComplete, :className, :closeButtonLabelText, :debounce, :defaultValue, :disabled, :isExpanded, :labelText, :light, :loading_state, :n_blur, :n_submit, :onChange, :onClear, :onExpand, :onKeyDown, :persisted_props, :persistence, :persistence_type, :placeholder, :renderIcon, :role, :size, :style, :type, :value]
        wild_props = Symbol[]
        return Component("expandablesearch", "ExpandableSearch", "carbon_dash", available_props, wild_props; kwargs...)
end

expandablesearch(children::Any; kwargs...) = expandablesearch(;kwargs..., children = children)
expandablesearch(children_maker::Function; kwargs...) = expandablesearch(children_maker(); kwargs...)

