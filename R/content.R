# AUTO GENERATED FILE - DO NOT EDIT

#' @export
content <- function(children=NULL, id=NULL, className=NULL, loading_state=NULL, style=NULL, tagName=NULL) {
    
    props <- list(children=children, id=id, className=className, loading_state=loading_state, style=style, tagName=tagName)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Content',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'loading_state', 'style', 'tagName'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
