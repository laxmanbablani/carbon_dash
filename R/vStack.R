# AUTO GENERATED FILE - DO NOT EDIT

#' @export
vStack <- function(children=NULL, id=NULL, as_=NULL, className=NULL, gap=NULL, loading_state=NULL, orientation=NULL, style=NULL) {
    
    props <- list(children=children, id=id, as_=as_, className=className, gap=gap, loading_state=loading_state, orientation=orientation, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'VStack',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'as_', 'className', 'gap', 'loading_state', 'orientation', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
