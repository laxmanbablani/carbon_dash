# AUTO GENERATED FILE - DO NOT EDIT

#' @export
codeSnippetSkeleton <- function(children=NULL, id=NULL, className=NULL, loading_state=NULL, style=NULL, type=NULL) {
    
    props <- list(children=children, id=id, className=className, loading_state=loading_state, style=style, type=type)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'CodeSnippetSkeleton',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'loading_state', 'style', 'type'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
