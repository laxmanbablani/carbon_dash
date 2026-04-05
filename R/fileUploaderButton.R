# AUTO GENERATED FILE - DO NOT EDIT

#' @export
fileUploaderButton <- function(children=NULL, id=NULL, accept=NULL, buttonKind=NULL, className=NULL, disableLabelChanges=NULL, disabled=NULL, labelText=NULL, loading_state=NULL, multiple=NULL, name=NULL, onChange=NULL, onClick=NULL, role=NULL, size=NULL, style=NULL, tabIndex=NULL) {
    
    props <- list(children=children, id=id, accept=accept, buttonKind=buttonKind, className=className, disableLabelChanges=disableLabelChanges, disabled=disabled, labelText=labelText, loading_state=loading_state, multiple=multiple, name=name, onChange=onChange, onClick=onClick, role=role, size=size, style=style, tabIndex=tabIndex)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'FileUploaderButton',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'accept', 'buttonKind', 'className', 'disableLabelChanges', 'disabled', 'labelText', 'loading_state', 'multiple', 'name', 'onChange', 'onClick', 'role', 'size', 'style', 'tabIndex'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
