# AUTO GENERATED FILE - DO NOT EDIT

export datepicker

"""
    datepicker(;kwargs...)
    datepicker(children::Any;kwargs...)
    datepicker(children_maker::Function;kwargs...)


A DatePicker component.
DatePicker is a wrapper for the Carbon DatePicker component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `allowInput` (Bool | Real | String | Dict | Array; optional): allowInput
- `appendTo` (Bool | Real | String | Dict | Array; optional): appendTo
- `className` (String; optional): className
- `closeOnSelect` (Bool | Real | String | Dict | Array; optional): closeOnSelect
- `dateFormat` (Bool | Real | String | Dict | Array; optional): dateFormat
- `datePickerType` (String; optional): datePickerType
- `debounce` (Bool | Real; optional): debounce
- `disable` (Bool | Real | String | Dict | Array; optional): disable
- `enable` (Bool | Real | String | Dict | Array; optional): enable
- `inline` (Bool | Real | String | Dict | Array; optional): inline
- `invalid` (Bool | Real | String | Dict | Array; optional): invalid
- `invalidText` (Bool | Real | String | Dict | Array; optional): invalidText
- `light` (Bool | Real | String | Dict | Array; optional): light
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `locale` (Bool | Real | String | Dict | Array; optional): locale
- `maxDate` (Bool | Real | String | Dict | Array; optional): maxDate
- `minDate` (Bool | Real | String | Dict | Array; optional): minDate
- `n_blur` (Real; optional): n_blur
- `n_submit` (Real; optional): n_submit
- `nextMonthAriaLabel` (Bool | Real | String | Dict | Array; optional): nextMonthAriaLabel
- `onChange` (Bool | Real | String | Dict | Array; optional): onChange
- `onClose` (Bool | Real | String | Dict | Array; optional): onClose
- `onOpen` (Bool | Real | String | Dict | Array; optional): onOpen
- `parseDate` (Bool | Real | String | Dict | Array; optional): parseDate
- `persisted_props` (Array of Strings; optional): persisted_props
- `persistence` (Bool | String | Real; optional): persistence
- `persistence_type` (a value equal to: 'local', 'session', 'memory'; optional): persistence_type
- `prevMonthAriaLabel` (Bool | Real | String | Dict | Array; optional): prevMonthAriaLabel
- `readOnly` (Bool | Real | String | Dict | Array; optional): readOnly
- `short` (Bool | Real | String | Dict | Array; optional): short
- `style` (Dict; optional): style
- `value` (Bool | Real | String | Dict | Array; optional): value
- `warn` (Bool | Real | String | Dict | Array; optional): warn
- `warnText` (Bool | Real | String | Dict | Array; optional): warnText
"""
function datepicker(; kwargs...)
        available_props = Symbol[:children, :id, :allowInput, :appendTo, :className, :closeOnSelect, :dateFormat, :datePickerType, :debounce, :disable, :enable, :inline, :invalid, :invalidText, :light, :loading_state, :locale, :maxDate, :minDate, :n_blur, :n_submit, :nextMonthAriaLabel, :onChange, :onClose, :onOpen, :parseDate, :persisted_props, :persistence, :persistence_type, :prevMonthAriaLabel, :readOnly, :short, :style, :value, :warn, :warnText]
        wild_props = Symbol[]
        return Component("datepicker", "DatePicker", "carbon_dash", available_props, wild_props; kwargs...)
end

datepicker(children::Any; kwargs...) = datepicker(;kwargs..., children = children)
datepicker(children_maker::Function; kwargs...) = datepicker(children_maker(); kwargs...)

