# AUTO GENERATED FILE - DO NOT EDIT

export fluidnumberinput

"""
    fluidnumberinput(;kwargs...)
    fluidnumberinput(children::Any;kwargs...)
    fluidnumberinput(children_maker::Function;kwargs...)


A FluidNumberInput component.
FluidNumberInput is a wrapper for the Carbon FluidNumberInput component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `allowEmpty` (Bool | Real | String | Dict | Array; optional): allowEmpty
- `className` (String; optional): className
- `debounce` (Bool | Real; optional): debounce
- `defaultValue` (Bool | Real | String | Dict | Array; optional): defaultValue
- `disableWheel` (Bool | Real | String | Dict | Array; optional): disableWheel
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `formatOptions` (Bool | Real | String | Dict | Array; optional): formatOptions
- `iconDescription` (Bool | Real | String | Dict | Array; optional): iconDescription
- `inputMode` (Bool | Real | String | Dict | Array; optional): inputMode
- `invalid` (Bool | Real | String | Dict | Array; optional): invalid
- `invalidText` (Bool | Real | String | Dict | Array; optional): invalidText
- `label` (Bool | Real | String | Dict | Array; optional): label
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
- `onChange` (Bool | Real | String | Dict | Array; optional): onChange
- `onClick` (Bool | Real | String | Dict | Array; optional): onClick
- `onKeyUp` (Bool | Real | String | Dict | Array; optional): onKeyUp
- `pattern` (Bool | Real | String | Dict | Array; optional): pattern
- `persisted_props` (Array of Strings; optional): persisted_props
- `persistence` (Bool | String | Real; optional): persistence
- `persistence_type` (a value equal to: 'local', 'session', 'memory'; optional): persistence_type
- `readOnly` (Bool | Real | String | Dict | Array; optional): readOnly
- `step` (Bool | Real | String | Dict | Array; optional): step
- `style` (Dict; optional): style
- `translateWithId` (Bool | Real | String | Dict | Array; optional): translateWithId
- `type` (Bool | Real | String | Dict | Array; optional): type
- `value` (Bool | Real | String | Dict | Array; optional): value
- `warn` (Bool | Real | String | Dict | Array; optional): warn
- `warnText` (Bool | Real | String | Dict | Array; optional): warnText
"""
function fluidnumberinput(; kwargs...)
        available_props = Symbol[:children, :id, :allowEmpty, :className, :debounce, :defaultValue, :disableWheel, :disabled, :formatOptions, :iconDescription, :inputMode, :invalid, :invalidText, :label, :loading_state, :locale, :max, :min, :n_blur, :n_submit, :onChange, :onClick, :onKeyUp, :pattern, :persisted_props, :persistence, :persistence_type, :readOnly, :step, :style, :translateWithId, :type, :value, :warn, :warnText]
        wild_props = Symbol[]
        return Component("fluidnumberinput", "FluidNumberInput", "carbon_dash", available_props, wild_props; kwargs...)
end

fluidnumberinput(children::Any; kwargs...) = fluidnumberinput(;kwargs..., children = children)
fluidnumberinput(children_maker::Function; kwargs...) = fluidnumberinput(children_maker(); kwargs...)

