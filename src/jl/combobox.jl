# AUTO GENERATED FILE - DO NOT EDIT

export combobox

"""
    combobox(;kwargs...)
    combobox(children::Any;kwargs...)
    combobox(children_maker::Function;kwargs...)


A ComboBox component.
ComboBox is a wrapper for the Carbon ComboBox component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `allowCustomValue` (Bool | Real | String | Dict | Array; optional): allowCustomValue
- `ariaLabel` (Bool | Real | String | Dict | Array; optional): ariaLabel
- `autoAlign` (Bool | Real | String | Dict | Array; optional): autoAlign
- `className` (String; optional): className
- `decorator` (Bool | Real | String | Dict | Array; optional): decorator
- `direction` (Bool | Real | String | Dict | Array; optional): direction
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `downshiftActions` (Bool | Real | String | Dict | Array; optional): downshiftActions
- `downshiftProps` (Bool | Real | String | Dict | Array; optional): downshiftProps
- `helperText` (Bool | Real | String | Dict | Array; optional): helperText
- `initialSelectedItem` (Bool | Real | String | Dict | Array; optional): initialSelectedItem
- `inputProps` (Bool | Real | String | Dict | Array; optional): inputProps
- `invalid` (Bool | Real | String | Dict | Array; optional): invalid
- `invalidText` (Bool | Real | String | Dict | Array; optional): invalidText
- `itemToElement` (Bool | Real | String | Dict | Array; optional): itemToElement
- `itemToString` (Bool | Real | String | Dict | Array; optional): itemToString
- `items` (Bool | Real | String | Dict | Array; optional): items
- `light` (Bool | Real | String | Dict | Array; optional): light
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `onChange` (Bool | Real | String | Dict | Array; optional): onChange
- `onInputChange` (Bool | Real | String | Dict | Array; optional): onInputChange
- `onToggleClick` (Bool | Real | String | Dict | Array; optional): onToggleClick
- `placeholder` (Bool | Real | String | Dict | Array; optional): placeholder
- `readOnly` (Bool | Real | String | Dict | Array; optional): readOnly
- `selectedItem` (Bool | Real | String | Dict | Array; optional): selectedItem
- `shouldFilterItem` (Bool | Real | String | Dict | Array; optional): shouldFilterItem
- `size` (Bool | Real | String | Dict | Array; optional): size
- `slug` (Bool | Real | String | Dict | Array; optional): slug
- `style` (Dict; optional): style
- `titleText` (Bool | Real | String | Dict | Array; optional): titleText
- `translateWithId` (Bool | Real | String | Dict | Array; optional): translateWithId
- `typeahead` (Bool | Real | String | Dict | Array; optional): typeahead
- `warn` (Bool | Real | String | Dict | Array; optional): warn
- `warnText` (Bool | Real | String | Dict | Array; optional): warnText
"""
function combobox(; kwargs...)
        available_props = Symbol[:children, :id, :allowCustomValue, :ariaLabel, :autoAlign, :className, :decorator, :direction, :disabled, :downshiftActions, :downshiftProps, :helperText, :initialSelectedItem, :inputProps, :invalid, :invalidText, :itemToElement, :itemToString, :items, :light, :loading_state, :onChange, :onInputChange, :onToggleClick, :placeholder, :readOnly, :selectedItem, :shouldFilterItem, :size, :slug, :style, :titleText, :translateWithId, :typeahead, :warn, :warnText]
        wild_props = Symbol[]
        return Component("combobox", "ComboBox", "carbon_dash", available_props, wild_props; kwargs...)
end

combobox(children::Any; kwargs...) = combobox(;kwargs..., children = children)
combobox(children_maker::Function; kwargs...) = combobox(children_maker(); kwargs...)

