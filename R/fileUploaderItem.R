# AUTO GENERATED FILE - DO NOT EDIT

#' @export
fileUploaderItem <- function(children=NULL, id=NULL, className=NULL, errorBody=NULL, errorSubject=NULL, iconDescription=NULL, invalid=NULL, loading_state=NULL, name=NULL, onDelete=NULL, size=NULL, status=NULL, style=NULL, uuid=NULL) {
    
    props <- list(children=children, id=id, className=className, errorBody=errorBody, errorSubject=errorSubject, iconDescription=iconDescription, invalid=invalid, loading_state=loading_state, name=name, onDelete=onDelete, size=size, status=status, style=style, uuid=uuid)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'FileUploaderItem',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'errorBody', 'errorSubject', 'iconDescription', 'invalid', 'loading_state', 'name', 'onDelete', 'size', 'status', 'style', 'uuid'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
