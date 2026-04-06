# AUTO GENERATED FILE - DO NOT EDIT

export headerpanel

"""
    headerpanel(;kwargs...)
    headerpanel(children::Any;kwargs...)
    headerpanel(children_maker::Function;kwargs...)


A HeaderPanel component.
HeaderPanel is a wrapper for the Carbon HeaderPanel component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `addFocusListeners` (Bool | Real | String | Dict | Array; optional): addFocusListeners
- `className` (String; optional): className
- `expanded` (Bool; optional): expanded
- `href` (Bool | Real | String | Dict | Array; optional): href
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `onHeaderPanelFocus` (Bool | Real | String | Dict | Array; optional): onHeaderPanelFocus
- `style` (Dict; optional): style
"""
function headerpanel(; kwargs...)
        available_props = Symbol[:children, :id, :addFocusListeners, :className, :expanded, :href, :loading_state, :onHeaderPanelFocus, :style]
        wild_props = Symbol[]
        return Component("headerpanel", "HeaderPanel", "carbon_dash", available_props, wild_props; kwargs...)
end

headerpanel(children::Any; kwargs...) = headerpanel(;kwargs..., children = children)
headerpanel(children_maker::Function; kwargs...) = headerpanel(children_maker(); kwargs...)

