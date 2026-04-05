# AUTO GENERATED FILE - DO NOT EDIT

#' @export
operationalTag <- function(children=NULL, id=NULL, className=NULL, disabled=NULL, loading_state=NULL, renderIcon=NULL, size=NULL, style=NULL, text=NULL, type=NULL) {
    
    props <- list(children=children, id=id, className=className, disabled=disabled, loading_state=loading_state, renderIcon=renderIcon, size=size, style=style, text=text, type=type)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'OperationalTag',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'disabled', 'loading_state', 'renderIcon', 'size', 'style', 'text', 'type'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
