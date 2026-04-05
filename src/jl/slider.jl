# AUTO GENERATED FILE - DO NOT EDIT

export slider

"""
    slider(;kwargs...)
    slider(children::Any;kwargs...)
    slider(children_maker::Function;kwargs...)


A Slider component.
Slider is a wrapper for the Carbon Slider component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `ariaLabelInput` (Bool | Real | String | Dict | Array; optional): ariaLabelInput
- `className` (String; optional): className
- `debounce` (Bool | Real; optional): debounce
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `formatLabel` (Bool | Real | String | Dict | Array; optional): formatLabel
- `hideLabel` (Bool | Real | String | Dict | Array; optional): hideLabel
- `hideTextInput` (Bool | Real | String | Dict | Array; optional): hideTextInput
- `inputType` (Bool | Real | String | Dict | Array; optional): inputType
- `invalid` (Bool | Real | String | Dict | Array; optional): invalid
- `invalidText` (Bool | Real | String | Dict | Array; optional): invalidText
- `label` (String; optional): label
- `labelText` (Bool | Real | String | Dict | Array; optional): labelText
- `light` (Bool | Real | String | Dict | Array; optional): light
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `max` (Real; optional): max
- `maxLabel` (Bool | Real | String | Dict | Array; optional): maxLabel
- `min` (Real; optional): min
- `minLabel` (Bool | Real | String | Dict | Array; optional): minLabel
- `n_blur` (Real; optional): n_blur
- `n_submit` (Real; optional): n_submit
- `name` (Bool | Real | String | Dict | Array; optional): name
- `onBlur` (Bool | Real | String | Dict | Array; optional): onBlur
- `onChange` (Bool | Real | String | Dict | Array; optional): onChange
- `onInputKeyUp` (Bool | Real | String | Dict | Array; optional): onInputKeyUp
- `onRelease` (Bool | Real | String | Dict | Array; optional): onRelease
- `persisted_props` (Array of Strings; optional): persisted_props
- `persistence` (Bool | String | Real; optional): persistence
- `persistence_type` (a value equal to: 'local', 'session', 'memory'; optional): persistence_type
- `readOnly` (Bool | Real | String | Dict | Array; optional): readOnly
- `required` (Bool | Real | String | Dict | Array; optional): required
- `step` (Bool | Real | String | Dict | Array; optional): step
- `stepMultiplier` (Bool | Real | String | Dict | Array; optional): stepMultiplier
- `style` (Dict; optional): style
- `translateWithId` (Bool | Real | String | Dict | Array; optional): translateWithId
- `unstable_ariaLabelInputUpper` (Bool | Real | String | Dict | Array; optional): unstable_ariaLabelInputUpper
- `unstable_nameUpper` (Bool | Real | String | Dict | Array; optional): unstable_nameUpper
- `unstable_valueUpper` (Bool | Real | String | Dict | Array; optional): unstable_valueUpper
- `value` (Real; optional): value
- `warn` (Bool | Real | String | Dict | Array; optional): warn
- `warnText` (Bool | Real | String | Dict | Array; optional): warnText
"""
function slider(; kwargs...)
        available_props = Symbol[:children, :id, :ariaLabelInput, :className, :debounce, :disabled, :formatLabel, :hideLabel, :hideTextInput, :inputType, :invalid, :invalidText, :label, :labelText, :light, :loading_state, :max, :maxLabel, :min, :minLabel, :n_blur, :n_submit, :name, :onBlur, :onChange, :onInputKeyUp, :onRelease, :persisted_props, :persistence, :persistence_type, :readOnly, :required, :step, :stepMultiplier, :style, :translateWithId, :unstable_ariaLabelInputUpper, :unstable_nameUpper, :unstable_valueUpper, :value, :warn, :warnText]
        wild_props = Symbol[]
        return Component("slider", "Slider", "carbon_dash", available_props, wild_props; kwargs...)
end

slider(children::Any; kwargs...) = slider(;kwargs..., children = children)
slider(children_maker::Function; kwargs...) = slider(children_maker(); kwargs...)

