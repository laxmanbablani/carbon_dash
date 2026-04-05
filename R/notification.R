# AUTO GENERATED FILE - DO NOT EDIT

#' @export
notification <- function(children=NULL, id=NULL, className=NULL) {
    
    props <- list(children=children, id=id, className=className)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Notification',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
