# AUTO GENERATED FILE - DO NOT EDIT

export progressbar

"""
    progressbar(;kwargs...)
    progressbar(children::Any;kwargs...)
    progressbar(children_maker::Function;kwargs...)


A ProgressBar component.
ProgressBar is a wrapper for the Carbon ProgressBar component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `debounce` (Bool | Real; optional): debounce
- `helperText` (Bool | Real | String | Dict | Array; optional): helperText
- `hideLabel` (Bool | Real | String | Dict | Array; optional): hideLabel
- `label` (Bool | Real | String | Dict | Array; optional): label
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `max` (Bool | Real | String | Dict | Array; optional): max
- `n_blur` (Real; optional): n_blur
- `n_submit` (Real; optional): n_submit
- `persisted_props` (Array of Strings; optional): persisted_props
- `persistence` (Bool | String | Real; optional): persistence
- `persistence_type` (a value equal to: 'local', 'session', 'memory'; optional): persistence_type
- `size` (Bool | Real | String | Dict | Array; optional): size
- `status` (Bool | Real | String | Dict | Array; optional): status
- `style` (Dict; optional): style
- `type` (Bool | Real | String | Dict | Array; optional): type
- `value` (Bool | Real | String | Dict | Array; optional): value
"""
function progressbar(; kwargs...)
        available_props = Symbol[:children, :id, :className, :debounce, :helperText, :hideLabel, :label, :loading_state, :max, :n_blur, :n_submit, :persisted_props, :persistence, :persistence_type, :size, :status, :style, :type, :value]
        wild_props = Symbol[]
        return Component("progressbar", "ProgressBar", "carbon_dash", available_props, wild_props; kwargs...)
end

progressbar(children::Any; kwargs...) = progressbar(;kwargs..., children = children)
progressbar(children_maker::Function; kwargs...) = progressbar(children_maker(); kwargs...)

