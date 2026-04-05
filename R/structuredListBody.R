# AUTO GENERATED FILE - DO NOT EDIT

#' @export
structuredListBody <- function(children=NULL, id=NULL, className=NULL, head=NULL, loading_state=NULL, onKeyDown=NULL, style=NULL) {
    
    props <- list(children=children, id=id, className=className, head=head, loading_state=loading_state, onKeyDown=onKeyDown, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'StructuredListBody',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'head', 'loading_state', 'onKeyDown', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
