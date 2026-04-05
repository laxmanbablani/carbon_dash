# AUTO GENERATED FILE - DO NOT EDIT

#' @export
modal <- function(children=NULL, id=NULL, alert=NULL, className=NULL, closeButtonLabel=NULL, current=NULL, danger=NULL, decorator=NULL, hasScrollingContent=NULL, isFullWidth=NULL, launcherButtonRef=NULL, loadingDescription=NULL, loadingIconDescription=NULL, loadingStatus=NULL, loading_state=NULL, modalAriaLabel=NULL, modalHeading=NULL, modalLabel=NULL, onKeyDown=NULL, onLoadingSuccess=NULL, onRequestClose=NULL, onRequestSubmit=NULL, onSecondarySubmit=NULL, open=NULL, passiveModal=NULL, persisted_props=NULL, persistence=NULL, persistence_type=NULL, preventCloseOnClickOutside=NULL, primaryButtonDisabled=NULL, primaryButtonText=NULL, secondaryButtonText=NULL, secondaryButtons=NULL, selectorPrimaryFocus=NULL, selectorsFloatingMenus=NULL, shouldSubmitOnEnter=NULL, size=NULL, slug=NULL, style=NULL) {
    
    props <- list(children=children, id=id, alert=alert, className=className, closeButtonLabel=closeButtonLabel, current=current, danger=danger, decorator=decorator, hasScrollingContent=hasScrollingContent, isFullWidth=isFullWidth, launcherButtonRef=launcherButtonRef, loadingDescription=loadingDescription, loadingIconDescription=loadingIconDescription, loadingStatus=loadingStatus, loading_state=loading_state, modalAriaLabel=modalAriaLabel, modalHeading=modalHeading, modalLabel=modalLabel, onKeyDown=onKeyDown, onLoadingSuccess=onLoadingSuccess, onRequestClose=onRequestClose, onRequestSubmit=onRequestSubmit, onSecondarySubmit=onSecondarySubmit, open=open, passiveModal=passiveModal, persisted_props=persisted_props, persistence=persistence, persistence_type=persistence_type, preventCloseOnClickOutside=preventCloseOnClickOutside, primaryButtonDisabled=primaryButtonDisabled, primaryButtonText=primaryButtonText, secondaryButtonText=secondaryButtonText, secondaryButtons=secondaryButtons, selectorPrimaryFocus=selectorPrimaryFocus, selectorsFloatingMenus=selectorsFloatingMenus, shouldSubmitOnEnter=shouldSubmitOnEnter, size=size, slug=slug, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Modal',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'alert', 'className', 'closeButtonLabel', 'current', 'danger', 'decorator', 'hasScrollingContent', 'isFullWidth', 'launcherButtonRef', 'loadingDescription', 'loadingIconDescription', 'loadingStatus', 'loading_state', 'modalAriaLabel', 'modalHeading', 'modalLabel', 'onKeyDown', 'onLoadingSuccess', 'onRequestClose', 'onRequestSubmit', 'onSecondarySubmit', 'open', 'passiveModal', 'persisted_props', 'persistence', 'persistence_type', 'preventCloseOnClickOutside', 'primaryButtonDisabled', 'primaryButtonText', 'secondaryButtonText', 'secondaryButtons', 'selectorPrimaryFocus', 'selectorsFloatingMenus', 'shouldSubmitOnEnter', 'size', 'slug', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
