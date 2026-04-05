# AUTO GENERATED FILE - DO NOT EDIT

#' @export
classPrefix <- function(children=NULL, id=NULL, className=NULL, loading_state=NULL, prefix=NULL, style=NULL) {
    
    props <- list(children=children, id=id, className=className, loading_state=loading_state, prefix=prefix, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'ClassPrefix',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'loading_state', 'prefix', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
