# AUTO GENERATED FILE - DO NOT EDIT

export modal

"""
    modal(;kwargs...)
    modal(children::Any;kwargs...)
    modal(children_maker::Function;kwargs...)


A Modal component.
Modal is a wrapper for the Carbon Modal component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `alert` (Bool | Real | String | Dict | Array; optional): alert
- `className` (String; optional): className
- `closeButtonLabel` (Bool | Real | String | Dict | Array; optional): closeButtonLabel
- `current` (Bool | Real | String | Dict | Array; optional): current
- `danger` (Bool | Real | String | Dict | Array; optional): danger
- `decorator` (Bool | Real | String | Dict | Array; optional): decorator
- `hasScrollingContent` (Bool | Real | String | Dict | Array; optional): hasScrollingContent
- `isFullWidth` (Bool | Real | String | Dict | Array; optional): isFullWidth
- `launcherButtonRef` (Bool | Real | String | Dict | Array; optional): launcherButtonRef
- `loadingDescription` (Bool | Real | String | Dict | Array; optional): loadingDescription
- `loadingIconDescription` (Bool | Real | String | Dict | Array; optional): loadingIconDescription
- `loadingStatus` (Bool | Real | String | Dict | Array; optional): loadingStatus
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `modalAriaLabel` (Bool | Real | String | Dict | Array; optional): modalAriaLabel
- `modalHeading` (String; optional): modalHeading
- `modalLabel` (Bool | Real | String | Dict | Array; optional): modalLabel
- `onKeyDown` (Bool | Real | String | Dict | Array; optional): onKeyDown
- `onLoadingSuccess` (Bool | Real | String | Dict | Array; optional): onLoadingSuccess
- `onRequestClose` (Bool | Real | String | Dict | Array; optional): onRequestClose
- `onRequestSubmit` (Bool | Real | String | Dict | Array; optional): onRequestSubmit
- `onSecondarySubmit` (Bool | Real | String | Dict | Array; optional): onSecondarySubmit
- `open` (Bool; optional): open
- `passiveModal` (Bool | Real | String | Dict | Array; optional): passiveModal
- `persisted_props` (Array of Strings; optional): persisted_props
- `persistence` (Bool | String | Real; optional): persistence
- `persistence_type` (a value equal to: 'local', 'session', 'memory'; optional): persistence_type
- `preventCloseOnClickOutside` (Bool | Real | String | Dict | Array; optional): preventCloseOnClickOutside
- `primaryButtonDisabled` (Bool | Real | String | Dict | Array; optional): primaryButtonDisabled
- `primaryButtonText` (String; optional): primaryButtonText
- `secondaryButtonText` (String; optional): secondaryButtonText
- `secondaryButtons` (Bool | Real | String | Dict | Array; optional): secondaryButtons
- `selectorPrimaryFocus` (Bool | Real | String | Dict | Array; optional): selectorPrimaryFocus
- `selectorsFloatingMenus` (Bool | Real | String | Dict | Array; optional): selectorsFloatingMenus
- `shouldSubmitOnEnter` (Bool | Real | String | Dict | Array; optional): shouldSubmitOnEnter
- `size` (Bool | Real | String | Dict | Array; optional): size
- `slug` (Bool | Real | String | Dict | Array; optional): slug
- `style` (Dict; optional): style
"""
function modal(; kwargs...)
        available_props = Symbol[:children, :id, :alert, :className, :closeButtonLabel, :current, :danger, :decorator, :hasScrollingContent, :isFullWidth, :launcherButtonRef, :loadingDescription, :loadingIconDescription, :loadingStatus, :loading_state, :modalAriaLabel, :modalHeading, :modalLabel, :onKeyDown, :onLoadingSuccess, :onRequestClose, :onRequestSubmit, :onSecondarySubmit, :open, :passiveModal, :persisted_props, :persistence, :persistence_type, :preventCloseOnClickOutside, :primaryButtonDisabled, :primaryButtonText, :secondaryButtonText, :secondaryButtons, :selectorPrimaryFocus, :selectorsFloatingMenus, :shouldSubmitOnEnter, :size, :slug, :style]
        wild_props = Symbol[]
        return Component("modal", "Modal", "carbon_dash", available_props, wild_props; kwargs...)
end

modal(children::Any; kwargs...) = modal(;kwargs..., children = children)
modal(children_maker::Function; kwargs...) = modal(children_maker(); kwargs...)

