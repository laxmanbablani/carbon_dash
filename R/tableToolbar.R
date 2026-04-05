# AUTO GENERATED FILE - DO NOT EDIT

#' @export
tableToolbar <- function(children=NULL, id=NULL, ariaLabel=NULL, className=NULL, loading_state=NULL, size=NULL, style=NULL) {
    
    props <- list(children=children, id=id, ariaLabel=ariaLabel, className=className, loading_state=loading_state, size=size, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'TableToolbar',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'ariaLabel', 'className', 'loading_state', 'size', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
