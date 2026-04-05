# AUTO GENERATED FILE - DO NOT EDIT

export radiotile

"""
    radiotile(;kwargs...)
    radiotile(children::Any;kwargs...)
    radiotile(children_maker::Function;kwargs...)


A RadioTile component.
RadioTile is a wrapper for the Carbon RadioTile component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `checked` (Bool | Real | String | Dict | Array; optional): checked
- `className` (String; optional): className
- `debounce` (Bool | Real; optional): debounce
- `decorator` (Bool | Real | String | Dict | Array; optional): decorator
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `event` (Bool | Real | String | Dict | Array; optional): event
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
- `persisted_props` (Array of Strings; optional): persisted_props
- `persistence` (Bool | String | Real; optional): persistence
- `persistence_type` (a value equal to: 'local', 'session', 'memory'; optional): persistence_type
- `required` (Bool | Real | String | Dict | Array; optional): required
- `slug` (Bool | Real | String | Dict | Array; optional): slug
- `style` (Dict; optional): style
- `tabIndex` (Bool | Real | String | Dict | Array; optional): tabIndex
- `value` (Bool | Real | String | Dict | Array; optional): value
"""
function radiotile(; kwargs...)
        available_props = Symbol[:children, :id, :checked, :className, :debounce, :decorator, :disabled, :event, :hasRoundedCorners, :light, :loading_state, :n_blur, :n_submit, :name, :onChange, :persisted_props, :persistence, :persistence_type, :required, :slug, :style, :tabIndex, :value]
        wild_props = Symbol[]
        return Component("radiotile", "RadioTile", "carbon_dash", available_props, wild_props; kwargs...)
end

radiotile(children::Any; kwargs...) = radiotile(;kwargs..., children = children)
radiotile(children_maker::Function; kwargs...) = radiotile(children_maker(); kwargs...)

