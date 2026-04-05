# AUTO GENERATED FILE - DO NOT EDIT

#' @export
skipToContent <- function(children=NULL, id=NULL, className=NULL, href=NULL, loading_state=NULL, style=NULL, tabIndex=NULL) {
    
    props <- list(children=children, id=id, className=className, href=href, loading_state=loading_state, style=style, tabIndex=tabIndex)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'SkipToContent',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'href', 'loading_state', 'style', 'tabIndex'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
