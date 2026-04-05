# AUTO GENERATED FILE - DO NOT EDIT

export fluidmultiselect

"""
    fluidmultiselect(;kwargs...)
    fluidmultiselect(children::Any;kwargs...)
    fluidmultiselect(children_maker::Function;kwargs...)


A FluidMultiSelect component.
FluidMultiSelect is a wrapper for the Carbon FluidMultiSelect component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `clearSelectionDescription` (Bool | Real | String | Dict | Array; optional): clearSelectionDescription
- `clearSelectionText` (Bool | Real | String | Dict | Array; optional): clearSelectionText
- `compareItems` (Bool | Real | String | Dict | Array; optional): compareItems
- `direction` (Bool | Real | String | Dict | Array; optional): direction
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `downshiftProps` (Bool | Real | String | Dict | Array; optional): downshiftProps
- `initialSelectedItems` (Bool | Real | String | Dict | Array; optional): initialSelectedItems
- `invalid` (Bool | Real | String | Dict | Array; optional): invalid
- `invalidText` (Bool | Real | String | Dict | Array; optional): invalidText
- `isCondensed` (Bool | Real | String | Dict | Array; optional): isCondensed
- `isFilterable` (Bool | Real | String | Dict | Array; optional): isFilterable
- `itemToElement` (Bool | Real | String | Dict | Array; optional): itemToElement
- `itemToString` (Bool | Real | String | Dict | Array; optional): itemToString
- `items` (Bool | Real | String | Dict | Array; optional): items
- `label` (Bool | Real | String | Dict | Array; optional): label
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `locale` (Bool | Real | String | Dict | Array; optional): locale
- `onChange` (Bool | Real | String | Dict | Array; optional): onChange
- `onInputValueChange` (Bool | Real | String | Dict | Array; optional): onInputValueChange
- `onMenuChange` (Bool | Real | String | Dict | Array; optional): onMenuChange
- `readOnly` (Bool | Real | String | Dict | Array; optional): readOnly
- `selectedItems` (Bool | Real | String | Dict | Array; optional): selectedItems
- `selectionFeedback` (Bool | Real | String | Dict | Array; optional): selectionFeedback
- `sortItems` (Bool | Real | String | Dict | Array; optional): sortItems
- `style` (Dict; optional): style
- `titleText` (Bool | Real | String | Dict | Array; optional): titleText
- `translateWithId` (Bool | Real | String | Dict | Array; optional): translateWithId
- `useTitleInItem` (Bool | Real | String | Dict | Array; optional): useTitleInItem
- `warn` (Bool | Real | String | Dict | Array; optional): warn
- `warnText` (Bool | Real | String | Dict | Array; optional): warnText
"""
function fluidmultiselect(; kwargs...)
        available_props = Symbol[:children, :id, :className, :clearSelectionDescription, :clearSelectionText, :compareItems, :direction, :disabled, :downshiftProps, :initialSelectedItems, :invalid, :invalidText, :isCondensed, :isFilterable, :itemToElement, :itemToString, :items, :label, :loading_state, :locale, :onChange, :onInputValueChange, :onMenuChange, :readOnly, :selectedItems, :selectionFeedback, :sortItems, :style, :titleText, :translateWithId, :useTitleInItem, :warn, :warnText]
        wild_props = Symbol[]
        return Component("fluidmultiselect", "FluidMultiSelect", "carbon_dash", available_props, wild_props; kwargs...)
end

fluidmultiselect(children::Any; kwargs...) = fluidmultiselect(;kwargs..., children = children)
fluidmultiselect(children_maker::Function; kwargs...) = fluidmultiselect(children_maker(); kwargs...)

