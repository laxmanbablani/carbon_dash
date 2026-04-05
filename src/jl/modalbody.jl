# AUTO GENERATED FILE - DO NOT EDIT

export modalbody

"""
    modalbody(;kwargs...)
    modalbody(children::Any;kwargs...)
    modalbody(children_maker::Function;kwargs...)


A ModalBody component.
ModalBody is a wrapper for the Carbon ModalBody component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `hasForm` (Bool | Real | String | Dict | Array; optional): hasForm
- `hasScrollingContent` (Bool | Real | String | Dict | Array; optional): hasScrollingContent
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `style` (Dict; optional): style
"""
function modalbody(; kwargs...)
        available_props = Symbol[:children, :id, :className, :hasForm, :hasScrollingContent, :loading_state, :style]
        wild_props = Symbol[]
        return Component("modalbody", "ModalBody", "carbon_dash", available_props, wild_props; kwargs...)
end

modalbody(children::Any; kwargs...) = modalbody(;kwargs..., children = children)
modalbody(children_maker::Function; kwargs...) = modalbody(children_maker(); kwargs...)

