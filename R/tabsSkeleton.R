# AUTO GENERATED FILE - DO NOT EDIT

#' @export
tabsSkeleton <- function(children=NULL, id=NULL, className=NULL, contained=NULL, loading_state=NULL, style=NULL) {
    
    props <- list(children=children, id=id, className=className, contained=contained, loading_state=loading_state, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'TabsSkeleton',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'contained', 'loading_state', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
