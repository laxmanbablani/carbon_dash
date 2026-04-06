# AUTO GENERATED FILE - DO NOT EDIT

export modalwrapper

"""
    modalwrapper(;kwargs...)
    modalwrapper(children::Any;kwargs...)
    modalwrapper(children_maker::Function;kwargs...)


A ModalWrapper component.
ModalWrapper is a wrapper for the Carbon ModalWrapper component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `buttonTriggerClassName` (Bool | Real | String | Dict | Array; optional): buttonTriggerClassName
- `buttonTriggerText` (Bool | Real | String | Dict | Array; optional): buttonTriggerText
- `className` (String; optional): className
- `disabled` (Bool | Real | String | Dict | Array; optional): disabled
- `handleOpen` (Bool | Real | String | Dict | Array; optional): handleOpen
- `handleSubmit` (Bool | Real | String | Dict | Array; optional): handleSubmit
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `modalBeforeContent` (Bool | Real | String | Dict | Array; optional): modalBeforeContent
- `modalHeading` (Bool | Real | String | Dict | Array; optional): modalHeading
- `modalLabel` (Bool | Real | String | Dict | Array; optional): modalLabel
- `modalText` (Bool | Real | String | Dict | Array; optional): modalText
- `onKeyDown` (Bool | Real | String | Dict | Array; optional): onKeyDown
- `passiveModal` (Bool | Real | String | Dict | Array; optional): passiveModal
- `preventCloseOnClickOutside` (Bool | Real | String | Dict | Array; optional): preventCloseOnClickOutside
- `primaryButtonText` (Bool | Real | String | Dict | Array; optional): primaryButtonText
- `renderTriggerButtonIcon` (a list of or a singular dash component, string or number; optional): renderTriggerButtonIcon
- `secondaryButtonText` (Bool | Real | String | Dict | Array; optional): secondaryButtonText
- `selectorPrimaryFocus` (Bool | Real | String | Dict | Array; optional): selectorPrimaryFocus
- `shouldCloseAfterSubmit` (Bool | Real | String | Dict | Array; optional): shouldCloseAfterSubmit
- `status` (Bool | Real | String | Dict | Array; optional): status
- `style` (Dict; optional): style
- `triggerButtonIconDescription` (Bool | Real | String | Dict | Array; optional): triggerButtonIconDescription
- `triggerButtonKind` (Bool | Real | String | Dict | Array; optional): triggerButtonKind
- `withHeader` (Bool | Real | String | Dict | Array; optional): withHeader
"""
function modalwrapper(; kwargs...)
        available_props = Symbol[:children, :id, :buttonTriggerClassName, :buttonTriggerText, :className, :disabled, :handleOpen, :handleSubmit, :loading_state, :modalBeforeContent, :modalHeading, :modalLabel, :modalText, :onKeyDown, :passiveModal, :preventCloseOnClickOutside, :primaryButtonText, :renderTriggerButtonIcon, :secondaryButtonText, :selectorPrimaryFocus, :shouldCloseAfterSubmit, :status, :style, :triggerButtonIconDescription, :triggerButtonKind, :withHeader]
        wild_props = Symbol[]
        return Component("modalwrapper", "ModalWrapper", "carbon_dash", available_props, wild_props; kwargs...)
end

modalwrapper(children::Any; kwargs...) = modalwrapper(;kwargs..., children = children)
modalwrapper(children_maker::Function; kwargs...) = modalwrapper(children_maker(); kwargs...)

