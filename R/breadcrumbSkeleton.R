# AUTO GENERATED FILE - DO NOT EDIT

#' @export
breadcrumbSkeleton <- function(children=NULL, id=NULL, className=NULL, items=NULL, loading_state=NULL, noTrailingSlash=NULL, size=NULL, style=NULL) {
    
    props <- list(children=children, id=id, className=className, items=items, loading_state=loading_state, noTrailingSlash=noTrailingSlash, size=size, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'BreadcrumbSkeleton',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'items', 'loading_state', 'noTrailingSlash', 'size', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
