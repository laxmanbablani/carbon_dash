# AUTO GENERATED FILE - DO NOT EDIT

export featureflags

"""
    featureflags(;kwargs...)
    featureflags(children::Any;kwargs...)
    featureflags(children_maker::Function;kwargs...)


A FeatureFlags component.
FeatureFlags is a wrapper for the Carbon FeatureFlags component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `enableDialogElement` (Bool | Real | String | Dict | Array; optional): enableDialogElement
- `enableEnhancedFileUploader` (Bool | Real | String | Dict | Array; optional): enableEnhancedFileUploader
- `enableExperimentalFocusWrapWithoutSentinels` (Bool | Real | String | Dict | Array; optional): enableExperimentalFocusWrapWithoutSentinels
- `enableFocusWrapWithoutSentinels` (Bool | Real | String | Dict | Array; optional): enableFocusWrapWithoutSentinels
- `enablePresence` (Bool | Real | String | Dict | Array; optional): enablePresence
- `enableTreeviewControllable` (Bool | Real | String | Dict | Array; optional): enableTreeviewControllable
- `enableV12DynamicFloatingStyles` (Bool | Real | String | Dict | Array; optional): enableV12DynamicFloatingStyles
- `enableV12Overflowmenu` (Bool | Real | String | Dict | Array; optional): enableV12Overflowmenu
- `enableV12TileDefaultIcons` (a list of or a singular dash component, string or number; optional): enableV12TileDefaultIcons
- `enableV12TileRadioIcons` (a list of or a singular dash component, string or number; optional): enableV12TileRadioIcons
- `flags` (Bool | Real | String | Dict | Array; optional): flags
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `style` (Dict; optional): style
"""
function featureflags(; kwargs...)
        available_props = Symbol[:children, :id, :className, :enableDialogElement, :enableEnhancedFileUploader, :enableExperimentalFocusWrapWithoutSentinels, :enableFocusWrapWithoutSentinels, :enablePresence, :enableTreeviewControllable, :enableV12DynamicFloatingStyles, :enableV12Overflowmenu, :enableV12TileDefaultIcons, :enableV12TileRadioIcons, :flags, :loading_state, :style]
        wild_props = Symbol[]
        return Component("featureflags", "FeatureFlags", "carbon_dash", available_props, wild_props; kwargs...)
end

featureflags(children::Any; kwargs...) = featureflags(;kwargs..., children = children)
featureflags(children_maker::Function; kwargs...) = featureflags(children_maker(); kwargs...)

