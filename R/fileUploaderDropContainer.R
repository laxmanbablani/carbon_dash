# AUTO GENERATED FILE - DO NOT EDIT

#' @export
fileUploaderDropContainer <- function(children=NULL, id=NULL, accept=NULL, className=NULL, disabled=NULL, labelText=NULL, loading_state=NULL, maxFileSize=NULL, multiple=NULL, name=NULL, onAddFiles=NULL, onClick=NULL, pattern=NULL, role=NULL, style=NULL, tabIndex=NULL) {
    
    props <- list(children=children, id=id, accept=accept, className=className, disabled=disabled, labelText=labelText, loading_state=loading_state, maxFileSize=maxFileSize, multiple=multiple, name=name, onAddFiles=onAddFiles, onClick=onClick, pattern=pattern, role=role, style=style, tabIndex=tabIndex)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'FileUploaderDropContainer',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'accept', 'className', 'disabled', 'labelText', 'loading_state', 'maxFileSize', 'multiple', 'name', 'onAddFiles', 'onClick', 'pattern', 'role', 'style', 'tabIndex'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
