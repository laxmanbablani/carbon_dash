# AUTO GENERATED FILE - DO NOT EDIT

#' @export
headerSideNavItems <- function(children=NULL, id=NULL, className=NULL, hasDivider=NULL, loading_state=NULL, style=NULL) {
    
    props <- list(children=children, id=id, className=className, hasDivider=hasDivider, loading_state=loading_state, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'HeaderSideNavItems',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'hasDivider', 'loading_state', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
