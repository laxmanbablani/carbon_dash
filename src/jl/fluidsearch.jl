# AUTO GENERATED FILE - DO NOT EDIT

export fluidsearch

"""
    fluidsearch(;kwargs...)
    fluidsearch(children::Any;kwargs...)
    fluidsearch(children_maker::Function;kwargs...)


A FluidSearch component.
FluidSearch is a wrapper for the Carbon FluidSearch component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `autoComplete` (Bool | Real | String | Dict | Array; optional): autoComplete
- `className` (String; optional): className
- `closeButtonLabelText` (Bool | Real | String | Dict | Array; optional): closeButtonLabelText
- `debounce` (Bool | Real; optional): debounce
- `defaultValue` (Bool | Real | String | Dict | Array; optional): defaultValue
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `labelText` (Bool | Real | String | Dict | Array; optional): labelText
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `n_blur` (Real; optional): n_blur
- `n_submit` (Real; optional): n_submit
- `onChange` (Bool | Real | String | Dict | Array; optional): onChange
- `onClear` (Bool | Real | String | Dict | Array; optional): onClear
- `onKeyDown` (Bool | Real | String | Dict | Array; optional): onKeyDown
- `persisted_props` (Array of Strings; optional): persisted_props
- `persistence` (Bool | String | Real; optional): persistence
- `persistence_type` (a value equal to: 'local', 'session', 'memory'; optional): persistence_type
- `placeholder` (Bool | Real | String | Dict | Array; optional): placeholder
- `role` (Bool | Real | String | Dict | Array; optional): role
- `style` (Dict; optional): style
- `type` (Bool | Real | String | Dict | Array; optional): type
- `value` (Bool | Real | String | Dict | Array; optional): value
"""
function fluidsearch(; kwargs...)
        available_props = Symbol[:children, :id, :autoComplete, :className, :closeButtonLabelText, :debounce, :defaultValue, :disabled, :labelText, :loading_state, :n_blur, :n_submit, :onChange, :onClear, :onKeyDown, :persisted_props, :persistence, :persistence_type, :placeholder, :role, :style, :type, :value]
        wild_props = Symbol[]
        return Component("fluidsearch", "FluidSearch", "carbon_dash", available_props, wild_props; kwargs...)
end

fluidsearch(children::Any; kwargs...) = fluidsearch(;kwargs..., children = children)
fluidsearch(children_maker::Function; kwargs...) = fluidsearch(children_maker(); kwargs...)

