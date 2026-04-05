# AUTO GENERATED FILE - DO NOT EDIT

export structuredlistinput

"""
    structuredlistinput(;kwargs...)
    structuredlistinput(children::Any;kwargs...)
    structuredlistinput(children_maker::Function;kwargs...)


A StructuredListInput component.
StructuredListInput is a wrapper for the Carbon StructuredListInput component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `debounce` (Bool | Real; optional): debounce
- `defaultChecked` (Bool | Real | String | Dict | Array; optional): defaultChecked
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
- `style` (Dict; optional): style
- `title` (Bool | Real | String | Dict | Array; optional): title
- `value` (Bool | Real | String | Dict | Array; optional): value
"""
function structuredlistinput(; kwargs...)
        available_props = Symbol[:children, :id, :className, :debounce, :defaultChecked, :loading_state, :n_blur, :n_submit, :name, :onChange, :persisted_props, :persistence, :persistence_type, :style, :title, :value]
        wild_props = Symbol[]
        return Component("structuredlistinput", "StructuredListInput", "carbon_dash", available_props, wild_props; kwargs...)
end

structuredlistinput(children::Any; kwargs...) = structuredlistinput(;kwargs..., children = children)
structuredlistinput(children_maker::Function; kwargs...) = structuredlistinput(children_maker(); kwargs...)

