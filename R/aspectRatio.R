# AUTO GENERATED FILE - DO NOT EDIT

#' @export
aspectRatio <- function(children=NULL, id=NULL, as_=NULL, className=NULL, loading_state=NULL, ratio=NULL, style=NULL) {
    
    props <- list(children=children, id=id, as_=as_, className=className, loading_state=loading_state, ratio=ratio, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'AspectRatio',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'as_', 'className', 'loading_state', 'ratio', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
