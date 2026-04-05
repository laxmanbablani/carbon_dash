# AUTO GENERATED FILE - DO NOT EDIT

#' @export
filename <- function(children=NULL, id=NULL, className=NULL, iconDescription=NULL, invalid=NULL, loading_state=NULL, name=NULL, status=NULL, style=NULL, tabIndex=NULL) {
    
    props <- list(children=children, id=id, className=className, iconDescription=iconDescription, invalid=invalid, loading_state=loading_state, name=name, status=status, style=style, tabIndex=tabIndex)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Filename',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'iconDescription', 'invalid', 'loading_state', 'name', 'status', 'style', 'tabIndex'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
