# AUTO GENERATED FILE - DO NOT EDIT

export modalheader

"""
    modalheader(;kwargs...)
    modalheader(children::Any;kwargs...)
    modalheader(children_maker::Function;kwargs...)


A ModalHeader component.
ModalHeader is a wrapper for the Carbon ModalHeader component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `buttonOnClick` (Bool | Real | String | Dict | Array; optional): buttonOnClick
- `className` (String; optional): className
- `closeClassName` (Bool | Real | String | Dict | Array; optional): closeClassName
- `closeIconClassName` (a list of or a singular dash component, string or number; optional): closeIconClassName
- `closeModal` (Bool | Real | String | Dict | Array; optional): closeModal
- `iconDescription` (Bool | Real | String | Dict | Array; optional): iconDescription
- `label` (Bool | Real | String | Dict | Array; optional): label
- `labelClassName` (Bool | Real | String | Dict | Array; optional): labelClassName
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `style` (Dict; optional): style
- `title` (Bool | Real | String | Dict | Array; optional): title
- `titleClassName` (Bool | Real | String | Dict | Array; optional): titleClassName
"""
function modalheader(; kwargs...)
        available_props = Symbol[:children, :id, :buttonOnClick, :className, :closeClassName, :closeIconClassName, :closeModal, :iconDescription, :label, :labelClassName, :loading_state, :style, :title, :titleClassName]
        wild_props = Symbol[]
        return Component("modalheader", "ModalHeader", "carbon_dash", available_props, wild_props; kwargs...)
end

modalheader(children::Any; kwargs...) = modalheader(;kwargs..., children = children)
modalheader(children_maker::Function; kwargs...) = modalheader(children_maker(); kwargs...)

