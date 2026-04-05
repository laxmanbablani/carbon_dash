# AUTO GENERATED FILE - DO NOT EDIT

export menubutton

"""
    menubutton(;kwargs...)
    menubutton(children::Any;kwargs...)
    menubutton(children_maker::Function;kwargs...)


A MenuButton component.
MenuButton is a wrapper for the Carbon MenuButton component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `kind` (Bool | Real | String | Dict | Array; optional): kind
- `label` (Bool | Real | String | Dict | Array; optional): label
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `menuAlignment` (Bool | Real | String | Dict | Array; optional): menuAlignment
- `menuBackgroundToken` (Bool | Real | String | Dict | Array; optional): menuBackgroundToken
- `menuBorder` (Bool | Real | String | Dict | Array; optional): menuBorder
- `menuTarget` (Bool | Real | String | Dict | Array; optional): menuTarget
- `size` (Bool | Real | String | Dict | Array; optional): size
- `style` (Dict; optional): style
- `tabIndex` (Bool | Real | String | Dict | Array; optional): tabIndex
"""
function menubutton(; kwargs...)
        available_props = Symbol[:children, :id, :className, :disabled, :kind, :label, :loading_state, :menuAlignment, :menuBackgroundToken, :menuBorder, :menuTarget, :size, :style, :tabIndex]
        wild_props = Symbol[]
        return Component("menubutton", "MenuButton", "carbon_dash", available_props, wild_props; kwargs...)
end

menubutton(children::Any; kwargs...) = menubutton(;kwargs..., children = children)
menubutton(children_maker::Function; kwargs...) = menubutton(children_maker(); kwargs...)

