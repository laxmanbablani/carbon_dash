# AUTO GENERATED FILE - DO NOT EDIT

export combobutton

"""
    combobutton(;kwargs...)
    combobutton(children::Any;kwargs...)
    combobutton(children_maker::Function;kwargs...)


A ComboButton component.
ComboButton is a wrapper for the Carbon ComboButton component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `label` (Bool | Real | String | Dict | Array; optional): label
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `menuAlignment` (Bool | Real | String | Dict | Array; optional): menuAlignment
- `onClick` (Bool | Real | String | Dict | Array; optional): onClick
- `size` (Bool | Real | String | Dict | Array; optional): size
- `style` (Dict; optional): style
- `tooltipAlignment` (Bool | Real | String | Dict | Array; optional): tooltipAlignment
- `translateWithId` (Bool | Real | String | Dict | Array; optional): translateWithId
"""
function combobutton(; kwargs...)
        available_props = Symbol[:children, :id, :className, :disabled, :label, :loading_state, :menuAlignment, :onClick, :size, :style, :tooltipAlignment, :translateWithId]
        wild_props = Symbol[]
        return Component("combobutton", "ComboButton", "carbon_dash", available_props, wild_props; kwargs...)
end

combobutton(children::Any; kwargs...) = combobutton(;kwargs..., children = children)
combobutton(children_maker::Function; kwargs...) = combobutton(children_maker(); kwargs...)

