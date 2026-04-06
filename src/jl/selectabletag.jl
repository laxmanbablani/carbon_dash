# AUTO GENERATED FILE - DO NOT EDIT

export selectabletag

"""
    selectabletag(;kwargs...)
    selectabletag(children::Any;kwargs...)
    selectabletag(children_maker::Function;kwargs...)


A SelectableTag component.
SelectableTag is a wrapper for the Carbon SelectableTag component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `defaultSelected` (Bool | Real | String | Dict | Array; optional): defaultSelected
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `onChange` (Bool | Real | String | Dict | Array; optional): onChange
- `onClick` (Bool | Real | String | Dict | Array; optional): onClick
- `renderIcon` (a list of or a singular dash component, string or number; optional): renderIcon
- `selected` (Bool | Real | String | Dict | Array; optional): selected
- `size` (Bool | Real | String | Dict | Array; optional): size
- `style` (Dict; optional): style
- `text` (Bool | Real | String | Dict | Array; optional): text
"""
function selectabletag(; kwargs...)
        available_props = Symbol[:children, :id, :className, :defaultSelected, :disabled, :loading_state, :onChange, :onClick, :renderIcon, :selected, :size, :style, :text]
        wild_props = Symbol[]
        return Component("selectabletag", "SelectableTag", "carbon_dash", available_props, wild_props; kwargs...)
end

selectabletag(children::Any; kwargs...) = selectabletag(;kwargs..., children = children)
selectabletag(children_maker::Function; kwargs...) = selectabletag(children_maker(); kwargs...)

