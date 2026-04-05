# AUTO GENERATED FILE - DO NOT EDIT

#' @export
headerName <- function(children=NULL, id=NULL, as_=NULL, className=NULL, element=NULL, href=NULL, isSideNavExpanded=NULL, loading_state=NULL, prefix=NULL, style=NULL) {
    
    props <- list(children=children, id=id, as_=as_, className=className, element=element, href=href, isSideNavExpanded=isSideNavExpanded, loading_state=loading_state, prefix=prefix, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'HeaderName',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'as_', 'className', 'element', 'href', 'isSideNavExpanded', 'loading_state', 'prefix', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
