# AUTO GENERATED FILE - DO NOT EDIT

#' @export
headerMenuItem <- function(children=NULL, id=NULL, as_=NULL, className=NULL, element=NULL, isActive=NULL, isCurrentPage=NULL, isSideNavExpanded=NULL, loading_state=NULL, role=NULL, style=NULL, tabIndex=NULL) {
    
    props <- list(children=children, id=id, as_=as_, className=className, element=element, isActive=isActive, isCurrentPage=isCurrentPage, isSideNavExpanded=isSideNavExpanded, loading_state=loading_state, role=role, style=style, tabIndex=tabIndex)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'HeaderMenuItem',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'as_', 'className', 'element', 'isActive', 'isCurrentPage', 'isSideNavExpanded', 'loading_state', 'role', 'style', 'tabIndex'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
