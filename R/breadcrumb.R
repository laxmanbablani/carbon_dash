# AUTO GENERATED FILE - DO NOT EDIT

#' @export
breadcrumb <- function(children=NULL, id=NULL, className=NULL, loading_state=NULL, noTrailingSlash=NULL, size=NULL, style=NULL) {
    
    props <- list(children=children, id=id, className=className, loading_state=loading_state, noTrailingSlash=noTrailingSlash, size=size, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Breadcrumb',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'loading_state', 'noTrailingSlash', 'size', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
