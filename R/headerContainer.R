# AUTO GENERATED FILE - DO NOT EDIT

#' @export
headerContainer <- function(children=NULL, id=NULL, className=NULL, isSideNavExpanded=NULL, loading_state=NULL, render=NULL, style=NULL) {
    
    props <- list(children=children, id=id, className=className, isSideNavExpanded=isSideNavExpanded, loading_state=loading_state, render=render, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'HeaderContainer',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'isSideNavExpanded', 'loading_state', 'render', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
