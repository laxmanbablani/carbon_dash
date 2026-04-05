# AUTO GENERATED FILE - DO NOT EDIT

#' @export
featureFlags <- function(children=NULL, id=NULL, className=NULL, enableDialogElement=NULL, enableEnhancedFileUploader=NULL, enableExperimentalFocusWrapWithoutSentinels=NULL, enableFocusWrapWithoutSentinels=NULL, enablePresence=NULL, enableTreeviewControllable=NULL, enableV12DynamicFloatingStyles=NULL, enableV12Overflowmenu=NULL, enableV12TileDefaultIcons=NULL, enableV12TileRadioIcons=NULL, flags=NULL, loading_state=NULL, style=NULL) {
    
    props <- list(children=children, id=id, className=className, enableDialogElement=enableDialogElement, enableEnhancedFileUploader=enableEnhancedFileUploader, enableExperimentalFocusWrapWithoutSentinels=enableExperimentalFocusWrapWithoutSentinels, enableFocusWrapWithoutSentinels=enableFocusWrapWithoutSentinels, enablePresence=enablePresence, enableTreeviewControllable=enableTreeviewControllable, enableV12DynamicFloatingStyles=enableV12DynamicFloatingStyles, enableV12Overflowmenu=enableV12Overflowmenu, enableV12TileDefaultIcons=enableV12TileDefaultIcons, enableV12TileRadioIcons=enableV12TileRadioIcons, flags=flags, loading_state=loading_state, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'FeatureFlags',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'enableDialogElement', 'enableEnhancedFileUploader', 'enableExperimentalFocusWrapWithoutSentinels', 'enableFocusWrapWithoutSentinels', 'enablePresence', 'enableTreeviewControllable', 'enableV12DynamicFloatingStyles', 'enableV12Overflowmenu', 'enableV12TileDefaultIcons', 'enableV12TileRadioIcons', 'flags', 'loading_state', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
