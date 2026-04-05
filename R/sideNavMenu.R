# AUTO GENERATED FILE - DO NOT EDIT

#' @export
sideNavMenu <- function(children=NULL, id=NULL, className=NULL, defaultExpanded=NULL, isActive=NULL, isSideNavExpanded=NULL, large=NULL, loading_state=NULL, renderIcon=NULL, style=NULL, tabIndex=NULL, title=NULL) {
    
    props <- list(children=children, id=id, className=className, defaultExpanded=defaultExpanded, isActive=isActive, isSideNavExpanded=isSideNavExpanded, large=large, loading_state=loading_state, renderIcon=renderIcon, style=style, tabIndex=tabIndex, title=title)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'SideNavMenu',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'defaultExpanded', 'isActive', 'isSideNavExpanded', 'large', 'loading_state', 'renderIcon', 'style', 'tabIndex', 'title'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
