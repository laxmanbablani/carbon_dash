# AUTO GENERATED FILE - DO NOT EDIT

#' @export
tableToolbarMenu <- function(children=NULL, id=NULL, className=NULL, iconDescription=NULL, loading_state=NULL, menuOptionsClass=NULL, renderIcon=NULL, style=NULL) {
    
    props <- list(children=children, id=id, className=className, iconDescription=iconDescription, loading_state=loading_state, menuOptionsClass=menuOptionsClass, renderIcon=renderIcon, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'TableToolbarMenu',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'iconDescription', 'loading_state', 'menuOptionsClass', 'renderIcon', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
