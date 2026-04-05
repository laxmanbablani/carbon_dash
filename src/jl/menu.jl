# AUTO GENERATED FILE - DO NOT EDIT

export menu

"""
    menu(;kwargs...)
    menu(children::Any;kwargs...)
    menu(children_maker::Function;kwargs...)


A Menu component.
Menu is a wrapper for the Carbon Menu component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `backgroundToken` (Bool | Real | String | Dict | Array; optional): backgroundToken
- `border` (Bool | Real | String | Dict | Array; optional): border
- `className` (String; optional): className
- `label` (Bool | Real | String | Dict | Array; optional): label
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `menuAlignment` (Bool | Real | String | Dict | Array; optional): menuAlignment
- `mode` (Bool | Real | String | Dict | Array; optional): mode
- `onClose` (Bool | Real | String | Dict | Array; optional): onClose
- `onOpen` (Bool | Real | String | Dict | Array; optional): onOpen
- `open` (Bool | Real | String | Dict | Array; optional): open
- `size` (Bool | Real | String | Dict | Array; optional): size
- `style` (Dict; optional): style
- `target` (Bool | Real | String | Dict | Array; optional): target
- `x` (Bool | Real | String | Dict | Array; optional): x
- `y` (Bool | Real | String | Dict | Array; optional): y
"""
function menu(; kwargs...)
        available_props = Symbol[:children, :id, :backgroundToken, :border, :className, :label, :loading_state, :menuAlignment, :mode, :onClose, :onOpen, :open, :size, :style, :target, :x, :y]
        wild_props = Symbol[]
        return Component("menu", "Menu", "carbon_dash", available_props, wild_props; kwargs...)
end

menu(children::Any; kwargs...) = menu(;kwargs..., children = children)
menu(children_maker::Function; kwargs...) = menu(children_maker(); kwargs...)

