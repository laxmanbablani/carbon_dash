# AUTO GENERATED FILE - DO NOT EDIT

export dropdown

"""
    dropdown(;kwargs...)
    dropdown(children::Any;kwargs...)
    dropdown(children_maker::Function;kwargs...)


A Dropdown component.
Dropdown is a wrapper for the Carbon Dropdown component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `ariaLabel` (Bool | Real | String | Dict | Array; optional): ariaLabel
- `autoAlign` (Bool | Real | String | Dict | Array; optional): autoAlign
- `className` (String; optional): className
- `decorator` (Bool | Real | String | Dict | Array; optional): decorator
- `direction` (Bool | Real | String | Dict | Array; optional): direction
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `downshiftProps` (Bool | Real | String | Dict | Array; optional): downshiftProps
- `helperText` (Bool | Real | String | Dict | Array; optional): helperText
- `hideLabel` (Bool | Real | String | Dict | Array; optional): hideLabel
- `initialSelectedItem` (Bool | Real | String | Dict | Array; optional): initialSelectedItem
- `invalid` (Bool | Real | String | Dict | Array; optional): invalid
- `invalidText` (Bool | Real | String | Dict | Array; optional): invalidText
- `itemToElement` (Bool | Real | String | Dict | Array; optional): itemToElement
- `itemToString` (Bool | Real | String | Dict | Array; optional): itemToString
- `items` (Array; optional): items
- `label` (String; optional): label
- `light` (Bool | Real | String | Dict | Array; optional): light
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `onChange` (Bool | Real | String | Dict | Array; optional): onChange
- `persisted_props` (Array of Strings; optional): persisted_props
- `persistence` (Bool | String | Real; optional): persistence
- `persistence_type` (a value equal to: 'local', 'session', 'memory'; optional): persistence_type
- `readOnly` (Bool | Real | String | Dict | Array; optional): readOnly
- `renderSelectedItem` (Bool | Real | String | Dict | Array; optional): renderSelectedItem
- `selectedItem` (Bool | Real | String | Dict | Array; optional): selectedItem
- `size` (Bool | Real | String | Dict | Array; optional): size
- `slug` (Bool | Real | String | Dict | Array; optional): slug
- `style` (Dict; optional): style
- `title` (String; optional): title
- `titleText` (Bool | Real | String | Dict | Array; optional): titleText
- `translateWithId` (Bool | Real | String | Dict | Array; optional): translateWithId
- `type` (Bool | Real | String | Dict | Array; optional): type
- `warn` (Bool | Real | String | Dict | Array; optional): warn
- `warnText` (Bool | Real | String | Dict | Array; optional): warnText
"""
function dropdown(; kwargs...)
        available_props = Symbol[:children, :id, :ariaLabel, :autoAlign, :className, :decorator, :direction, :disabled, :downshiftProps, :helperText, :hideLabel, :initialSelectedItem, :invalid, :invalidText, :itemToElement, :itemToString, :items, :label, :light, :loading_state, :onChange, :persisted_props, :persistence, :persistence_type, :readOnly, :renderSelectedItem, :selectedItem, :size, :slug, :style, :title, :titleText, :translateWithId, :type, :warn, :warnText]
        wild_props = Symbol[]
        return Component("dropdown", "Dropdown", "carbon_dash", available_props, wild_props; kwargs...)
end

dropdown(children::Any; kwargs...) = dropdown(;kwargs..., children = children)
dropdown(children_maker::Function; kwargs...) = dropdown(children_maker(); kwargs...)

