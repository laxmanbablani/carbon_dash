# AUTO GENERATED FILE - DO NOT EDIT

export modalfooter

"""
    modalfooter(;kwargs...)
    modalfooter(children::Any;kwargs...)
    modalfooter(children_maker::Function;kwargs...)


A ModalFooter component.
ModalFooter is a wrapper for the Carbon ModalFooter component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `closeModal` (Bool | Real | String | Dict | Array; optional): closeModal
- `danger` (Bool | Real | String | Dict | Array; optional): danger
- `inputref` (Bool | Real | String | Dict | Array; optional): inputref
- `loadingDescription` (Bool | Real | String | Dict | Array; optional): loadingDescription
- `loadingIconDescription` (Bool | Real | String | Dict | Array; optional): loadingIconDescription
- `loadingStatus` (Bool | Real | String | Dict | Array; optional): loadingStatus
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `onLoadingSuccess` (Bool | Real | String | Dict | Array; optional): onLoadingSuccess
- `onRequestClose` (Bool | Real | String | Dict | Array; optional): onRequestClose
- `onRequestSubmit` (Bool | Real | String | Dict | Array; optional): onRequestSubmit
- `primaryButtonDisabled` (Bool | Real | String | Dict | Array; optional): primaryButtonDisabled
- `primaryButtonText` (Bool | Real | String | Dict | Array; optional): primaryButtonText
- `primaryClassName` (Bool | Real | String | Dict | Array; optional): primaryClassName
- `secondaryButtonText` (Bool | Real | String | Dict | Array; optional): secondaryButtonText
- `secondaryButtons` (Bool | Real | String | Dict | Array; optional): secondaryButtons
- `secondaryClassName` (Bool | Real | String | Dict | Array; optional): secondaryClassName
- `style` (Dict; optional): style
"""
function modalfooter(; kwargs...)
        available_props = Symbol[:children, :id, :className, :closeModal, :danger, :inputref, :loadingDescription, :loadingIconDescription, :loadingStatus, :loading_state, :onLoadingSuccess, :onRequestClose, :onRequestSubmit, :primaryButtonDisabled, :primaryButtonText, :primaryClassName, :secondaryButtonText, :secondaryButtons, :secondaryClassName, :style]
        wild_props = Symbol[]
        return Component("modalfooter", "ModalFooter", "carbon_dash", available_props, wild_props; kwargs...)
end

modalfooter(children::Any; kwargs...) = modalfooter(;kwargs..., children = children)
modalfooter(children_maker::Function; kwargs...) = modalfooter(children_maker(); kwargs...)

