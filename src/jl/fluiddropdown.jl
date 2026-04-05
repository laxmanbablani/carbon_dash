# AUTO GENERATED FILE - DO NOT EDIT

export fluiddropdown

"""
    fluiddropdown(;kwargs...)
    fluiddropdown(children::Any;kwargs...)
    fluiddropdown(children_maker::Function;kwargs...)


A FluidDropdown component.
FluidDropdown is a wrapper for the Carbon FluidDropdown component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `direction` (Bool | Real | String | Dict | Array; optional): direction
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `initialSelectedItem` (Bool | Real | String | Dict | Array; optional): initialSelectedItem
- `invalid` (Bool | Real | String | Dict | Array; optional): invalid
- `invalidText` (Bool | Real | String | Dict | Array; optional): invalidText
- `isCondensed` (Bool | Real | String | Dict | Array; optional): isCondensed
- `itemToElement` (Bool | Real | String | Dict | Array; optional): itemToElement
- `itemToString` (Bool | Real | String | Dict | Array; optional): itemToString
- `items` (Bool | Real | String | Dict | Array; optional): items
- `label` (Bool | Real | String | Dict | Array; optional): label
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `onChange` (Bool | Real | String | Dict | Array; optional): onChange
- `renderSelectedItem` (Bool | Real | String | Dict | Array; optional): renderSelectedItem
- `selectedItem` (Bool | Real | String | Dict | Array; optional): selectedItem
- `style` (Dict; optional): style
- `titleText` (Bool | Real | String | Dict | Array; optional): titleText
- `translateWithId` (Bool | Real | String | Dict | Array; optional): translateWithId
- `warn` (Bool | Real | String | Dict | Array; optional): warn
- `warnText` (Bool | Real | String | Dict | Array; optional): warnText
"""
function fluiddropdown(; kwargs...)
        available_props = Symbol[:children, :id, :className, :direction, :disabled, :initialSelectedItem, :invalid, :invalidText, :isCondensed, :itemToElement, :itemToString, :items, :label, :loading_state, :onChange, :renderSelectedItem, :selectedItem, :style, :titleText, :translateWithId, :warn, :warnText]
        wild_props = Symbol[]
        return Component("fluiddropdown", "FluidDropdown", "carbon_dash", available_props, wild_props; kwargs...)
end

fluiddropdown(children::Any; kwargs...) = fluiddropdown(;kwargs..., children = children)
fluiddropdown(children_maker::Function; kwargs...) = fluiddropdown(children_maker(); kwargs...)

