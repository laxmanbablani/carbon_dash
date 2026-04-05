# AUTO GENERATED FILE - DO NOT EDIT

export button

"""
    button(;kwargs...)
    button(children::Any;kwargs...)
    button(children_maker::Function;kwargs...)


A Button component.
Button is a wrapper for the Carbon Button component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `as_` (Bool | Real | String | Dict | Array; optional): as
- `autoAlign` (Bool | Real | String | Dict | Array; optional): autoAlign
- `className` (String; optional): className
- `dangerDescription` (Bool | Real | String | Dict | Array; optional): dangerDescription
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `hasIconOnly` (Bool | Real | String | Dict | Array; optional): hasIconOnly
- `href` (Bool | Real | String | Dict | Array; optional): href
- `iconDescription` (Bool | Real | String | Dict | Array; optional): iconDescription
- `isExpressive` (Bool | Real | String | Dict | Array; optional): isExpressive
- `isSelected` (Bool | Real | String | Dict | Array; optional): isSelected
- `kind` (Bool | Real | String | Dict | Array; optional): kind
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `n_clicks` (Real; optional): n_clicks
- `onBlur` (Bool | Real | String | Dict | Array; optional): onBlur
- `onClick` (Bool | Real | String | Dict | Array; optional): onClick
- `onFocus` (Bool | Real | String | Dict | Array; optional): onFocus
- `onMouseEnter` (Bool | Real | String | Dict | Array; optional): onMouseEnter
- `onMouseLeave` (Bool | Real | String | Dict | Array; optional): onMouseLeave
- `persisted_props` (Array of Strings; optional): persisted_props
- `persistence` (Bool | String | Real; optional): persistence
- `persistence_type` (a value equal to: 'local', 'session', 'memory'; optional): persistence_type
- `rel` (Bool | Real | String | Dict | Array; optional): rel
- `renderIcon` (Bool | Real | String | Dict | Array; optional): renderIcon
- `role` (Bool | Real | String | Dict | Array; optional): role
- `size` (Bool | Real | String | Dict | Array; optional): size
- `style` (Dict; optional): style
- `tabIndex` (Bool | Real | String | Dict | Array; optional): tabIndex
- `target` (Bool | Real | String | Dict | Array; optional): target
- `tooltipAlignment` (Bool | Real | String | Dict | Array; optional): tooltipAlignment
- `tooltipDropShadow` (Bool | Real | String | Dict | Array; optional): tooltipDropShadow
- `tooltipHighContrast` (Bool | Real | String | Dict | Array; optional): tooltipHighContrast
- `tooltipPosition` (Bool | Real | String | Dict | Array; optional): tooltipPosition
- `type` (Bool | Real | String | Dict | Array; optional): type
"""
function button(; kwargs...)
        available_props = Symbol[:children, :id, :as_, :autoAlign, :className, :dangerDescription, :disabled, :hasIconOnly, :href, :iconDescription, :isExpressive, :isSelected, :kind, :loading_state, :n_clicks, :onBlur, :onClick, :onFocus, :onMouseEnter, :onMouseLeave, :persisted_props, :persistence, :persistence_type, :rel, :renderIcon, :role, :size, :style, :tabIndex, :target, :tooltipAlignment, :tooltipDropShadow, :tooltipHighContrast, :tooltipPosition, :type]
        wild_props = Symbol[]
        return Component("button", "Button", "carbon_dash", available_props, wild_props; kwargs...)
end

button(children::Any; kwargs...) = button(;kwargs..., children = children)
button(children_maker::Function; kwargs...) = button(children_maker(); kwargs...)

