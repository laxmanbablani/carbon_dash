# AUTO GENERATED FILE - DO NOT EDIT

export radiobutton

"""
    radiobutton(;kwargs...)
    radiobutton(children::Any;kwargs...)
    radiobutton(children_maker::Function;kwargs...)


A RadioButton component.
RadioButton is a wrapper for the Carbon RadioButton component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `checked` (Bool; optional): checked
- `className` (String; optional): className
- `debounce` (Bool | Real; optional): debounce
- `decorator` (Bool | Real | String | Dict | Array; optional): decorator
- `defaultChecked` (Bool | Real | String | Dict | Array; optional): defaultChecked
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `hideLabel` (Bool | Real | String | Dict | Array; optional): hideLabel
- `invalid` (Bool | Real | String | Dict | Array; optional): invalid
- `invalidText` (Bool | Real | String | Dict | Array; optional): invalidText
- `label` (String; optional): label
- `labelPosition` (Bool | Real | String | Dict | Array; optional): labelPosition
- `labelText` (Bool | Real | String | Dict | Array; optional): labelText
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `n_blur` (Real; optional): n_blur
- `n_submit` (Real; optional): n_submit
- `name` (Bool | Real | String | Dict | Array; optional): name
- `onChange` (Bool | Real | String | Dict | Array; optional): onChange
- `onClick` (Bool | Real | String | Dict | Array; optional): onClick
- `persisted_props` (Array of Strings; optional): persisted_props
- `persistence` (Bool | String | Real; optional): persistence
- `persistence_type` (a value equal to: 'local', 'session', 'memory'; optional): persistence_type
- `readOnly` (Bool | Real | String | Dict | Array; optional): readOnly
- `required` (Bool | Real | String | Dict | Array; optional): required
- `slug` (Bool | Real | String | Dict | Array; optional): slug
- `style` (Dict; optional): style
- `value` (Bool | Real | String | Dict | Array; optional): value
- `warn` (Bool | Real | String | Dict | Array; optional): warn
- `warnText` (Bool | Real | String | Dict | Array; optional): warnText
"""
function radiobutton(; kwargs...)
        available_props = Symbol[:children, :id, :checked, :className, :debounce, :decorator, :defaultChecked, :disabled, :hideLabel, :invalid, :invalidText, :label, :labelPosition, :labelText, :loading_state, :n_blur, :n_submit, :name, :onChange, :onClick, :persisted_props, :persistence, :persistence_type, :readOnly, :required, :slug, :style, :value, :warn, :warnText]
        wild_props = Symbol[]
        return Component("radiobutton", "RadioButton", "carbon_dash", available_props, wild_props; kwargs...)
end

radiobutton(children::Any; kwargs...) = radiobutton(;kwargs..., children = children)
radiobutton(children_maker::Function; kwargs...) = radiobutton(children_maker(); kwargs...)

