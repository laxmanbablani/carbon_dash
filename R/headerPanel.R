# AUTO GENERATED FILE - DO NOT EDIT

#' @export
headerPanel <- function(children=NULL, id=NULL, addFocusListeners=NULL, className=NULL, expanded=NULL, href=NULL, loading_state=NULL, onHeaderPanelFocus=NULL, style=NULL) {
    
    props <- list(children=children, id=id, addFocusListeners=addFocusListeners, className=className, expanded=expanded, href=href, loading_state=loading_state, onHeaderPanelFocus=onHeaderPanelFocus, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'HeaderPanel',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'addFocusListeners', 'className', 'expanded', 'href', 'loading_state', 'onHeaderPanelFocus', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
