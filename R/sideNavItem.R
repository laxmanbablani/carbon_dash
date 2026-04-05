# AUTO GENERATED FILE - DO NOT EDIT

#' @export
sideNavItem <- function(children=NULL, id=NULL, className=NULL, large=NULL, loading_state=NULL, style=NULL) {
    
    props <- list(children=children, id=id, className=className, large=large, loading_state=loading_state, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'SideNavItem',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'large', 'loading_state', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
