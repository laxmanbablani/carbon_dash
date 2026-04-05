# AUTO GENERATED FILE - DO NOT EDIT

export numberinput

"""
    numberinput(;kwargs...)
    numberinput(children::Any;kwargs...)
    numberinput(children_maker::Function;kwargs...)


A NumberInput component.
NumberInput is a wrapper for the Carbon NumberInput component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `allowEmpty` (Bool | Real | String | Dict | Array; optional): allowEmpty
- `className` (String; optional): className
- `debounce` (Bool | Real; optional): debounce
- `decorator` (Bool | Real | String | Dict | Array; optional): decorator
- `defaultValue` (Bool | Real | String | Dict | Array; optional): defaultValue
- `disableWheel` (Bool | Real | String | Dict | Array; optional): disableWheel
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `formatOptions` (Bool | Real | String | Dict | Array; optional): formatOptions
- `helperText` (Bool | Real | String | Dict | Array; optional): helperText
- `hideLabel` (Bool | Real | String | Dict | Array; optional): hideLabel
- `hideSteppers` (Bool | Real | String | Dict | Array; optional): hideSteppers
- `iconDescription` (Bool | Real | String | Dict | Array; optional): iconDescription
- `inputMode` (Bool | Real | String | Dict | Array; optional): inputMode
- `invalid` (Bool | Real | String | Dict | Array; optional): invalid
- `invalidText` (Bool | Real | String | Dict | Array; optional): invalidText
- `label` (String; optional): label
- `light` (Bool | Real | String | Dict | Array; optional): light
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `locale` (Bool | Real | String | Dict | Array; optional): locale
- `max` (Bool | Real | String | Dict | Array; optional): max
- `min` (Bool | Real | String | Dict | Array; optional): min
- `n_blur` (Real; optional): n_blur
- `n_submit` (Real; optional): n_submit
- `onBlur` (Bool | Real | String | Dict | Array; optional): onBlur
- `onChange` (Bool | Real | String | Dict | Array; optional): onChange
- `onClick` (Bool | Real | String | Dict | Array; optional): onClick
- `onKeyUp` (Bool | Real | String | Dict | Array; optional): onKeyUp
- `onStepperBlur` (Bool | Real | String | Dict | Array; optional): onStepperBlur
- `pattern` (Bool | Real | String | Dict | Array; optional): pattern
- `persisted_props` (Array of Strings; optional): persisted_props
- `persistence` (Bool | String | Real; optional): persistence
- `persistence_type` (a value equal to: 'local', 'session', 'memory'; optional): persistence_type
- `readOnly` (Bool | Real | String | Dict | Array; optional): readOnly
- `size` (Bool | Real | String | Dict | Array; optional): size
- `slug` (Bool | Real | String | Dict | Array; optional): slug
- `step` (Bool | Real | String | Dict | Array; optional): step
- `stepStartValue` (Bool | Real | String | Dict | Array; optional): stepStartValue
- `style` (Dict; optional): style
- `translateWithId` (Bool | Real | String | Dict | Array; optional): translateWithId
- `type` (Bool | Real | String | Dict | Array; optional): type
- `validate` (Bool | Real | String | Dict | Array; optional): validate
- `value` (Real; optional): value
- `warn` (Bool | Real | String | Dict | Array; optional): warn
- `warnText` (Bool | Real | String | Dict | Array; optional): warnText
"""
function numberinput(; kwargs...)
        available_props = Symbol[:children, :id, :allowEmpty, :className, :debounce, :decorator, :defaultValue, :disableWheel, :disabled, :formatOptions, :helperText, :hideLabel, :hideSteppers, :iconDescription, :inputMode, :invalid, :invalidText, :label, :light, :loading_state, :locale, :max, :min, :n_blur, :n_submit, :onBlur, :onChange, :onClick, :onKeyUp, :onStepperBlur, :pattern, :persisted_props, :persistence, :persistence_type, :readOnly, :size, :slug, :step, :stepStartValue, :style, :translateWithId, :type, :validate, :value, :warn, :warnText]
        wild_props = Symbol[]
        return Component("numberinput", "NumberInput", "carbon_dash", available_props, wild_props; kwargs...)
end

numberinput(children::Any; kwargs...) = numberinput(;kwargs..., children = children)
numberinput(children_maker::Function; kwargs...) = numberinput(children_maker(); kwargs...)

