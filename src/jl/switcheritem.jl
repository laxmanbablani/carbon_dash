# AUTO GENERATED FILE - DO NOT EDIT

export switcheritem

"""
    switcheritem(;kwargs...)
    switcheritem(children::Any;kwargs...)
    switcheritem(children_maker::Function;kwargs...)


A SwitcherItem component.
SwitcherItem is a wrapper for the Carbon SwitcherItem component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `handleSwitcherItemFocus` (Bool | Real | String | Dict | Array; optional): handleSwitcherItemFocus
- `href` (Bool | Real | String | Dict | Array; optional): href
- `index` (Bool | Real | String | Dict | Array; optional): index
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `onClick` (Bool | Real | String | Dict | Array; optional): onClick
- `onKeyDown` (Bool | Real | String | Dict | Array; optional): onKeyDown
- `rel` (Bool | Real | String | Dict | Array; optional): rel
- `style` (Dict; optional): style
- `tabIndex` (Bool | Real | String | Dict | Array; optional): tabIndex
- `target` (Bool | Real | String | Dict | Array; optional): target
"""
function switcheritem(; kwargs...)
        available_props = Symbol[:children, :id, :className, :handleSwitcherItemFocus, :href, :index, :loading_state, :onClick, :onKeyDown, :rel, :style, :tabIndex, :target]
        wild_props = Symbol[]
        return Component("switcheritem", "SwitcherItem", "carbon_dash", available_props, wild_props; kwargs...)
end

switcheritem(children::Any; kwargs...) = switcheritem(;kwargs..., children = children)
switcheritem(children_maker::Function; kwargs...) = switcheritem(children_maker(); kwargs...)

