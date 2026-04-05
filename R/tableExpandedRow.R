# AUTO GENERATED FILE - DO NOT EDIT

#' @export
tableExpandedRow <- function(children=NULL, id=NULL, className=NULL, colSpan=NULL, loading_state=NULL, style=NULL) {
    
    props <- list(children=children, id=id, className=className, colSpan=colSpan, loading_state=loading_state, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'TableExpandedRow',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'colSpan', 'loading_state', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
