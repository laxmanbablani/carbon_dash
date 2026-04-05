# AUTO GENERATED FILE - DO NOT EDIT

#' @export
tabContent <- function(children=NULL, id=NULL, className=NULL, loading_state=NULL, selected=NULL, style=NULL) {
    
    props <- list(children=children, id=id, className=className, loading_state=loading_state, selected=selected, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'TabContent',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'loading_state', 'selected', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
