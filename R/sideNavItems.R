# AUTO GENERATED FILE - DO NOT EDIT

#' @export
sideNavItems <- function(children=NULL, id=NULL, className=NULL, isSideNavExpanded=NULL, loading_state=NULL, style=NULL) {
    
    props <- list(children=children, id=id, className=className, isSideNavExpanded=isSideNavExpanded, loading_state=loading_state, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'SideNavItems',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'isSideNavExpanded', 'loading_state', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
