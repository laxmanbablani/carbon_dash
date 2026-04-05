# AUTO GENERATED FILE - DO NOT EDIT

#' @export
sideNavLink <- function(children=NULL, id=NULL, as_=NULL, className=NULL, element=NULL, isActive=NULL, isSideNavExpanded=NULL, large=NULL, loading_state=NULL, renderIcon=NULL, style=NULL, tabIndex=NULL) {
    
    props <- list(children=children, id=id, as_=as_, className=className, element=element, isActive=isActive, isSideNavExpanded=isSideNavExpanded, large=large, loading_state=loading_state, renderIcon=renderIcon, style=style, tabIndex=tabIndex)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'SideNavLink',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'as_', 'className', 'element', 'isActive', 'isSideNavExpanded', 'large', 'loading_state', 'renderIcon', 'style', 'tabIndex'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
