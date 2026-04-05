# AUTO GENERATED FILE - DO NOT EDIT

export iconswitch

"""
    iconswitch(;kwargs...)
    iconswitch(children::Any;kwargs...)
    iconswitch(children_maker::Function;kwargs...)


An IconSwitch component.
IconSwitch is a wrapper for the Carbon IconSwitch component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `align` (Bool | Real | String | Dict | Array; optional): align
- `className` (String; optional): className
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `enterDelayMs` (Bool | Real | String | Dict | Array; optional): enterDelayMs
- `index` (Bool | Real | String | Dict | Array; optional): index
- `leaveDelayMs` (Bool | Real | String | Dict | Array; optional): leaveDelayMs
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `name` (Bool | Real | String | Dict | Array; optional): name
- `onClick` (Bool | Real | String | Dict | Array; optional): onClick
- `onKeyDown` (Bool | Real | String | Dict | Array; optional): onKeyDown
- `selected` (Bool | Real | String | Dict | Array; optional): selected
- `size` (Bool | Real | String | Dict | Array; optional): size
- `style` (Dict; optional): style
- `text` (Bool | Real | String | Dict | Array; optional): text
"""
function iconswitch(; kwargs...)
        available_props = Symbol[:children, :id, :align, :className, :disabled, :enterDelayMs, :index, :leaveDelayMs, :loading_state, :name, :onClick, :onKeyDown, :selected, :size, :style, :text]
        wild_props = Symbol[]
        return Component("iconswitch", "IconSwitch", "carbon_dash", available_props, wild_props; kwargs...)
end

iconswitch(children::Any; kwargs...) = iconswitch(;kwargs..., children = children)
iconswitch(children_maker::Function; kwargs...) = iconswitch(children_maker(); kwargs...)

