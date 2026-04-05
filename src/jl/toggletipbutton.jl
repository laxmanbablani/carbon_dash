# AUTO GENERATED FILE - DO NOT EDIT

export toggletipbutton

"""
    toggletipbutton(;kwargs...)
    toggletipbutton(children::Any;kwargs...)
    toggletipbutton(children_maker::Function;kwargs...)


A ToggletipButton component.
ToggletipButton is a wrapper for the Carbon ToggletipButton component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `label` (Bool | Real | String | Dict | Array; optional): label
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `style` (Dict; optional): style
"""
function toggletipbutton(; kwargs...)
        available_props = Symbol[:children, :id, :className, :label, :loading_state, :style]
        wild_props = Symbol[]
        return Component("toggletipbutton", "ToggletipButton", "carbon_dash", available_props, wild_props; kwargs...)
end

toggletipbutton(children::Any; kwargs...) = toggletipbutton(;kwargs..., children = children)
toggletipbutton(children_maker::Function; kwargs...) = toggletipbutton(children_maker(); kwargs...)

