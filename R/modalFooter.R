# AUTO GENERATED FILE - DO NOT EDIT

#' @export
modalFooter <- function(children=NULL, id=NULL, className=NULL, closeModal=NULL, danger=NULL, inputref=NULL, loadingDescription=NULL, loadingIconDescription=NULL, loadingStatus=NULL, loading_state=NULL, onLoadingSuccess=NULL, onRequestClose=NULL, onRequestSubmit=NULL, primaryButtonDisabled=NULL, primaryButtonText=NULL, primaryClassName=NULL, secondaryButtonText=NULL, secondaryButtons=NULL, secondaryClassName=NULL, style=NULL) {
    
    props <- list(children=children, id=id, className=className, closeModal=closeModal, danger=danger, inputref=inputref, loadingDescription=loadingDescription, loadingIconDescription=loadingIconDescription, loadingStatus=loadingStatus, loading_state=loading_state, onLoadingSuccess=onLoadingSuccess, onRequestClose=onRequestClose, onRequestSubmit=onRequestSubmit, primaryButtonDisabled=primaryButtonDisabled, primaryButtonText=primaryButtonText, primaryClassName=primaryClassName, secondaryButtonText=secondaryButtonText, secondaryButtons=secondaryButtons, secondaryClassName=secondaryClassName, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'ModalFooter',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'closeModal', 'danger', 'inputref', 'loadingDescription', 'loadingIconDescription', 'loadingStatus', 'loading_state', 'onLoadingSuccess', 'onRequestClose', 'onRequestSubmit', 'primaryButtonDisabled', 'primaryButtonText', 'primaryClassName', 'secondaryButtonText', 'secondaryButtons', 'secondaryClassName', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
