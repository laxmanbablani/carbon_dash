# AUTO GENERATED FILE - DO NOT EDIT

export accordionitem

"""
    accordionitem(;kwargs...)
    accordionitem(children::Any;kwargs...)
    accordionitem(children_maker::Function;kwargs...)


An AccordionItem component.
AccordionItem is a wrapper for the Carbon AccordionItem component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `onClick` (Bool | Real | String | Dict | Array; optional): onClick
- `onHeadingClick` (Bool | Real | String | Dict | Array; optional): onHeadingClick
- `open` (Bool; optional): open
- `persisted_props` (Array of Strings; optional): persisted_props
- `persistence` (Bool | String | Real; optional): persistence
- `persistence_type` (a value equal to: 'local', 'session', 'memory'; optional): persistence_type
- `renderExpando` (Bool | Real | String | Dict | Array; optional): renderExpando
- `renderToggle` (Bool | Real | String | Dict | Array; optional): renderToggle
- `style` (Dict; optional): style
- `title` (a list of or a singular dash component, string or number; optional): title
"""
function accordionitem(; kwargs...)
        available_props = Symbol[:children, :id, :className, :disabled, :loading_state, :onClick, :onHeadingClick, :open, :persisted_props, :persistence, :persistence_type, :renderExpando, :renderToggle, :style, :title]
        wild_props = Symbol[]
        return Component("accordionitem", "AccordionItem", "carbon_dash", available_props, wild_props; kwargs...)
end

accordionitem(children::Any; kwargs...) = accordionitem(;kwargs..., children = children)
accordionitem(children_maker::Function; kwargs...) = accordionitem(children_maker(); kwargs...)

