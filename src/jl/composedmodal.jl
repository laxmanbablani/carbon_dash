# AUTO GENERATED FILE - DO NOT EDIT

export composedmodal

"""
    composedmodal(;kwargs...)
    composedmodal(children::Any;kwargs...)
    composedmodal(children_maker::Function;kwargs...)


A ComposedModal component.
ComposedModal is a wrapper for the Carbon ComposedModal component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `containerClassName` (Bool | Real | String | Dict | Array; optional): containerClassName
- `current` (Bool | Real | String | Dict | Array; optional): current
- `danger` (Bool | Real | String | Dict | Array; optional): danger
- `decorator` (Bool | Real | String | Dict | Array; optional): decorator
- `isFullWidth` (Bool | Real | String | Dict | Array; optional): isFullWidth
- `launcherButtonRef` (Bool | Real | String | Dict | Array; optional): launcherButtonRef
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `onClose` (Bool | Real | String | Dict | Array; optional): onClose
- `onKeyDown` (Bool | Real | String | Dict | Array; optional): onKeyDown
- `open` (Bool | Real | String | Dict | Array; optional): open
- `preventCloseOnClickOutside` (Bool | Real | String | Dict | Array; optional): preventCloseOnClickOutside
- `selectorPrimaryFocus` (Bool | Real | String | Dict | Array; optional): selectorPrimaryFocus
- `selectorsFloatingMenus` (Bool | Real | String | Dict | Array; optional): selectorsFloatingMenus
- `size` (Bool | Real | String | Dict | Array; optional): size
- `slug` (Bool | Real | String | Dict | Array; optional): slug
- `style` (Dict; optional): style
"""
function composedmodal(; kwargs...)
        available_props = Symbol[:children, :id, :className, :containerClassName, :current, :danger, :decorator, :isFullWidth, :launcherButtonRef, :loading_state, :onClose, :onKeyDown, :open, :preventCloseOnClickOutside, :selectorPrimaryFocus, :selectorsFloatingMenus, :size, :slug, :style]
        wild_props = Symbol[]
        return Component("composedmodal", "ComposedModal", "carbon_dash", available_props, wild_props; kwargs...)
end

composedmodal(children::Any; kwargs...) = composedmodal(;kwargs..., children = children)
composedmodal(children_maker::Function; kwargs...) = composedmodal(children_maker(); kwargs...)

