# AUTO GENERATED FILE - DO NOT EDIT

export multiselect

"""
    multiselect(;kwargs...)
    multiselect(children::Any;kwargs...)
    multiselect(children_maker::Function;kwargs...)


A MultiSelect component.
MultiSelect is a wrapper for the Carbon MultiSelect component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `autoAlign` (Bool | Real | String | Dict | Array; optional): autoAlign
- `className` (String; optional): className
- `clearSelectionDescription` (Bool | Real | String | Dict | Array; optional): clearSelectionDescription
- `clearSelectionText` (Bool | Real | String | Dict | Array; optional): clearSelectionText
- `compareItems` (Bool | Real | String | Dict | Array; optional): compareItems
- `decorator` (Bool | Real | String | Dict | Array; optional): decorator
- `direction` (Bool | Real | String | Dict | Array; optional): direction
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `downshiftProps` (Bool | Real | String | Dict | Array; optional): downshiftProps
- `helperText` (Bool | Real | String | Dict | Array; optional): helperText
- `hideLabel` (Bool | Real | String | Dict | Array; optional): hideLabel
- `initialSelectedItems` (Bool | Real | String | Dict | Array; optional): initialSelectedItems
- `invalid` (Bool | Real | String | Dict | Array; optional): invalid
- `invalidText` (Bool | Real | String | Dict | Array; optional): invalidText
- `itemToElement` (Bool | Real | String | Dict | Array; optional): itemToElement
- `itemToString` (Bool | Real | String | Dict | Array; optional): itemToString
- `items` (Bool | Real | String | Dict | Array; optional): items
- `label` (Bool | Real | String | Dict | Array; optional): label
- `light` (Bool | Real | String | Dict | Array; optional): light
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `locale` (Bool | Real | String | Dict | Array; optional): locale
- `onChange` (Bool | Real | String | Dict | Array; optional): onChange
- `onMenuChange` (Bool | Real | String | Dict | Array; optional): onMenuChange
- `open` (Bool; optional): open
- `readOnly` (Bool | Real | String | Dict | Array; optional): readOnly
- `selectedItems` (Bool | Real | String | Dict | Array; optional): selectedItems
- `selectionFeedback` (Bool | Real | String | Dict | Array; optional): selectionFeedback
- `size` (Bool | Real | String | Dict | Array; optional): size
- `slug` (Bool | Real | String | Dict | Array; optional): slug
- `sortItems` (Bool | Real | String | Dict | Array; optional): sortItems
- `style` (Dict; optional): style
- `titleText` (Bool | Real | String | Dict | Array; optional): titleText
- `translateWithId` (Bool | Real | String | Dict | Array; optional): translateWithId
- `type` (Bool | Real | String | Dict | Array; optional): type
- `useTitleInItem` (Bool | Real | String | Dict | Array; optional): useTitleInItem
- `warn` (Bool | Real | String | Dict | Array; optional): warn
- `warnText` (Bool | Real | String | Dict | Array; optional): warnText
"""
function multiselect(; kwargs...)
        available_props = Symbol[:children, :id, :autoAlign, :className, :clearSelectionDescription, :clearSelectionText, :compareItems, :decorator, :direction, :disabled, :downshiftProps, :helperText, :hideLabel, :initialSelectedItems, :invalid, :invalidText, :itemToElement, :itemToString, :items, :label, :light, :loading_state, :locale, :onChange, :onMenuChange, :open, :readOnly, :selectedItems, :selectionFeedback, :size, :slug, :sortItems, :style, :titleText, :translateWithId, :type, :useTitleInItem, :warn, :warnText]
        wild_props = Symbol[]
        return Component("multiselect", "MultiSelect", "carbon_dash", available_props, wild_props; kwargs...)
end

multiselect(children::Any; kwargs...) = multiselect(;kwargs..., children = children)
multiselect(children_maker::Function; kwargs...) = multiselect(children_maker(); kwargs...)

