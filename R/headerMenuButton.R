# AUTO GENERATED FILE - DO NOT EDIT

#' @export
headerMenuButton <- function(children=NULL, id=NULL, className=NULL, isActive=NULL, isCollapsible=NULL, loading_state=NULL, onClick=NULL, style=NULL) {
    
    props <- list(children=children, id=id, className=className, isActive=isActive, isCollapsible=isCollapsible, loading_state=loading_state, onClick=onClick, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'HeaderMenuButton',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'isActive', 'isCollapsible', 'loading_state', 'onClick', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
