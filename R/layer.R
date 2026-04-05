# AUTO GENERATED FILE - DO NOT EDIT

#' @export
layer <- function(children=NULL, id=NULL, as_=NULL, className=NULL, level=NULL, loading_state=NULL, style=NULL, withBackground=NULL) {
    
    props <- list(children=children, id=id, as_=as_, className=className, level=level, loading_state=loading_state, style=style, withBackground=withBackground)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Layer',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'as_', 'className', 'level', 'loading_state', 'style', 'withBackground'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
