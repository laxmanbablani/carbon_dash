# AUTO GENERATED FILE - DO NOT EDIT

#' @export
tabListVertical <- function(children=NULL, id=NULL, activation=NULL, className=NULL, loading_state=NULL, style=NULL) {
    
    props <- list(children=children, id=id, activation=activation, className=className, loading_state=loading_state, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'TabListVertical',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'activation', 'className', 'loading_state', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
