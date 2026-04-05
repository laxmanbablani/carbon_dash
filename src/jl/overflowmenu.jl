# AUTO GENERATED FILE - DO NOT EDIT

export overflowmenu

"""
    overflowmenu(;kwargs...)
    overflowmenu(children::Any;kwargs...)
    overflowmenu(children_maker::Function;kwargs...)


An OverflowMenu component.
OverflowMenu is a wrapper for the Carbon OverflowMenu component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `align` (Bool | Real | String | Dict | Array; optional): align
- `ariaLabel` (Bool | Real | String | Dict | Array; optional): ariaLabel
- `className` (String; optional): className
- `direction` (Bool | Real | String | Dict | Array; optional): direction
- `flipped` (Bool | Real | String | Dict | Array; optional): flipped
- `focusTrap` (Bool | Real | String | Dict | Array; optional): focusTrap
- `iconClass` (Bool | Real | String | Dict | Array; optional): iconClass
- `iconDescription` (Bool | Real | String | Dict | Array; optional): iconDescription
- `left` (Bool | Real | String | Dict | Array; optional): left
- `light` (Bool | Real | String | Dict | Array; optional): light
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `menuOffset` (Bool | Real | String | Dict | Array; optional): menuOffset
- `menuOffsetFlip` (Bool | Real | String | Dict | Array; optional): menuOffsetFlip
- `menuOptionsClass` (Bool | Real | String | Dict | Array; optional): menuOptionsClass
- `onClick` (Bool | Real | String | Dict | Array; optional): onClick
- `onClose` (Bool | Real | String | Dict | Array; optional): onClose
- `onFocus` (Bool | Real | String | Dict | Array; optional): onFocus
- `onKeyDown` (Bool | Real | String | Dict | Array; optional): onKeyDown
- `onOpen` (Bool | Real | String | Dict | Array; optional): onOpen
- `open` (Bool | Real | String | Dict | Array; optional): open
- `renderIcon` (Bool | Real | String | Dict | Array; optional): renderIcon
- `selectorPrimaryFocus` (Bool | Real | String | Dict | Array; optional): selectorPrimaryFocus
- `size` (Bool | Real | String | Dict | Array; optional): size
- `style` (Dict; optional): style
- `top` (Bool | Real | String | Dict | Array; optional): top
"""
function overflowmenu(; kwargs...)
        available_props = Symbol[:children, :id, :align, :ariaLabel, :className, :direction, :flipped, :focusTrap, :iconClass, :iconDescription, :left, :light, :loading_state, :menuOffset, :menuOffsetFlip, :menuOptionsClass, :onClick, :onClose, :onFocus, :onKeyDown, :onOpen, :open, :renderIcon, :selectorPrimaryFocus, :size, :style, :top]
        wild_props = Symbol[]
        return Component("overflowmenu", "OverflowMenu", "carbon_dash", available_props, wild_props; kwargs...)
end

overflowmenu(children::Any; kwargs...) = overflowmenu(;kwargs..., children = children)
overflowmenu(children_maker::Function; kwargs...) = overflowmenu(children_maker(); kwargs...)

