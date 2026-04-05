# AUTO GENERATED FILE - DO NOT EDIT

#' @export
modalWrapper <- function(children=NULL, id=NULL, buttonTriggerClassName=NULL, buttonTriggerText=NULL, className=NULL, disabled=NULL, handleOpen=NULL, handleSubmit=NULL, loading_state=NULL, modalBeforeContent=NULL, modalHeading=NULL, modalLabel=NULL, modalText=NULL, onKeyDown=NULL, passiveModal=NULL, preventCloseOnClickOutside=NULL, primaryButtonText=NULL, renderTriggerButtonIcon=NULL, secondaryButtonText=NULL, selectorPrimaryFocus=NULL, shouldCloseAfterSubmit=NULL, status=NULL, style=NULL, triggerButtonIconDescription=NULL, triggerButtonKind=NULL, withHeader=NULL) {
    
    props <- list(children=children, id=id, buttonTriggerClassName=buttonTriggerClassName, buttonTriggerText=buttonTriggerText, className=className, disabled=disabled, handleOpen=handleOpen, handleSubmit=handleSubmit, loading_state=loading_state, modalBeforeContent=modalBeforeContent, modalHeading=modalHeading, modalLabel=modalLabel, modalText=modalText, onKeyDown=onKeyDown, passiveModal=passiveModal, preventCloseOnClickOutside=preventCloseOnClickOutside, primaryButtonText=primaryButtonText, renderTriggerButtonIcon=renderTriggerButtonIcon, secondaryButtonText=secondaryButtonText, selectorPrimaryFocus=selectorPrimaryFocus, shouldCloseAfterSubmit=shouldCloseAfterSubmit, status=status, style=style, triggerButtonIconDescription=triggerButtonIconDescription, triggerButtonKind=triggerButtonKind, withHeader=withHeader)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'ModalWrapper',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'buttonTriggerClassName', 'buttonTriggerText', 'className', 'disabled', 'handleOpen', 'handleSubmit', 'loading_state', 'modalBeforeContent', 'modalHeading', 'modalLabel', 'modalText', 'onKeyDown', 'passiveModal', 'preventCloseOnClickOutside', 'primaryButtonText', 'renderTriggerButtonIcon', 'secondaryButtonText', 'selectorPrimaryFocus', 'shouldCloseAfterSubmit', 'status', 'style', 'triggerButtonIconDescription', 'triggerButtonKind', 'withHeader'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
