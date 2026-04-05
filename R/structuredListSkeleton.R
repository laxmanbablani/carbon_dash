# AUTO GENERATED FILE - DO NOT EDIT

#' @export
structuredListSkeleton <- function(children=NULL, id=NULL, className=NULL, loading_state=NULL, rowCount=NULL, style=NULL) {
    
    props <- list(children=children, id=id, className=className, loading_state=loading_state, rowCount=rowCount, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'StructuredListSkeleton',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'loading_state', 'rowCount', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
