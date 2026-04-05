# AUTO GENERATED FILE - DO NOT EDIT

#' @export
theme <- function(children=NULL, id=NULL, as_=NULL, className=NULL, loading_state=NULL, style=NULL, theme=NULL) {
    
    props <- list(children=children, id=id, as_=as_, className=className, loading_state=loading_state, style=style, theme=theme)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Theme',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'as_', 'className', 'loading_state', 'style', 'theme'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
