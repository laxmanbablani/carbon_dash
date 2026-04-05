# AUTO GENERATED FILE - DO NOT EDIT

#' @export
breadcrumbItem <- function(children=NULL, id=NULL, className=NULL, href=NULL, isCurrentPage=NULL, loading_state=NULL, style=NULL) {
    
    props <- list(children=children, id=id, className=className, href=href, isCurrentPage=isCurrentPage, loading_state=loading_state, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'BreadcrumbItem',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'href', 'isCurrentPage', 'loading_state', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
