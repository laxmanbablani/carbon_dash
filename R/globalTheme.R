# AUTO GENERATED FILE - DO NOT EDIT

#' @export
globalTheme <- function(children=NULL, id=NULL, className=NULL, loading_state=NULL, style=NULL, theme=NULL) {
    
    props <- list(children=children, id=id, className=className, loading_state=loading_state, style=style, theme=theme)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'GlobalTheme',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'loading_state', 'style', 'theme'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
