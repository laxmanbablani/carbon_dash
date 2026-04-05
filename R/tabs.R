# AUTO GENERATED FILE - DO NOT EDIT

#' @export
tabs <- function(children=NULL, id=NULL, className=NULL, defaultSelectedIndex=NULL, dismissable=NULL, loading_state=NULL, onChange=NULL, onTabCloseRequest=NULL, persisted_props=NULL, persistence=NULL, persistence_type=NULL, selectedIndex=NULL, style=NULL) {
    
    props <- list(children=children, id=id, className=className, defaultSelectedIndex=defaultSelectedIndex, dismissable=dismissable, loading_state=loading_state, onChange=onChange, onTabCloseRequest=onTabCloseRequest, persisted_props=persisted_props, persistence=persistence, persistence_type=persistence_type, selectedIndex=selectedIndex, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Tabs',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'defaultSelectedIndex', 'dismissable', 'loading_state', 'onChange', 'onTabCloseRequest', 'persisted_props', 'persistence', 'persistence_type', 'selectedIndex', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
