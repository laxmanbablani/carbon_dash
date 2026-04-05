# AUTO GENERATED FILE - DO NOT EDIT

#' @export
selectSkeleton <- function(children=NULL, id=NULL, className=NULL, hideLabel=NULL, loading_state=NULL, style=NULL) {
    
    props <- list(children=children, id=id, className=className, hideLabel=hideLabel, loading_state=loading_state, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'SelectSkeleton',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'hideLabel', 'loading_state', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
