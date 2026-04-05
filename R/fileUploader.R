# AUTO GENERATED FILE - DO NOT EDIT

#' @export
fileUploader <- function(children=NULL, id=NULL, accept=NULL, buttonKind=NULL, buttonLabel=NULL, className=NULL, disabled=NULL, filenameStatus=NULL, iconDescription=NULL, labelDescription=NULL, labelTitle=NULL, loading_state=NULL, maxFileSize=NULL, multiple=NULL, name=NULL, onAddFiles=NULL, onChange=NULL, onClick=NULL, onDelete=NULL, size=NULL, style=NULL) {
    
    props <- list(children=children, id=id, accept=accept, buttonKind=buttonKind, buttonLabel=buttonLabel, className=className, disabled=disabled, filenameStatus=filenameStatus, iconDescription=iconDescription, labelDescription=labelDescription, labelTitle=labelTitle, loading_state=loading_state, maxFileSize=maxFileSize, multiple=multiple, name=name, onAddFiles=onAddFiles, onChange=onChange, onClick=onClick, onDelete=onDelete, size=size, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'FileUploader',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'accept', 'buttonKind', 'buttonLabel', 'className', 'disabled', 'filenameStatus', 'iconDescription', 'labelDescription', 'labelTitle', 'loading_state', 'maxFileSize', 'multiple', 'name', 'onAddFiles', 'onChange', 'onClick', 'onDelete', 'size', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
